from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Esto es la página de inicio")

def home(request):
    return HttpResponse("Esto es la página de /home")