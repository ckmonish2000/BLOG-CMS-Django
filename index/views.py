from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import blog

# Create your views here.
class main(View):
    def post(self,request):
        if request.method=='POST':
            title=request.POST['title']
            body=request.POST['Body']
            link=request.POST['link']
            x=blog(title=title,body=body,imglink=link)
            print(x)
            x.save()  
            return render(request,"index.html")


    def get(self,request):
        return render(request,"index.html")
    

class posts(View):
    def get(self,request):
        x=blog.objects.all()
        context={"stuff":x}
        return render(request,"posts.html",context)

class views(View):
    def get(self,request,tit):
        x=blog.objects.get(title=tit)
        context={"stuff":x}
        return render(request,"view.html",context)





