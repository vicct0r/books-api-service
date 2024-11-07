from django.urls import path
from .views import LivroAPIView, LivrosAPIView

urlpatterns = [
    path('books/', LivrosAPIView.as_view(), name='livros'),
    path('books/<int:pk>/', LivroAPIView.as_view(), name='livro')
]