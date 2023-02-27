import datetime as dt
from time import sleep
from pathlib import Path

from config import dsn, es_params, es_state, etl_fetch_delay, logger
from state import State, YamlFileStorage
from extractor import PostgresExtractor
from loader import ElasticsearchLoader
from transform import DataTransform


def postgres_to_es() -> None:
    """Функция ETL процесса."""

    state = get_state_storage()
    postgres = PostgresExtractor(dsn, state)
    elastic = ElasticsearchLoader(es_params)
    transform = DataTransform()
    while True:
        data = postgres.data_extractor()
        if data:
            prepared_data = transform.transform(data)
            elastic.es_saver(prepared_data)
        sleep(etl_fetch_delay)


def get_state_storage() -> State:
    """Настраивает контейнер для хранения состояний."""

    state_file_path = Path(__file__).parent.joinpath(es_state)
    storage = YamlFileStorage(state_file_path)
    return State(storage)


if __name__ == '__main__':

    logger.info('Скрипт начал работу...')
    postgres_to_es()


