from django.shortcuts import render
from rest_framework import generics
from .models import books_details
from .serializers import Bookserilizers

# Create your views here.

# class BookListCreate(generics.ListCreateAPIView):
#     queryset = books_details.objects.all()
#     serializer_class = Bookserilizers


# class BookRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = books_details.objects.all()
#     serializer_class = Bookserilizers

# for create 
class For_createView(generics.CreateAPIView):
    queryset = books_details.objects.all()
    serializer_class = Bookserilizers

# for Read(all books)
class For_ReadView(generics.ListAPIView):
    queryset = books_details.objects.all()
    serializer_class = Bookserilizers

# for Update
class For_UpdateView(generics.UpdateAPIView):
    queryset = books_details.objects.all()
    serializer_class = Bookserilizers
    lookup_field = 'pk'

# for Delete
class For_DeleteView(generics.DestroyAPIView):
    queryset = books_details.objects.all()
    serializer_class = Bookserilizers
    lookup_field = 'pk'

