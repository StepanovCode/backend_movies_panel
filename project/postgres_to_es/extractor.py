import datetime as dt
import psycopg2

from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor

from typing import List, Iterator, Tuple, Dict

import querys
from backoff import backoff
from config import logger, fetchmany_size
from state import State


class PostgresExtractor:
    """Загрузка данных из Postgres."""
    connection: _connection
    state: State

    def __init__(self, dsn: Dict, state: State):
        self.dsn = dsn
        self.connection = self.get_connection()
        self.state = state
        self.last_update = None

    @backoff(logger=logger)
    def get_connection(self) -> _connection:
        logger.info('Подключение к БД Postgres...')
        with psycopg2.connect(**self.dsn, cursor_factory=DictCursor) as pg_conn:
            logger.info('Соединение с Postgres установлено.')
            return pg_conn

    def pg_executor(self, query: str, params: Tuple) -> Iterator[Tuple]:
        while True:
            try:
                if self.connection.closed:
                    self.connection = self.get_connection()
                cur = self.connection.cursor()
                cur.execute(query, params)
                while True:
                    data = cur.fetchmany(fetchmany_size)
                    if not data:
                        return
                    for row in data:
                        yield row
            except psycopg2.OperationalError as _ex:
                logger.error(f'Ошибка Postgres при выполении запроса в БД: {_ex}')

    @backoff(logger=logger, is_connection=False)
    def data_extractor(self) -> Iterator[Tuple] | List:
        self.last_update = self.state.get_state('last_update') or dt.datetime.min
        movies_ids = self.pg_executor(querys.movies_data_ids, (self.last_update, ))
        movies_ids = tuple([item[0] for item in movies_ids])
        if movies_ids:
            movies_data = self.pg_executor(querys.movies_data, (movies_ids,))
            now = dt.datetime.utcnow()
            self.state.set_state('last_update', str(now))
            self.last_update = now
            return movies_data
        return []
