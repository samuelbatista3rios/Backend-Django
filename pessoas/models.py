from django.db import models

class Pessoa(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    cpf = models.CharField(max_length=14, unique=True)
    altura = models.FloatField()
    peso = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.cpf})"

    def imc(self):
        if self.sexo == 'M':
            return (72.7 * self.altura) - 58
        else:
            return (62.1 * self.altura) - 44.7
