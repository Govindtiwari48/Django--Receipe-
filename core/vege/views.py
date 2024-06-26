from django.shortcuts import render, redirect # type: ignore
from .models import *

# Create your views here.
def recepies(request):
    if request.method == "POST":

        data = request.POST
        receipe_image = request.FILES.get("receipe_image")
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        print(receipe_description)
        print(receipe_name)
        print(receipe_image)


        Receipe.objects.create(
            receipe_image = receipe_image,
            receipe_name  = receipe_name,
            receipe_description =  receipe_description
            )
        return redirect("/receipes/")


    return render(request,"receipes.html")