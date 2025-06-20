from django.db import models

# Create your models here.
class User(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=100)
     

    def __str__(self):
       return self.name
print(User)

class Confeccion(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    punzonado_width_lenght = models.IntegerField()
    punzonado_height_lenght = models.IntegerField()
    tejido_width_lenght = models.IntegerField()
    tejido_height_lenght = models.IntegerField()
    micrado_width_lenght = models.IntegerField()
    micrado_height_lenght = models.IntegerField()


    def __str__(self):
       return self.name
print(Confeccion)