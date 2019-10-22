from django.contrib import admin
from .models import Profile,Image,Instagram,Comments

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('instagram')

# Register your models here.
admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Instagram)
admin.site.register(Comments)
