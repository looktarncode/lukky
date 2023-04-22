from django.shortcuts import render

def Homepage(request):
    return render(request, 'tools/homepage.html')
# Create your views here.
