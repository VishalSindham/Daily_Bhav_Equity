from rest_framework import viewsets
from .models import Bhav
from .serializers import BhavSerializer

from rest_framework.response import Response
from page.models import Bhav
from django.shortcuts import render
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class BhavViewSet(viewsets.ModelViewSet):
    queryset = Bhav.objects.all()
    serializer_class = BhavSerializer

    @method_decorator(cache_page(60*150))
    def dispatch(self,*args,**kwargs):
        return super(BhavViewSet,self).dispatch(*args,**kwargs)