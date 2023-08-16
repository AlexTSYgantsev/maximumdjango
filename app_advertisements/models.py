from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.html import format_html

User = get_user_model()

class Advertisements(models.Model):
    title = models.CharField("Заголовок", max_length=128) # Короткое текстовое поле
    description = models.TextField('Описание') # Длинное текствое поле
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2) # Числовое поле
    auction = models.BooleanField("Торг", help_text="Отметьте, если торг уместен") # Булевое поле( True или False )
    created_at = models.DateTimeField(auto_now_add=True) # Поле времени
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='advertisements/')
    def __str__(self):
        return f"Advertisements(id={self.id}, title={self.title}, price={self.price})"

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S') # strftime - вывести время в нормальном формате
            return format_html(
                '<span style="color:green; font-weight: bold">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='Дата последнего обновления')
    def updated_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.created_at.date() == timezone.now().date():
            created_time = self.update_at.time().strftime('%H:%M:%S')  # strftime - вывести время в нормальном формате
            return format_html(
                '<span>Сегодня в {}</span>', created_time
            )
        return self.update_at.strftime('%d.%m.%Y в %H:%M:%S')
    @admin.display(description='фото')
    def get_html_image(self):
        if self.image:
            return format_html(
                '<img src="{url}" style="max-width: 80px; max-height: 80px;">', url=self.image.url
            )

class Meta:
    db_table = "advertisements"

# Create your models here.
