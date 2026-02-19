from django.shortcuts import render

def index(request):
    # You can pass data into the template using the context dict if you want later.
    return render(request, "index_hello.html")

def about(request):
    # We'll show your name in the template instead of raw HttpResponse
    return render(request, "about_hello.html", {"name": "Sebastian Caniglia"})
