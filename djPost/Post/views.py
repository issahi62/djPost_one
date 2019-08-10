from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Post, Author 
from .forms import PostModelForm, PostForm

def home(request):
    all_posts = Post.objects.all()
    context = { 
    'all_posts' : all_posts
    }
    return render(request, 'post_lists.html', context)


def detail_blog(request, slug):
	details = get_object_or_404(Post, slug=slug)
	context =  {
	'details': details  
	}
	return render(request, 'details.html', context)	

def create_blogform(request): 
    author, created = Author.objects.get_or_create(
        user = request.user, 
        email = request.user.email, 
        contact = '0245900924',
    )
    form = PostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid(): 
        form.instance.author = author 
        form.save()
        return redirect('/posts/') 
    context = {
        'form': form
    }
    return render(request, 'createform.html', context)
    
def createform(request):
    form_a = PostForm(request.POST or None, request.FILES or None)
    if form_a.is_valid():
        form_a.save()
        return redirect("/posts/")
        
    context  = { 
        'form_a':form_a
    }
    return render(request, 'create_view.html', context)

# CRUD create retrieve update and delete 

def post_update(request, slug): 
    unique_post = get_object_or_404(Post, slug=slug)
    form = PostModelForm(request.POST or None, request.FILES or None, instance=unique_post)
    if form.is_valid():
        form.save()
        return redirect("/posts/")

    context = {
        "form":form
    }
    return render(request, 'create_update.html', context)
  
        
def post_delete(request, slug): 
    unique_post = get_object_or_404(Post, slug=slug)
    unique_post.delete()
    return redirect("/posts/")
