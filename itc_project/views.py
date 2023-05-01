from django.shortcuts import HttpResponse,render

def home_view(request):
    return render(request,'home.html')