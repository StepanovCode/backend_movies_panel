from django.contrib import admin

from .models import Genre, Filmwork, GenreFilmwork,\
    Person, PersonFilmwork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    search_fields = ('full_name',)


class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmwork
    autocomplete_fields = ('genre',)


class PersonFilmworkinline(admin.TabularInline):
    model = PersonFilmwork
    autocomplete_fields = ('person',)


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = [
        GenreFilmworkInline,
        PersonFilmworkinline,
    ]
    list_display = ('title', 'type', 'creation_date',
                    'rating', 'created', 'modified',
                    )
    list_filter = ('type',)
    search_fields = ('title', 'description',
                     'creation_date', 'rating',
                     )
