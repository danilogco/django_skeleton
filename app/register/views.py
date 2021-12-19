#from django.core import serializers
from django.http import JsonResponse

import json

def index(request):
    #response = serializers.serialize('json', model_inst)
    return JsonResponse({ 'message': 'Hello, World!' })
