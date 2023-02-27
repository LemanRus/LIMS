from django.db import models

from core.models import CustomUser


class Methodic(models.Model):
    name = models.CharField(max_length=200)
    acts_from = models.DateField(blank=True, null=True)
    acts_to = models.DateField(blank=True, null=True)
    used_reagents = models.ManyToManyField('Reagent', blank=True, related_name='methodics')
    used_equipment = models.ManyToManyField('Equipment', blank=True, related_name='methodics')

    def __str__(self):
        return f'Методика "{self.name}"'

    class Meta:
        verbose_name = 'Методика'
        verbose_name_plural = 'Методики'


class Reagent(models.Model):
    name = models.CharField(max_length=200)
    made_by = models.CharField(max_length=200)
    made_date = models.DateField(blank=True, null=True)
    best_before = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Реактив'
        verbose_name_plural = 'Реактивы'


class Equipment(models.Model):
    name = models.CharField(max_length=200)
    last_cal = models.DateField()
    next_cal = models.DateField()
    cal_organisation = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'


class TechnicalMaintenance(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(choices=[('Плановое', 'Плановое'), ('Периодическое', 'Периодическое'),
                                     ('Внеплановое', 'Внеплановое')], max_length=60)
    next_date = models.DateField()
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='maintenance')

    def __str__(self):
        return f'{self.name}, {self.type}'

    class Meta:
        verbose_name = 'Техническое обслуживание'
        verbose_name_plural = 'Техническое обслуживание'


class Contract(models.Model):
    number = models.CharField(max_length=200)
    contragent = models.CharField(max_length=200)
    date_conclusion = models.DateField()
    date_end = models.DateField()
    file_contract = models.FileField(blank=True, null=True)

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
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='protocols', default=CustomUser.objects.first().pk)
    contract = models.ForeignKey('Contract', on_delete=models.CASCADE, related_name='protocols')
    number = models.CharField(max_length=200)
    act_number = models.CharField(max_length=200)
    file_protocol = models.FileField(blank=True, null=True)
    file_act = models.FileField(blank=True, null=True)
    close_date = models.DateTimeField()

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
    contract = models.ForeignKey('Contract', on_delete=models.CASCADE, related_name='bids')
    number = models.CharField(max_length=200)
    invoices = models.ManyToManyField('Invoice', related_name='bids')
    status = models.CharField(choices=[('c', 'Исполнена'), ('r', 'Отклонена'),
                                     ('p', 'Выполняется')], max_length=60, default='p')

    def __str__(self):
        return f'Заявка {self.number} ({self.get_status_display()})'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Invoice(models.Model):
    number = models.CharField(max_length=200)
    status = models.CharField(choices=[('p', 'Оплачен'), ('b', 'Задолженность'),
                                       ('w', 'В процессе')], max_length=60, default='w')

    def __str__(self):
        return f'Счёт {self.number} ({self.get_status_display()})'

    class Meta:
        verbose_name = 'Счёт'
        verbose_name_plural = 'Счета'


def notebook_record_file_path(instance, filename):
    user_id = instance.id
    return f'user_files/user-{user_id}/{filename}'


class Record(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='records')
    text = models.TextField(max_length=5000)
    file = models.FileField(upload_to=notebook_record_file_path, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    @property
    def file_record_url(self):
        if self.file and hasattr(self.file, 'url'):
            return self.file.url
