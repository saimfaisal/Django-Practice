from django.shortcuts import render

# Create your views here.
def all_saim(request):
    return render(request ,'saimapp/all_saim.html',{})
