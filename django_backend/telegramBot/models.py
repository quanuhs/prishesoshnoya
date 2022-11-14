from django.db import models

class BotSettings(models.Model):
    """Модель настройки Telegram бота"""

    token = models.CharField(max_length=128, verbose_name="Токен бота")
    webhook_secret = models.CharField(max_length=128, verbose_name="Код webhook")

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
    btn_politics = models.CharField(max_length=125, verbose_name="Кнопка - политика о персональных данных")
     
    text_pay = models.TextField(verbose_name="Текст - оплата")
    btn_pay = models.CharField(max_length=125, verbose_name="Кнопка - оплатить")

    text_after_pay = models.TextField(verbose_name="Текст - после оплаты")
    text_bunt = models.TextField(verbose_name="Текст - про БУНТ")
    
    btn_bunt_channel = models.CharField(max_length=125, verbose_name="Кнопка - канал")
    

    # Основные кнопки
    btn_back = models.CharField(max_length=125, verbose_name="Кнопка - назад")
    btn_menu = models.CharField(max_length=125, verbose_name="В главное меню")
