from django.db import models


# Create your models here.
class FilesUploaded(models.Model):
    nombre = models.CharField(max_length=255)
    tipo_mime = models.CharField(max_length=50)
    extencion = models.CharField(max_length=5)
    archivo = models.FileField()
    tamanno = models.DecimalField(max_digits=12, decimal_places=4)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nombre', 'extencion', ]

    def __str__(self):
        return '%s.%s' % (self.nombre, self.extencion)