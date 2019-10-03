from django.urls import path, include
from . import views
from . import APIviews
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="Swagger Docs")
app_name = 'blog'
urlpatterns=[
    path("", views.homepage, name="homepage"),
    path("post/<post_slug>", views.blog_post, name="post"),
    path("category/<slug>", views.category_posts, name="category_posts"),
    path("contact-me/", views.visitor_message, name="message"),
    path("login/", views.login, name="login"),
    path("about-me/", views.about_me, name="aboutme"),
    path("post/JSON/", APIviews.PostView.as_view(), name="posts_json"),
    path("post/<slug>/JSON/", APIviews.PostDetail.as_view(), name="post_detail"),
    path("category/JSON/", APIviews.CategoryView.as_view(), name="categories_json"),
    path("category/<slug>/JSON/", APIviews.CategoryPostsView.as_view(), name="category_posts_json"),
    path("docs/", schema_view, name="api_docs"),
]
