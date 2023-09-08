from django.db import models
from django.contrib import admin
# Create your models here.
# унаслед. класс models.Model
#  Придумать 6-7 полей для этой сущности
# title -> Заголовок
# description -> описание
# price -> цена
# creation_date -> дата создания
# category -> категория
# author -> автор
# location -> город
# auction -> торг (булево значение)

# {type} + Field -> нейминг типов джанго моделей
#  Модель объявления
class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.SmallIntegerField("Категория")
    author = models.CharField("Автор", max_length=20)
    location = models.CharField("Локация товара", max_length=255)
    auction = models.BooleanField("Торг", help_text="Отметьте, если торг уместен")

    def __str__(self):
        return f'Advertisement(title={self.title}, price={self.price})'
    @admin.display(description="Дата создания")
    def created_date(self):
        from django.utils import timezone
        if self.created_at == timezone.now().date():
            create_time = self.created_at.strftime("%H:%M.%S")
            return form_html("""
            <span>Сегодня в {}</span>
            """, create_time)
        return self.created_at.strftime('%d.%m.%Y в %H:%M.%S')

    @admin.display(description="Дата обновления")
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at == timezone.now().date():
            update_time = self.updated_at.strftime("%H:%M.%S")
            return form_html("""
               <span>Сегодня в {}</span>
               """, update_time)
        return self.updated_at.strftime('%d.%m.%Y в %H:%M.%S')
    class Meta:
        verbose_name = 'Объявления'
        verbose_name_plural = 'Объявления'