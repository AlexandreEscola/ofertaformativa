from django.db import models

class OfertaFormativa(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    saidas_profissionais = models.TextField()
    carga_horaria = models.IntegerField()
    disciplinas = models.TextField()
    imagem = models.ImageField(upload_to='ofertas/', blank=True, null=True)

    def __str__(self):
        return self.nome
