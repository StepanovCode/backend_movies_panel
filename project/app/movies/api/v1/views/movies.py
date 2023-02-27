from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework import status

from movies.models import Filmwork
from movies.api.v1.serializers.movies import MoviesSerializer
from movies.pagination import CustomPagination


class MoviesViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Filmwork.objects.all().prefetch_related(
        'genres',
        'persons',
    )
    serializer_class = MoviesSerializer
    pagination_class = CustomPagination

    @extend_schema(
        responses={
            status.HTTP_200_OK: MoviesSerializer,
        },
    )
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    @extend_schema(
        responses={
            status.HTTP_200_OK: MoviesSerializer,
        },
    )
    def retrieve(self, request, *args, **kwargs):

        return super().retrieve(request, *args, **kwargs)
