from django.shortcuts import render
from . import models


def IndexView(request):
    region = models.Regions.objects.get(id=71)
    universities = region.universities.all()
    return render(request, "main/index.html", context={"universities": universities})
