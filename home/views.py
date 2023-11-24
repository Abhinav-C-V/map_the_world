from django.shortcuts import render
from . models import PackageGallery,Package
# Create your views here.

def home(request):
    package = Package.objects.all().order_by('id')
    package_imgs = PackageGallery.objects.all().order_by('id')
    context = {
        'package': package,
        'package_imgs': package_imgs
    }
    return render(request, 'index.html',context)