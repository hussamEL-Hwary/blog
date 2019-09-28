from django.urls import path, include
from . import views


app_name = 'blog'
urlpatterns=[
    path("", views.homepage, name="homepage"),
    path("post/<post_slug>", views.blog_post, name="post"),
    path("category/<slug>", views.category_posts, name="category_posts"),
    path("contact-me/", views.visitor_message, name="message"),
    path("login/", views.login, name="login"),
    path("about-me/", views.about_me, name="aboutme")
]
