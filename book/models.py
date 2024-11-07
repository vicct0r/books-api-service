from django.db import models
from stdimage import StdImageField


class Livro(models.Model):
    nome = models.CharField(max_length=60)
    pdf = models.FileField(upload_to='books/files/')
    img = StdImageField(upload_to='books/images/')

    def __str__(self):
        return self.nome