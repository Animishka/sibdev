from django.urls import path, include
from rest_framework import routers
from . import views
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register('dealscsv', views.DealsCsvView)  # загрузка файла, POST-запрос
router.register('get_top', views.GetTopView)  # получение данных из БД, GET-запрос

urlpatterns = [
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)