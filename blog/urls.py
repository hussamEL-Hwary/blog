from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns=[
    path("", views.homepage, name="homepage"),
    path("post/<int:post_id>", views.blog_post, name="post"),
    path("category/<slug>", views.category_posts, name="category_posts"),
    path("contact-me/", views.visitor_message, name="message"),
]