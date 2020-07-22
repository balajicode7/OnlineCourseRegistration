from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request, 'index.html')


def login(request):
    return render(request, "admin_login.html")