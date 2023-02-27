import json
import elasticsearch

from elasticsearch import Elasticsearch, helpers
from pathlib import Path
from dataclasses import asdict
from typing import List, Dict

from backoff import backoff
from config import logger
from dataclass import FilmWork


class ElasticsearchLoader:
    """Загрузка данных в Elasticsearch."""

    def __init__(self, params: Dict):
        self.host = params['host']
        self.port = params['port']
        self.index_name = params['index_name']
        self.index_config = params['index_config']
        self.es_client = self.get_connection_es_client()
        self.create_index()

    @backoff(logger=logger)
    def get_connection_es_client(self) -> Elasticsearch:
        host = f'{self.host}:{self.port}'
        logger.info(f'Создание клиента Elasticsearch...'
                    f'\n адрес: {self.host}:{self.port}')

        _client = Elasticsearch(hosts=host)
        _client.cluster.health(wait_for_status="yellow")
        logger.info('Соединение с Elasticsearch установлено')
        return _client

    def create_index(self) -> None:
        """Создание индекса в Elasticsearch"""

        logger.info(f'Создание индекса: {self.index_name} в Elasticsearch')
        if self.es_client.indices.exists(index=self.index_name):
            logger.info(f'Индекс {self.index_name} уже существует')
            return
        path = Path(__file__).parent.joinpath(self.index_config)
        with open(path, 'r') as index_file:
            index_body = json.load(index_file)

            self.es_client.indices.create(
                index=self.index_name,
                body=index_body
            )
            logger.info(f'Индекс {self.index_name} успешно создан')

    def es_saver(self, data: List[FilmWork]) -> None:
        """Загрузка данных в индекс"""

        actions = [
            {
                "_index": "movies",
                "_id": movie.id,
                "_source": asdict(movie)
            }
            for movie in data
        ]
        while True:
            logger.info('Обновление фильмов...')
            try:
                success, failed = helpers.bulk(
                    client=self.es_client,
                    actions=actions,
                    raise_on_error=False,
                    stats_only=True
                )
                if success:
                    logger.info(f'Обновлено фильмов: {success}')
                if failed:
                    logger.error(f'Данные не смогли обновиться'
                                 f' или добавиться у {failed} фильмов')
                return
            except elasticsearch.ConnectionError as _ex:
                logger.error(f'Ошибка соединения: {_ex}')
                self.es_client = self.get_connection_es_client()
