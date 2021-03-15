from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('phadmin/', admin.site.urls),
    path('', include('apps.home.urls', namespace='home')),
    path('users/', include('apps.users.urls', namespace='users')),
    path('products/', include('apps.products.urls', namespace='products')),
    path('orders/', include('apps.orders.urls', namespace='orders')),
    path('api/', include('apps.users.api.urls', namespace='users_api')),
    path('api/', include('apps.products.api.urls', namespace='products_api')),
    path('api/', include('apps.home.api.urls', namespace='home_api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
