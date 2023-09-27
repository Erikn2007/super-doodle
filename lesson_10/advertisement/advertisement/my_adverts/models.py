from django.db import models
from django.forms import ModelForm
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.html import format_html
from django.conf.urls.static import static
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
User = get_user_model()
# {type} + Field -> нейминг типов джанго моделей
#  Модель объявления
class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="my_adverts", blank=True, null=True)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.SmallIntegerField("Категория")
    author = models.CharField("Автор", max_length=20)
    location = models.CharField("Локация товара", max_length=255)
    auction = models.BooleanField("Торг", help_text="Отметьте, если торг уместен")
    user = models.ForeignKey(User, verbose_name="Автор", on_delete = models.CASCADE)

    def __str__(self):
        return f'Advertisement(title={self.title}, price={self.price})'
    @admin.display(description="Дата создания")
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.strftime("%H:%M.%S")
            return format_html('<span style="color: teal; font-weight: bold"> Сегодня в {}</span>', created_time)
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

    def image_img(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return 'Нет изображения'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True




