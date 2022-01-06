from django.db import models


class Entregadore(models.Model):
    nome = models.CharField(
        max_length=200,
        verbose_name='Nome'
    )
    imagem = models.ImageField(
        verbose_name='Sua foto'
    )
    cnh = models.ImageField(
        null=True, 
        blank=True,
        verbose_name='Imagem CNH'
    )
    doc_moto = models.FileField(
        null=True, 
        blank=True,
        verbose_name='Imagem documento da Moto'
    )
    
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
        