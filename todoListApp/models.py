from django.db import models

# Create your models here.

class Class(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)

    class Meta:
        # Changes the admin panels name to "Classes" instead of "Classs"
        verbose_name_plural = 'Classes'

class Assignment(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 80)
    classId = models.ForeignKey(Class,on_delete=models.CASCADE)
    dueDate = models.DateTimeField()
    completed = models.BooleanField()

