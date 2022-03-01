from django.contrib import admin

# Register your models here.

from post_images.models import image_attachment, item

admin.site.register(image_attachment)
admin.site.register(item)