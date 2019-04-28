from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User
from .models import *



    
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class LikeReceptAdmin(admin.ModelAdmin):
    """Диалоги"""
    list_display = ("user", "recept")

admin.site.register(LikeRecept, LikeReceptAdmin)

# admin.site.register(Profile)
class ReceptInline(admin.TabularInline):
    fk_name = 'recept'
    model = Gallery


@admin.register(Recept)
class ReceptAdmin(admin.ModelAdmin):
    inlines = [ReceptInline,]

# admin.site.register(Recept)
admin.site.register(Comment)
admin.site.register(LikeComment)
admin.site.register(Tag)




# # Register your models here.
# class Profile(models.Model):

#     def __unicode__(self):
#         return self.username


# class Recept(models.Model):
   
#     def __str__(self):
#         return self.title


# # Create your models here.
# class Comments(models.Model):
    
#     def __str__(self):
#         return self.text

# # Create your models here.
# class Likes(models.Model):

#     def __unicode__(self):
#         return str(self.id)

# class Tag(models.Model):

#     def __str__(self):
#         return  self.name
