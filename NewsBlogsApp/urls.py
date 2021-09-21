from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='NewsBlogsApp'),
    # path("about", views.about, name='about'),
    path("blogs", views.blogs, name='blogs'),
    path("contact", views.contact, name='contact'),
]
