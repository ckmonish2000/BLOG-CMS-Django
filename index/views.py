from django.shortcuts import render
from django.http import JsonResponse
from .models import blog
# Create your views here.


def index(request):
    if request.method=='POST':
        title=request.POST['title']
        body=request.POST['Body']
        link=request.POST['link']
        x=blog(title=title,body=body,imglink=link)
        print(x)
        x.save()  
        return render(request,"index.html")
    return render(request,"index.html")



def post(request):
    x=blog.objects.all()
    context={"stuff":x}
    return render(request,"posts.html",context)

def view(request,tit):
    x=blog.objects.get(title=tit)
    context={"stuff":x}
    return render(request,"view.html",context)





