from enum import unique
from tabnanny import verbose
from django.db import models

class KategoriModel(models.Model):
    isim = models.CharField(max_length=30,blank=False,null=False)
   
    class Meta:
        db_table="kategori"
        verbose_name_plural="Kategoriler"
        verbose_name="Kategori"
    def __str__(self):
        return self.isim