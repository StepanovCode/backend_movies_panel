import uuid
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Genre:
    """Структура данных жанра для отправки в Elasticsearch."""

    id: uuid.UUID
    name: str


@dataclass
class Person:
    """Структура данных персоны для отправки в Elasticsearch."""

    id: uuid.UUID
    name: str


@dataclass
class FilmWork:
    """Структура данных Фильма для отправки в Elasticsearch."""

    id: uuid.UUID
    title: str
    description: str
    imdb_rating: float
    actors: Optional[List[Person]] = field(default_factory=list)
    writers: Optional[List[Person]] = field(default_factory=list)
    actors_names: Optional[List[str]] = field(default_factory=list)
    director: Optional[List[str]] = field(default_factory=list)
    writers_names: Optional[List[str]] = field(default_factory=list)
    genre: Optional[List[uuid.UUID]] = field(default_factory=list)

    def add_person(self, person: Person, role: str):
        if role == 'actor':
            if person not in self.actors:
                self.actors.append(person)
                self.actors_names.append(person.name)
        if role == 'director':
            if person.name not in self.director:
                if person.name is None:
                    person.name = ''
                self.director.append(person.name)
        if role == 'writer':
            if person not in self.writers:
                self.writers.append(person)
                self.writers_names.append(person.name)

    def add_genre(self, genre: Genre):
        if genre not in self.genre:
            self.genre.append(genre.id)
