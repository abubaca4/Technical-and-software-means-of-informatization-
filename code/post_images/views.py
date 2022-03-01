from django.shortcuts import render

# Create your views here.

from .models import item

def index(request):
    items_with_images = item.objects.prefetch_related('images')
    context = {'items_with_images': items_with_images}
    return render(request, "index.html", context)