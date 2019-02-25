#from django.http import request
from django.shortcuts import render
from.forms import ContactForm

def home_page(request):
    context={
        "title":"hello world! title",
        "content":"welcome to the home page"
    }
    return render(request,"home_page.html" ,context)
def about_page(request):
    context={

        "title": "hello world! title aboutpage",
        "content": "welcome to the about page"
    }
    return render(request,"about_page.html",context)

def contact_page(request):
    contact_form=ContactForm()
    context={
        "title": "hello world! title contactpage",
        "content": "welcome to the contact page",
        "form": contact_form

    }
    if request.method=="post":
        print(request.POST)
        print(request.POST.GET('fullname'))
        print(request.post.get('email'))
        print(request.post.get('content'))
    return render(request,"contact/view.html",context)