from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 10000
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return Response({
            'next': self.page.next_page_number() if self.page.has_next() else None,
            'prev': self.page.previous_page_number() if self.page.has_previous() else None,
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })

    def get_paginated_response_schema(self, schema):
        return {
            'type': 'object',
            'properties': {
                'count': {
                    'type': 'integer',
                    'example': 1000,
                },
                'total_pages': {
                    'type': 'integer',
                    'example': 20,
                },
                'next': {
                    'type': 'integer',
                    'nullable': True,
                    'format': 'uri',
                    'example': 3
                },
                'prev': {
                    'type': 'integer',
                    'nullable': True,
                    'format': 'uri',
                    'example': 2
                },
                'results': schema,
            },
        }
