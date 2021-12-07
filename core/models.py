from django.db import models


class Entregadore(models.Model):
    nome = models.CharField(max_length=200)
    historia = models.CharField(max_length=200)
    imagem = models.ImageField()
    
    @property
    def imageURL(self):
        try:
            url = self.imagem.url
        except:
            url = ''
        return url
    
    def __str__(self):
        return self.nome
    
    
class Parceiro(models.Model):
    imagem = models.ImageField()
    
    @property
    def imageURL(self):
        try:
            url = self.imagem.url
        except:
            url = ''
        return url
        