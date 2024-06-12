from django.contrib import admin

from core.models import Project, QuotationRequest

# Register your models here.
admin.site.register(Project)
admin.site.register(QuotationRequest)