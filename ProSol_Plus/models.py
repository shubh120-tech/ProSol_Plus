from django.db import models
from datetime import datetime
# Create your models here.

class SignUp(models.Model):

    name = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    mobile = models.IntegerField()

    def __str__(self):
        return self.name

class UserFile(models.Model):
    namefile = models.ForeignKey(SignUp,on_delete=models.CASCADE)
    file = models.FileField(upload_to='ProSol_Plus/files', default="")
    date = models.DateTimeField(default=datetime.now())


    def __str__(self):
        return self.namefile.name

class Solution(models.Model):
    namefile = models.ForeignKey(UserFile,on_delete=models.CASCADE)
    file = models.FileField(upload_to='ProSol_Plus/Solutions', default="")
    amount = models.IntegerField(default=0)


    def __str__(self):
        return self.namefile.namefile.name




