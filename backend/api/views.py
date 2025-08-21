from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from pymongo import MongoClient

from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

client = MongoClient(settings.MONGO_URI)
mongo_db = client["exampledb"]
collection = mongo_db["mongo_items"]

@api_view(['GET', 'POST'])
def mongo_items(request):
    if request.method == 'POST':
        data = request.data
        collection.insert_one({'name': data.get('name', '')})
    items = [{'name': doc.get('name', '')} for doc in collection.find()]
    return Response(items)
