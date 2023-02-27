from rest_framework import serializers
from movies.models import Filmwork, Genre, Person, PersonFilmwork


class MoviesSerializer(serializers.ModelSerializer):
    """Данные фильма"""

    genres = serializers.SlugRelatedField(
        many=True,
        required=True,
        slug_field='name',
        queryset=Genre.objects.all()
    )
    actors = serializers.SlugRelatedField(
        many=True,
        required=True,
        source='persons',
        slug_field='full_name',
        queryset=Filmwork.persons.through.objects.filter(role='actor')
    )
    directors = serializers.SlugRelatedField(
        many=True,
        required=True,
        source='persons',
        slug_field='full_name',
        queryset=Filmwork.persons.through.objects.filter(role='director')
    )
    writers = serializers.SlugRelatedField(
        many=True,
        required=True,
        source='persons',
        slug_field='full_name',
        queryset=Filmwork.persons.through.objects.filter(role='writer')
    )

    class Meta:
        model = Filmwork
        fields = [
            'id',
            'title',
            'description',
            'creation_date',
            'rating',
            'type',
            'genres',
            'actors',
            'directors',
            'writers'
        ]
