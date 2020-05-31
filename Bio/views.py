from django.shortcuts import render

# Create your views here.




def explorer(request):
    return render(request,'Bio/index.html',dict())