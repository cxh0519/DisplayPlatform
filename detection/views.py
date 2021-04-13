from django.shortcuts import render
from .models import DetectionImage
from uuid import uuid4
from django.core.files.base import ContentFile
from PIL import Image
import models


def index(request):
    return render(request, 'detection/index.html')


def upload_image_and_detection(request):
    try:
        content = ContentFile(request.FILES['image'].read())
        Image.open(content)
    except Exception:
        return render(request, 'detection/result.html', {'status': 'failure'})
    unicode = str(uuid4())
    image = DetectionImage(unicode=unicode)
    image.image.save(unicode+'.'+request.FILES['image'].name.split('.')[-1], content)
    ###############################    # call your model here with image, process the output as string and store in value 'result'
    result = 'empty for now'
    ###############################
    return render(request, 'detection/result.html', {'status': 'success', 'image': image, 'result': result})

