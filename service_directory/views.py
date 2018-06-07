from django.shortcuts import render, HttpResponse

def home_page(request):
    return HttpResponse("Welcome to our service directory")

def signup(request):

    return render(request, 'registration/registration.html')

def mediakit(request):
    return render(request, 'directories/media_kit.html')

def test(request):
    if request.method == "POST":
        return HttpResponse("http response works")
    return render(request, 'registration/test.html')