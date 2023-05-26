from django.db import models
from ap.validators import file_size
# Create your models here.

class Aloqa(models.Model):
    name = models.CharField(max_length=150,blank=True,null=True)
    email = models.EmailField(max_length=150)
    number = models.CharField(max_length=150)
    msg = models.CharField(max_length=999)

    def __str__(self):
        return self.name
    
class Author(models.Model):
    about1 = models.CharField(max_length=999)

class Faxrimiz(models.Model):
    images = models.ImageField(upload_to='image/')
    name = models.CharField(max_length=100,blank=True,null=True)
    img= models.ImageField(upload_to='image/')
    data = models.DateTimeField(auto_now_add=True)
    about = models.CharField(max_length=999)
    aboutt = models.CharField(max_length=999)
    rasm = models.ImageField(upload_to='image/',blank=True,null=True)
    rasm2 = models.ImageField(upload_to='image/',blank=True,null=True)
    rasm3 = models.ImageField(upload_to='image/',blank=True,null=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Authorr(models.Model):
    about1 = models.CharField(max_length=999)

class Uqituv(models.Model):
    name = models.CharField(max_length=150,blank=True)
    img = models.ImageField(upload_to='image/')
    job = models.CharField(max_length=150)
    yil = models.CharField(max_length=150)
    Stafkaa = models.TextChoices('Stafkaa','1stafka yarim_stafka')
    stafka = models.CharField(blank=True,choices=Stafkaa.choices,max_length=30)
    Toifaa = models.TextChoices('Toifaa','3 2 1')
    toifa = models.CharField(blank=True,choices=Toifaa.choices,max_length=100)
    fan = models.CharField(max_length=150)
    video = models.FileField(upload_to="video/%y",validators=[file_size])
    theme = models.CharField(max_length=999)
    author = models.ForeignKey(Authorr,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class About(models.Model):
    images = models.ImageField(upload_to='image/')
    joy = models.CharField(max_length=100,blank=True)
    img= models.ImageField(upload_to='image/')
    about = models.CharField(max_length=999)
    def __str__(self):
        return self.joy

class Direktor(models.Model):
    images = models.ImageField(upload_to='image/')
    ism = models.CharField(max_length=100,blank=True)
    img= models.ImageField(upload_to='image/')
    about = models.CharField(max_length=999)
    def __str__(self):
        return self.ism