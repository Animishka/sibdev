from django.db import models


class Customer(models.Model):
    """
    Модель для сохранения данных о клиентах.
    поле total - каждая новая сделка обновляет значение поля на сумму сделки
    поле items_set - список драгоценных камней, по которым была сделка. Драгоценные камни не повторяются,
    наименование камней чувствительно к регистру.
    """
    customer = models.CharField(max_length=200, blank=False, unique=True)
    total = models.IntegerField()
    items_set = models.TextField()

    def __str__(self):
        return self.customer


class CustomersItems(models.Model):
    """
    Модель для сохранения сделок. Сделки проверяются на уникальность, учитывая все поля.
    поле customer связано отношением многие к одному или Foreign Key с моделью Customer.
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.CharField(max_length=100, blank=False)
    total_deal = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now=False, auto_now_add=False, auto_created=False)

    def __str__(self):
        return self.items


class DealsCsv(models.Model):
    """
    Модель для сохранения файлов при POST запросе. Если файл уже загружался, он также сохранится,
    но данные из него не повлияют на данные моделей Customer и CustomersItems.
    """
    upload_file = models.FileField(upload_to='uploaded_files', max_length=300, blank=False, null=False)
    upload_date = models.DateTimeField(auto_now_add=True, auto_now=False)