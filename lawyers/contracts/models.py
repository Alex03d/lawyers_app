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

    def __str__(self):
        return self.full_name


class Client(models.Model):
    full_name = models.CharField(
        max_length=100,
        default='Ф.И.О. или наименование')

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
        related_name='contracts',
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    description = models.TextField()

    def __str__(self):
        return f'Соглашение № e-{str(self.pk)}'
