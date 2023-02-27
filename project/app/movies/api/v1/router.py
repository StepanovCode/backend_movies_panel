from rest_framework.routers import DefaultRouter

from movies.api.v1.views.movies import MoviesViewSet

router = DefaultRouter()
router.register(r'api/v1/movies', MoviesViewSet, basename='movies')
