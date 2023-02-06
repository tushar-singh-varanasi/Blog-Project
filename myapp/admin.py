from django.contrib import admin
from .models import Contact,Business,Politics


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['id','Name','Email','Message']

@admin.register(Business)
class BusnessAdmin(admin.ModelAdmin):
    list_display=['id','title','content','date','image']

@admin.register(Politics)
class PoliticsAdmin(admin.ModelAdmin):
    list_display=['id','title','content','date','image']
    




    