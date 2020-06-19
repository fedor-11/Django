from django.shortcuts import render
from .models import Bd

def index(request):
    bbs = Bd.objects.all()
    return render(request, 'bboard/index.html', {"bbs":bbs})


