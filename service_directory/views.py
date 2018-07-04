from django.shortcuts import render, HttpResponse

def home_page(request):
    return render(request, 'defaults/index.html')

def signup(request):

    return render(request, 'registration/registration.html')

def mediakit(request):
    return render(request, 'directories/media_kit.html')

def test(request):
    if request.method == "POST":
        return HttpResponse("http response works")
    return render(request, 'registration/test.html')