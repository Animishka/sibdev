from .models import *
import csv

from django.core.files.storage import FileSystemStorage


def save_customers_deals(serializer):
    """
    Функция, которая позволяет получить файл после сохранения его в базе данных и сохранить информацмю
    о сделках из файла в БД с помощью моделей Customer и CustomersItems.
    :param serializer:
    :return:
    """
    file = serializer.data['upload_file'].split('/')[-1]
    fs = FileSystemStorage()
    file_path = fs.url(file)
    f = open('uploaded_files' + file_path, 'r', encoding='utf8')
    reader = csv.reader(f)
    l = list(reader)  # преобразовали в список, чтобы пройтись циклом по индексам (1, len(l))
    for i in range(1, len(l)):
        total = int(l[i][2])
        quantity = int(l[i][3])

        if Customer.objects.filter(customer=l[i][0]):
            if not CustomersItems.objects.filter(
                    customer__customer=l[i][0],
                    items=l[i][1],
                    total_deal=total,
                    quantity=quantity,
                    date=l[i][4]):  # если такой сделки не было еще сохранено, сохраняем новую
                customer = Customer.objects.filter(customer=l[i][0])[0]
                total_now = customer.total + total
                items = customer.items_set
                if l[i][1] not in items:  # проверка списка драг.камней, если нет, то добавить
                    items_now = f'{l[i][1]}, {items}'
                else:
                    items_now = items
                Customer.objects.filter(customer=l[i][0]).update(total=total_now, items_set=items_now)

                CustomersItems.objects.create(customer=customer, items=l[i][1], total_deal=total, quantity=quantity,
                                              date=l[i][4])

        else:  # если в БД нет customer, то сохраняем нового customer и новую сделку
            customer = Customer.objects.create(customer=l[i][0], total=total, items_set=l[i][1])
            CustomersItems.objects.create(customer=customer, items=l[i][1], total_deal=total, quantity=quantity, date=l[i][4])
    f.close()

