from django.db import models

class BotSettings(models.Model):
    """Модель настройки Telegram бота"""

    token = models.CharField(max_length=128, verbose_name="Токен бота")
    webhook_secret = models.CharField(max_length=128, verbose_name="Код webhook")


    subscription_channel_url = models.TextField(verbose_name="Ссылка на канал с подпиской")
    free_channel_url = models.TextField(verbose_name="Ссылка на общий канал")

    contact_us = models.TextField(verbose_name="Ссылка для связи (связаться с нами)")


    # Оферта
    offerta = models.FileField(upload_to='static/file', blank=True, null=True, verbose_name='Оферта')
   
    # Политика персональных данных
    policy = models.FileField(upload_to='static/file', blank=True, null=True, verbose_name='Политика персональных данных')


    # ID магазина из ЛК Robokassa
    id_shop = models.TextField(default='test', verbose_name='ID магазина из ЛК Robokassa')
    
    # Пароль 1
    password_shop_1 = models.TextField(default='test', verbose_name='Пароль 1')
    
    # Пароль 2
    password_shop_2 = models.TextField(default='test', verbose_name='Пароль 2')


    def __str__(self):
        return f"{self.webhook_secret}"

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"



class BotDictionary(models.Model):
    """Модель словаря Telegram бота"""

    text_start = models.TextField(verbose_name="Текст - Главное меню")
    btn_process = models.CharField(max_length=125, verbose_name="Кнопка - про 'причеши процессы'")
    btn_bunt = models.CharField(max_length=125, verbose_name="Кнопка - про БУНТ")
    btn_prichess = models.CharField(max_length=125, verbose_name="Кнопка - про Причесошную")

    text_about = models.TextField(verbose_name="Текст - 'причеши процессы'")
    btn_price = models.CharField(max_length=125, verbose_name="Кнопка - цена вопроса")
    btn_contact = models.CharField(max_length=125, verbose_name="Кнопка - связаться с нами")
    btn_free = models.CharField(max_length=125, verbose_name="Кнопка - бесплатный доступ")

    text_price = models.TextField(verbose_name="Текст - цена вопроса")
    btn_subscribe = models.CharField(max_length=125, verbose_name="Кнопка - подписаться")
    btn_offerta = models.CharField(max_length=125, verbose_name="Кнопка - договор оферты")
    btn_policy = models.CharField(max_length=125, verbose_name="Кнопка - политика о персональных данных")
     
    text_pay = models.TextField(verbose_name="Текст - оплата")
    btn_pay = models.CharField(max_length=125, verbose_name="Кнопка - оплатить")

    text_after_pay = models.TextField(verbose_name="Текст - после оплаты")
    text_bunt = models.TextField(verbose_name="Текст - про БУНТ")
    
    btn_bunt_channel = models.CharField(max_length=125, verbose_name="Кнопка - канал")
    

    # Основные кнопки
    btn_back = models.CharField(max_length=125, verbose_name="Кнопка - назад")
    btn_menu = models.CharField(max_length=125, verbose_name="В главное меню")

    def __str__(self):
        return f"Словарь"

    class Meta:
        verbose_name = "Словарь"
        verbose_name_plural = "Словари"



# Подписки
class Subscription(models.Model):
    # Название
    name = models.CharField(max_length=125, verbose_name='Название')
    # Цена
    price = models.FloatField(default=0, verbose_name='Цена')
    # Активность
    active = models.BooleanField(default=True, verbose_name='Активно')
    # Описание при оплате
    description = models.TextField(default='Описание', verbose_name='Описание при оплате')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Настройки подписки"
        verbose_name_plural = "Настройки подписок"

# Логи робокассы
class RobokassaLogs(models.Model):
    text = models.TextField(verbose_name='Содержание')
    date = models.DateTimeField(auto_now=True, verbose_name='Дата')


# Пользователи
class TelegramUser(models.Model):
    # id
    user_id = models.TextField(verbose_name='id пользователя')
    
    # Текущая подписка
    subscription = models.ForeignKey(Subscription, on_delete=models.RESTRICT, default=None, blank=True, null=True)
   
    # Дата начала подписки
    date_sub = models.DateTimeField(blank=True, null=True, verbose_name='Дата начала подписки')
    
    # Материнский платеж
    previous_invoice_id = models.IntegerField(blank=True, null=True, verbose_name='Материнский платеж')
    
    # Автопродление подписки
    auto_payment = models.BooleanField(default=True, verbose_name='Автоматическая оплата')

    # Отправляем сообщение
    # Отправить пользователю сообщение
    
    def __str__(self):
        return f"{self.user_id}"

    class Meta:
        verbose_name = "Пользователь бота"
        verbose_name_plural = "Пользователи бота"


# Квитация оплаты
class Payment(models.Model):
    # Дата создания
    date = models.DateTimeField(auto_now_add=True)
    # Подписка
    subscription = models.ForeignKey(Subscription, on_delete=models.RESTRICT)
    # Пользователь
    user = models.ForeignKey(TelegramUser, on_delete=models.RESTRICT)
    # Номер счета
    invoice_number = models.IntegerField()
    # Статус
    status = models.BooleanField(default=False)
    # Материнский платеж (для автооплаты = True)
    maternity_payment = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.date} {self.invoice_number} {self.subscription} {self.user}'

    class Meta:
        verbose_name = "Квитантция на оплату"
        verbose_name_plural = "Квитантции на оплату"
