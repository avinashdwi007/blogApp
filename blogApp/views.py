from django.shortcuts import redirect, render

from blog.models import Post


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def portfolio(request):
    return render(request,'portfolio.html')
def newpost(request):
     if request.method == "POST":
        title=request.POST['title']
        content=request.POST['content']
        post=Post(title=title,content=content)
        post.save()
        return redirect('blog')
     else:
         return render(request,'newpost.html')
def blog(request):
   
    blogDetails=Post.objects.all()
    
    return render(request,'blog.html',{"blogDetails":blogDetails})