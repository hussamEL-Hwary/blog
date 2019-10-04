# My_Blog

## Table of content
- [Introduction](#introduction)
- [Features](#Features)
- [Installation](#Installation)
- [Routes](#Routes)
- [file-structure](#file-structure)
- [screen-shots](#screen-shots)

## Introduction
  A simple blog shows posts in different categories, users can log in with Github and Facebook to comment 
  on posts and any visitor can send me a message and viewing my portfolio.
  [https://hossam-hwary.herokuapp.com](https://hossam-hwary.herokuapp.com)
## Features
#### Built with [Django2](https://docs.djangoproject.com/en/2.2/releases/2.0/)
| Features  |
| :------------ |
| Viewing posts |
| Viewing posts in categories |
| send message |
| [ratelimit](https://django-ratelimit.readthedocs.io/en/stable/) message form |
| CSRF protection |
| [TinyMCE](https://django-tinymce.readthedocs.io/en/latest/) editor|
| dango_rest_framework for APIs endpoints |
| [Swagger](https://django-rest-swagger.readthedocs.io/en/latest/) to decument APIs |
| commenting on posts |
| Github login |
| Facebook login |
| Viewing portfolio |
| Deployed to [Heroku](https://dashboard.heroku.com/) |


## Installation
#### preequisits
- install [python3](https://www.python.org/download/releases/3.0/) 
- install [pip](https://itsfoss.com/install-pip-ubuntu/)
- Create [GitHub](https://github.com/settings/developers) and [Facebook](https://developers.facebook.com/) OAuth apps
- In ```settins.py``` replace key and secret with your app credentials
``` python
SOCIAL_AUTH_GITHUB_KEY = '###########'
SOCIAL_AUTH_GITHUB_SECRET = '#################'

SOCIAL_AUTH_FACEBOOK_KEY = '###################'
SOCIAL_AUTH_FACEBOOK_SECRET = '########################'

```

- Open terminal in the project direcory and install all required packages
   ```shell
   pip3 install -r requirements.txt
   ```
- Migrate database
  ```shell
  python3 manage.py makemigrations

  python3 manage.py migrate
  ```
- Create superuser
  ```shell
  python3 manage.py createsuperuser
  ```
- Run the app
  ```shell
  python3 manage.py runserver
  ```
Great! Now hit the project url :)


## Routes
- ```/```
- ```post/<post_slug>```
- ```category/<slug>```
- ```contact-me/```
- ```login/```
- ```about-me/```
- ```post/JSON/```
- ```post/<slug>/JSON/```
- ```category/JSON/```
- ```category/<slug>/JSON/```
- ```docs/```
- ```logout/```

## file-structure
```shell
.
├── blog
│   ├── admin.py
│   ├── APIviews.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_tutorial.py
│   │   ├── 0003_tutorial_min_read.py
│   │   ├── 0004_category_category_slug.py
│   │   ├── 0005_message.py
│   │   ├── 0006_auto_20190906_1322.py
│   │   ├── 0007_comment.py
│   │   ├── 0008_comment_user.py
│   │   ├── 0009_tutorial_comments.py
│   │   ├── 0010_tutorial_img_url.py
│   │   ├── 0012_message_created_at.py
│   │   ├── 0014_tutorial_slug.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-36.pyc
│   │       ├── 0002_tutorial.cpython-36.pyc
│   │       ├── 0003_tutorial_min_read.cpython-36.pyc
│   │       ├── 0004_category_category_slug.cpython-36.pyc
│   │       ├── 0005_message.cpython-36.pyc
│   │       ├── 0006_auto_20190906_1322.cpython-36.pyc
│   │       ├── 0007_comment.cpython-36.pyc
│   │       ├── 0008_comment_user.cpython-36.pyc
│   │       ├── 0009_tutorial_comments.cpython-36.pyc
│   │       ├── 0010_tutorial_img_url.cpython-36.pyc
│   │       ├── 0012_message_created_at.cpython-36.pyc
│   │       ├── 0014_tutorial_slug.cpython-36.pyc
│   │       └── __init__.cpython-36.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-36.pyc
│   │   ├── APIviews.cpython-36.pyc
│   │   ├── apps.cpython-36.pyc
│   │   ├── forms.cpython-36.pyc
│   │   ├── __init__.cpython-36.pyc
│   │   ├── models.cpython-36.pyc
│   │   ├── serializers.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── views.cpython-36.pyc
│   ├── serializers.py
│   ├── static
│   │   ├── css
│   │   │   ├── bootstrap-social.css
│   │   │   ├── github-activity.css
│   │   │   ├── index.css
│   │   │   ├── octicons.eot
│   │   │   ├── octicons.min.css
│   │   │   ├── octicons.svg
│   │   │   ├── octicons.ttf
│   │   │   └── octicons.woff
│   │   ├── imgs
│   │   │   ├── a.png
│   │   │   ├── avatar.jpg
│   │   │   ├── blog-post-thumb-3.jpg
│   │   │   ├── httprouter.png
│   │   │   ├── Intro.jpg
│   │   │   ├── trie.jpg
│   │   │   ├── trie.png
│   │   │   └── user.png
│   │   └── js
│   │       └── github-activity.js
│   ├── templates
│   │   ├── 404.html
│   │   ├── categories_block.html
│   │   ├── category_posts.html
│   │   ├── contact_me.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── post_card.html
│   │   ├── post.html
│   │   └── who_am_i.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── settings.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── wsgi.cpython-36.pyc
│   ├── settings.py
│   ├── templates
│   │   └── base.html
│   ├── urls.py
│   └── wsgi.py
├── Procfile
├── README.md
├── requirements.txt
└── runtime.txt

```

## screen-shots
### Homepage
![home](/screenshots/home.png)



### About me
![about-me](/screenshots/about-me.png)



### Message Me
![message](/screenshots/message.png)



### API docs
![api-docs](/screenshots/api-docs.png)
