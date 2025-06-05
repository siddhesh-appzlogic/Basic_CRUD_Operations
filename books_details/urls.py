from django.urls import path
from .views import For_createView, For_DeleteView, For_ReadView, For_UpdateView


urlpatterns = [
        path('books_details/create/',For_createView.as_view(), name ='book-create'),
        path('books_details/',For_ReadView.as_view(), name ='book-read'),
        path('books_details/<int:pk>/update/',For_UpdateView.as_view(), name = 'book-update'),
        path('books_details/<int:pk>/delete/',For_DeleteView.as_view(), name = 'book-delete'),
]

