from django.shortcuts import render
from .models import ReidImage
from uuid import uuid4
from django.core.files.base import ContentFile
from PIL import Image
import models


def index(request):
    return render(request, 'reid/index.html')


def upload_image_and_reid(request):
    try:
        content = ContentFile(request.FILES['image'].read())
        Image.open(content)
    except Exception:
        return render(request, 'reid/result.html', {'status': 'failure'})
    unicode = str(uuid4())
    image = ReidImage(unicode=unicode)
    image.image.save(unicode+'.'+request.FILES['image'].name.split('.')[-1], content)
    result = 'result'
    return render(request, 'reid/result.html', {'status': 'success', 'image': image, 'result': result})

