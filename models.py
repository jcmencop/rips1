#from django.db import models
from django.db import models
from django.utils import timezone


class Post(models.Model): #define modelo (es un objeto). class indoca que lo estamos definiendo, post es el nombre (letra inicial mayuscula)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #models.Model indica a django que es un modleo y debe guardarlo en la base de datos
    title = models.CharField(max_length=200) #el titulo es caracter de max 200 de largo
    text = models.TextField()                #texto sin limites
    created_date = models.DateTimeField(
            default=timezone.now)            #fecha creacion, x defecto de la fecha de ahora importada arriba
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):      #self indica que es un metodo y el nombre es publish
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #se obtiene el resultado qeu devuelve el metodo en este caso 
        return self.title

# Create your models here.
