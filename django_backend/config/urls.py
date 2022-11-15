from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import telegramBot.views as telegram_view

from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='admin/')),
    path('admin/', admin.site.urls),
    path('telegram/<secret_key>', telegram_view.handle_telegram),
    path('robokassa/result/', telegram_view.robokassa_result)
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
               static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#admin.site.site_header = ...
#admin.site.site_title =  ...
