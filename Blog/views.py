from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView

# Create your views here.


class TestBootstrapView(ListView):

    template_name = "bootstrap_test.html"
