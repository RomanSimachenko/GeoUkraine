from django.shortcuts import render
from . import models


def IndexView(request):
    return render(request, "main/index.html", context={})
