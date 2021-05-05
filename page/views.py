from rest_framework.response import Response
from page.models import Bhav
from django.shortcuts import render
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from django.http import HttpResponse
from rest_framework.decorators import api_view, schema
from .models import Bhav
from .serializers import BhavSerializer
CACHE_TTL = getattr(settings,'CACHE_TTL',DEFAULT_TIMEOUT)

# Create your views here.

@api_view(['GET'])
def homePageView(request):
#     if cache.get(request):
#         bhav = cache.get(request)
#         serializer = BhavSerializer(bhav, many=True)
#     else:
#         bhav = Bhav.objects.all()
#         serializer = BhavSerializer(bhav, many=True)
#         cache.set(request,Response(serializer.data))
#     return Response(serializer.data)
    pass