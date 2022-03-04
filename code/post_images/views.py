from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import item, image_attachment

def index(request):
    items_with_images = item.objects.prefetch_related('images')
    context = {'items_with_images': items_with_images}
    return render(request, "index.html", context)

def image_redirect(request, id):
    image_obj = get_object_or_404(image_attachment, id=id)
    return redirect(image_obj.picture.url)