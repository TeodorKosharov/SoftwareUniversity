from django.shortcuts import render
from rest_framework import serializers, status
from django_rest_framework.api.models import Book, Item
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_rest_framework.api.serializers import ItemSerializer
from django.views.generic import ListView



# Response - този клас приема python данни и ги превръща в json
# many=True това указва че ще сериализираме повече от един елемент, а ако е един пишем many=False

@api_view(['GET'])
def get_data(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class ListBooksView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({'books': serializer.data})

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


##################################################

@api_view(['GET'])
def get_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


def demo_view(request):
    return render(request, 'demo.html')
