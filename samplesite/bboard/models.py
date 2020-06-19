from django.db import models


class Bd(models.Model):
	title = models.CharField(max_length=50, verbose_name="Заголовок")
	content = models.TextField(null=True, blank=True, verbose_name="Тело статьи")
	price = models.FloatField(null=True, blank=True, verbose_name="Цена")
	published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')


	class Meta:
		verbose_name_plural = 'Объявления'
		verbose_name = 'Объявление'
		ordering = ['-published']




