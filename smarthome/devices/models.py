from django.db import models


class Environment(models.Model):
    name = models.CharField(max_length=100)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Ambiente'
        verbose_name_plural='Ambientes'

    def __str__(self) -> str:
        return f'{self.name}'


class Device(models.Model):
    name = models.CharField(max_length=50)
    update = models.DateTimeField(auto_now=True)

    environment = models.ForeignKey(Environment, on_delete=models.CASCADE, related_name='devices')


    class Meta:
        verbose_name='Dispositivo'
        verbose_name_plural='Dispositivos'

    def __str__(self) -> str:
        return f'{self.name}'