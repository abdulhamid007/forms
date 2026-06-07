from django.db import models


class KursAriza(models.Model):
    toliq_ism = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    yosh = models.PositiveIntegerField()
    yonalish = models.CharField(max_length=20)
    tajriba_bor = models.BooleanField(default=False)
    qoshimcha = models.TextField(blank=True)
    yuborilgan_sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.toliq_ism