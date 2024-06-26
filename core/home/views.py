from django.shortcuts import render # type: ignore

from django.http import HttpResponse # type: ignore
# Create your views here.
def home(request):
    people=[
        {"name":"Govind","age":"22"},
         {"name":"rahil","age":"21"},
          {"name":"abhisheik","age":"55"},
           {"name":"mansi","age":"16"},
            {"name":"ritik","age":"11"},
    ]


    text = """
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Distinctio praesentium velit non vero accusamus amet debitis, facilis reiciendis dignissimos, consequatur, sequi porro dolore assumenda facere quo modi! Optio, consequatur explicabo.
      """
    return render(request,'index.html', context={"people":people  , "text": text, "page":"django 2024"})
    # return HttpResponse("<h1>hello this is http request from the django</h1>")


def success_page(request):
    return HttpResponse("working witht the routes")

def contact(request):
    context = {"page": "contact" }
    return render(request,'contact.html',context)

def about(request):
    context = {"page": "about" }
    return render(request,'about.html',context)
