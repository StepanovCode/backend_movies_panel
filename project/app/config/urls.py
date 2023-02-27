from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('movies.api.v1.urls'))
]


if settings.DEBUG:
    urlpatterns.extend(
        [
            path('schema/', SpectacularAPIView.as_view(), name='schema'),
            path(
                'schema/swagger/',
                SpectacularSwaggerView.as_view(url_name='schema'),
                name='swagger',
            ),
        ]
    )
