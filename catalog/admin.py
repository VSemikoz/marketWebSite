from django.contrib import admin
from .models import Producer, Electronic, ElectronicInstance, ElectronicType


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name']
    list_filter = ['company_name']


@admin.register(Electronic)
class ElectronicAdmin(admin.ModelAdmin):
    list_display = ['electronicName', 'picture', 'producer', 'electronicType']
    list_filter = ['electronicName', 'producer', 'electronicType']
    fields = [('electronicName', 'picture'), 'description', ('producer', 'electronicType')]


@admin.register(ElectronicInstance)
class ElectronicInstanceAdmin(admin.ModelAdmin):
    list_display = ['electronic']
    list_filter = ['electronic']


@admin.register(ElectronicType)
class ElectronicTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']






