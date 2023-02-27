from typing import List, Iterator, Tuple

from config import logger
from dataclass import FilmWork, Person, Genre


class DataTransform:
    """Преобразование данных для загрузки в Elasticsearch."""

    def __init__(self):
        self.storage = []

    def transform(self, data: Iterator[Tuple]) -> List[FilmWork]:
        for movie in data:
            fw_id, *data, pfw_role, p_id, p_full_name, g_id, g_name = movie

            filmwork = FilmWork(fw_id, *data)
            person = Person(p_id, p_full_name)
            genre = Genre(g_id, g_name)
            movie = self.check_movie_in_storage(filmwork)
            movie.add_person(person=person, role=pfw_role)
            movie.add_genre(genre=genre)

        logger.info(f'Подготовлено {len(self.storage)} записей'
                    f' для передачи в Elasticsearch')

        return self.storage

    def check_movie_in_storage(self, movie: FilmWork) -> FilmWork:
        if self.storage:
            for item in self.storage:
                if item.id == movie.id:
                    return item
        self.storage.append(movie)
        return movie
