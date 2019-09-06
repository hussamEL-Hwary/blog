from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Tutorial, Message
from .forms import MessageForm

# Create your views here.
# get latest 6 posts
# get all categories
def homepage(request):
    categories = Category.objects.all()
    latest_items = Tutorial.objects.all().order_by('-updated_at')[:6]
    context = {
        'latest_items': latest_items, 
        'categories': categories}
    return render(request, 'home.html',context=context)


# get post by id
def blog_post(request, post_id):
    categories = Category.objects.all()
    # TODO: raise an error when there is no post id
    tutorial = Tutorial.objects.get(pk=post_id)
    context = {'tutorial': tutorial, 
               'categories': categories}
    return render(request, 'post.html', context=context)
    

def category_posts(request, slug):
    category = Category.objects.get(category_slug=slug)
    related_tutorials = Tutorial.objects.filter(category=category).all()
    categories = Category.objects.all()
    tut_count = len(related_tutorials)
    context = {'related_tutorials': related_tutorials,
                'categories': categories,
                'category': category,
                'tut_count': tut_count}
    return render(request, 'category_posts.html', context=context)


def visitor_message(request):
    form = MessageForm()
    if request.method == 'POST':
        # save message
        form = MessageForm(request.POST)
        if form.is_valid():
            message = Message(
                author=form.cleaned_data["author"],
                email=form.cleaned_data["email"],
                body=form.cleaned_data["body"]
            )
            message.save()
            return redirect("blog:homepage")

    return render(request, 'contact_me.html', context={"form": form})