from django.db import models
from applications.departamento.models import Departamento
# Create your models here.


class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades empleados'
    
    def __str__(self) -> str:
        return str(self.id ) + self.habilidad 

class Empleado(models.Model):
    """_summary_ Modelo de cada empleado

    Args:
        models (_type_): _description_
    """
    JOB_CHOICES = (
        ('0','Contador'),
        ('1','Administrador'),
        ('2','Economista'),
        ('3','otro'),
    )
    fist_name = models.CharField("Nombres", max_length=60)
    last_name = models.CharField("Apellidos", max_length=60)
    job = models.CharField("Trabajo",choices=JOB_CHOICES, max_length=1)
    departamento = models.ForeignKey(Departamento,  on_delete=models.CASCADE)
    habilidades= models.ManyToManyField(Habilidades)
    #image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self) -> str:
        return str(self.id ) + self.fist_name + self.last_name