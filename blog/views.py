from django.shortcuts import render
from django.views.generic import ListView

from works.models import Work
from .models import Blog
from mainpage.models import Main
from about.models import About


# Create your views here.

class BlogPageView(ListView):
    model = Blog
    template_name = 'blog.html'


class HomePageView(ListView):
    model = Main
    template_name = 'home.html'


class WorksPageView(ListView):
    model = Work
    template_name = 'works.html'


class AboutPageView(ListView):
    model = About
    template_name = 'about.html'

