import uuid
from django.db import models


class FundoImobiliario(models.Model):

    SETOR_CHOICES = [
        ('hospital', 'Hospital'), ('hotel', 'Hotel'), ('hibrido', 'Híbrido'),
        ('lajes_corporativas', 'Lajes Corporativas'),
        ('logistica', 'Logística'), ('outros', 'Outros'),
        ('residencial', 'Residencial'),
        ('titulos_valores_mobiliarios', 'Títulos e Val. Mob.')
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        null=False,
        blank=False
    )

    codigo = models.CharField(
        null=False,
        blank=False,
        max_length=8
    )

    setor = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices=SETOR_CHOICES
    )

    dividend_yield_medio_12m = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False,
    )

    vacancia_financeira = models.DecimalField(
        null=False,
        blank=False,
        max_digits=5,
        decimal_places=2
    )

    vacancia_fisica = models.DecimalField(
        null=False,
        blank=False,
        max_digits=5,
        decimal_places=2
    )

    quantidade_ativos = models.IntegerField(
        null=False,
        blank=False,
        default=0
    )
