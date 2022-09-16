from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Attorney(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    full_name = models.CharField(
        max_length=100,
        default='Ф.И.О.'
    )
    test1 = models.TextField(
        null=True,
        unique=True
    )

    def __str__(self):
        return self.full_name


class Client(models.Model):
    full_name = models.CharField(
        max_length=100,
        default='Ф.И.О. или наименование')
    test = models.ForeignKey(
        Attorney,
        to_field='test1',
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.full_name


class Contract(models.Model):
    name = models.ForeignKey(
        Attorney,
        on_delete=models.CASCADE,
        related_name='contracts'
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='contracts'
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    description = models.TextField(
        default='пусто'
    )

    def __str__(self):
        return f'Соглашение № e-{str(self.pk)}'
