from django.contrib import admin
from .models import BotSettings, BotDictionary, TelegramUser, Subscription, Payment, RobokassaLogs


admin.site.register(TelegramUser)
admin.site.register(Payment)
admin.site.register(RobokassaLogs)

@admin.register(BotSettings)
class BotSettingsAdmin(admin.ModelAdmin):
    pass


@admin.register(BotDictionary)
class BotDictionaryAdmin(admin.ModelAdmin):
    pass

class BotUsersInline(admin.TabularInline):
    extra = 0
    model = TelegramUser

    def has_add_permission(self, *args, **kwargs) -> bool:
        return False

    def has_change_permission(self, *args, **kwargs) -> bool:
        return False
    
@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    inlines = [BotUsersInline]

# @admin.register(BotMenu)
# class BotMenuAdmin(admin.ModelAdmin):
#     inlines = [BotButtonsInline]