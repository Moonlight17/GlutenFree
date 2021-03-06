import datetime
from django.utils import timezone
from django.contrib.postgres.fields import JSONField
from django.conf import settings
# from djoser.urls.base import User
from django.contrib.auth.models import User
from django.db import models



class Tag(models.Model):
	name = models.CharField(max_length = 40, default = None)

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name

		


class Profile(models.Model):
	# email = models.EmailField(max_length=254)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(verbose_name="Изображение профиля", upload_to='media', default='‎⁨media/default.png')
	quantity = models.IntegerField(verbose_name="Количество рецептов", default=0)

	def __str__(self):
		return self.user.username


# Create your models here.
class Recept(models.Model):
	title = models.CharField(max_length=200, default='Вкуснятина')
	comp = JSONField()
	text = JSONField()
	pub_date = models.DateTimeField(verbose_name="Дата и время публикации",auto_now=True)
	user = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
	tag_name = models.ManyToManyField(Tag)
	likes = models.IntegerField(default=0)

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

	def __str__(self):
		return self.title

class Gallery(models.Model):
    image = models.ImageField(upload_to='Recepts')
    recept = models.ForeignKey(Recept, on_delete=models.CASCADE, related_name='images')

# Create your models here.
class LikeRecept(models.Model):
	user = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
	recept = models.ForeignKey(Recept, verbose_name="Рецепт", on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.id)
	
	def __str__(self):
		return self.user.username + ' ' + self.recept.title


# Create your models here.
class Comment(models.Model):
	recept = models.ForeignKey(Recept, default= None, on_delete=models.CASCADE)
	text = models.CharField(max_length=200, default='Комментарий')
	pub_date = models.DateTimeField(verbose_name="Дата и время публикации", auto_now=True)
	user = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
	likes = models.IntegerField(default=0)

	def __str__(self):
		return self.text

# Create your models here.
class LikeComment(models.Model):
	user = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
	recept = models.ForeignKey(Recept, default= None, on_delete=models.CASCADE)
	comment = models.ForeignKey(Comment, default= None, on_delete=models.CASCADE)

	def __str__(self):
		return self.recept.title


