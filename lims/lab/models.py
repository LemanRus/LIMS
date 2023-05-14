from django.db import models

from core.models import CustomUser
from simple_history.models import HistoricalRecords


class Methodic(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    acts_from = models.DateField(blank=True, null=True, verbose_name='Введена в')
    acts_to = models.DateField(blank=True, null=True, verbose_name='Действительна до')
    used_reagents = models.ManyToManyField('Reagent', blank=True, related_name='methodics',
                                           verbose_name='Используемые реактивы')
    used_equipment = models.ManyToManyField('Equipment', blank=True, related_name='methodics',
                                            verbose_name='Используемое оборудование')

    history = HistoricalRecords()

    def __str__(self):
        return f'Методика "{self.name}"'

    class Meta:
        verbose_name = 'Методика'
        verbose_name_plural = 'Методики'


class Reagent(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    made_by = models.CharField(max_length=200, verbose_name='Изготовитель')
    made_date = models.DateField(blank=True, null=True, verbose_name='Дата производства')
    best_before = models.DateField(blank=True, null=True, verbose_name='Годен до')

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Реактив'
        verbose_name_plural = 'Реактивы'


class Equipment(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    last_cal = models.DateField(verbose_name='Дата последней калибровки (поверки)')
    next_cal = models.DateField(verbose_name='Дата следующей калибровки (поверки)')
    cal_organisation = models.CharField(max_length=200, verbose_name='Организация, проводящая калибровку (поверку)')

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'


class TechnicalMaintenance(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    type = models.CharField(choices=[('Плановое', 'Плановое'), ('Периодическое', 'Периодическое'),
                                     ('Внеплановое', 'Внеплановое')], max_length=60, verbose_name='Тип техобслуживания')
    next_date = models.DateField(verbose_name='Дата следующего техобслуживания')
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='maintenance',
                                  verbose_name='Относится к оборудованию')

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.name}, {self.type}'

    class Meta:
        verbose_name = 'Техническое обслуживание'
        verbose_name_plural = 'Техническое обслуживание'


class Contract(models.Model):
    number = models.CharField(max_length=200, verbose_name='Номер договора')
    contragent = models.CharField(max_length=200, verbose_name='С кем заключен договор')
    date_conclusion = models.DateField(verbose_name='Дата заключения')
    date_end = models.DateField(verbose_name='Дата окончания')
    file_contract = models.FileField(blank=True, null=True, verbose_name='Файл договора (скан)')

    history = HistoricalRecords()

    def __str__(self):
        return f'Договор {self.number} с «{self.contragent}»'

    @property
    def file_contract_url(self):
        if self.file_contract and hasattr(self.file_contract, 'url'):
            return self.file_contract.url

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'


class Protocol(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='protocols',
                               default=CustomUser.objects.first().pk, verbose_name='Автор')
    contract = models.ForeignKey('Contract', on_delete=models.CASCADE, related_name='protocols', verbose_name='К договору')
    number = models.CharField(max_length=200, verbose_name='Номер протокола')
    act_number = models.CharField(max_length=200, verbose_name='Номер акта')
    used_methodics = models.ManyToManyField(Methodic, related_name='protocols', verbose_name='Используемые методики')
    file_protocol = models.FileField(blank=True, null=True, verbose_name='Файл протокола')
    file_act = models.FileField(blank=True, null=True, verbose_name='Файл акта')
    close_date = models.DateTimeField(verbose_name='Дата закрытия')

    history = HistoricalRecords()

    def __str__(self):
        return f'Протокол {self.number}'

    @property
    def file_protocol_url(self):
        if self.file_protocol and hasattr(self.file_protocol, 'url'):
            return self.file_protocol.url

    @property
    def file_act_url(self):
        if self.file_act and hasattr(self.file_act, 'url'):
            return self.file_act.url

    class Meta:
        verbose_name = 'Протокол'
        verbose_name_plural = 'Протоколы'


class Bid(models.Model):
    contract = models.ForeignKey('Contract', on_delete=models.CASCADE, related_name='bids', verbose_name='К договору')
    number = models.CharField(max_length=200, verbose_name='Номер заявки')
    invoices = models.ManyToManyField('Invoice', related_name='bids', verbose_name='Счета')
    status = models.CharField(choices=[('c', 'Исполнена'), ('r', 'Отклонена'),
                                       ('p', 'Выполняется')], max_length=60, default='p', verbose_name='Статус')

    history = HistoricalRecords()

    def __str__(self):
        return f'Заявка {self.number} ({self.get_status_display()})'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Invoice(models.Model):
    number = models.CharField(max_length=200, verbose_name='Номер счёта')
    status = models.CharField(choices=[('p', 'Оплачен'), ('b', 'Задолженность'),
                                       ('w', 'В процессе')], max_length=60, default='w', verbose_name='Статус')

    history = HistoricalRecords()

    def __str__(self):
        return f'Счёт {self.number} ({self.get_status_display()})'

    class Meta:
        verbose_name = 'Счёт'
        verbose_name_plural = 'Счета'


def notebook_record_file_path(instance, filename):
    user_id = instance.id
    return f'user_files/user-{user_id}/{filename}'


class Record(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='records', verbose_name='Автор')
    text = models.TextField(max_length=5000, verbose_name='Текст записи')
    file = models.FileField(upload_to=notebook_record_file_path, blank=True, verbose_name='Приложенный файл')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    history = HistoricalRecords()

    @property
    def file_record_url(self):
        if self.file and hasattr(self.file, 'url'):
            return self.file.url
