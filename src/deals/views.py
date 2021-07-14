from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import DealsCsvSerializer, GetTopSerializer

from .utils import save_customers_deals


class DealsCsvView(viewsets.ModelViewSet):
    """
    Загрузка файла со сделками в формате .csv
    """
    queryset = DealsCsv.objects.all()
    serializer_class = DealsCsvSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)  # сохранение файла в БД
        save_customers_deals(serializer)  # сохранение данных по сделкам в БД
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class GetTopView(viewsets.ReadOnlyModelViewSet):
    """
    Вывод первых пяти покупателей, отсортированных по общему объему покупок
    """
    queryset = Customer.objects.order_by('-total')[:5].values()
    serializer_class = GetTopSerializer
