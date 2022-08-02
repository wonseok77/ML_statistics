from django.db import models

# Create your models(=Table) here.

# class name == Table name
class Curriculum(models.Model) :
    # 변수 이름 == 컬럼 이름..
    name = models.CharField(max_length=255)