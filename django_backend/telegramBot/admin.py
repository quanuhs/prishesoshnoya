from django.contrib import admin
from .models import BotSettings, BotDictionary, TelegramUser, Subscription, Payment, RobokassaLogs


admin.site.register(TelegramUser)
admin.site.register(Subscription)
admin.site.register(Payment)
admin.site.register(RobokassaLogs)

@admin.register(BotSettings)
class BotSettingsAdmin(admin.ModelAdmin):
    pass


@admin.register(BotDictionary)
class BotDictionaryAdmin(admin.ModelAdmin):
    pass

# class BotButtonsInline(admin.TabularInline):
#     fk_name = 'origin_menu'
#     extra = 0
#     model = BotButton


# @admin.register(BotMenu)
# class BotMenuAdmin(admin.ModelAdmin):
#     inlines = [BotButtonsInline]