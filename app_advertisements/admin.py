from django.contrib import admin
from .models import Advertisements

class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ['id','description', 'price','created_date','updated_date','auction','get_html_image']
    list_filter = ['auction','created_at']
    #pass - пропуск

admin.site.register(Advertisements, AdvertisementsAdmin)


# Register your models here.
