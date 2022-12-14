from django.db import models

# Create your models here.
# RESERVADO, COMPLETADA, ANULADA, NO ASISTEN

estado = [
    ('reservado','RESERVADO'),
    ('completada','COMPLETADA'),
    ('anulada','ANULADA'),
    ('no asisten','NO ASISTEN')
]
personas = [
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,7),
    (8,8),
    (9,9),
    (10,10),
    (11,11),
    (12,12),
    (13,13),
    (14,14),
    (15,15)
]

class Inscripcion(models.Model):
    rut                 = models.CharField(max_length=12)  
    nombre              = models.CharField(max_length = 70)
    telefono            = models.IntegerField()
    fecha_inscripcion   = models.DateField()
    hora                = models.TimeField()
    institucion          = models.CharField(max_length = 70)
    estado_reserva      = models.CharField(max_length = 70,choices = estado)
    observacion         = models.TextField(blank=True)