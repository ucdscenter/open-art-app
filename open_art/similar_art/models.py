from django.db import models

# Create your models here.

class Query(models.Model):
    image_name = models.CharField(max_length=200)
    date = models.DateTimeField('date uploaded')


class Response(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    main_responses = models.CharField(max_length=200)

class Art(models.Model):
    art_main_Img = models.ImageField(upload_to ='images/')
