from rest_framework import serializers
from .models import *


class DealsCsvSerializer(serializers.HyperlinkedModelSerializer):
    """
    serializer для загрузки файла в базу данных и сохранения данных о сделках из файла
    """
    class Meta:
        model = DealsCsv
        fields = ('upload_file', 'upload_date')


class GetTopSerializer(serializers.HyperlinkedModelSerializer):
    """
    serializer для получения данных из БД GET запросом
    """
    class Meta:
        model = Customer
        fields = ('customer', 'total', 'items_set')