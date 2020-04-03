from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .handle import handle_uploaded_file
from .models import blog
from .forms import mainform

# Create your views here.
class main(View):
    def post(self,request):
        if request.method=='POST':
            print(request.POST)
            title=request.POST['title']
            body=request.POST['body']
            link=request.POST['link']
            a=handle_uploaded_file(request.FILES['file'])
            x=blog(title=title,body=body,imglink=link,filepath=a)
            print(x)
            x.save()
            context={"stuff":mainform()}
            return render(request,"index.html",context)
           


    def get(self,request):
        context={"stuff":mainform()}
        return render(request,"index.html",context)
    

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





