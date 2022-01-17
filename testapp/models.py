from django.db import models

class employee(models.Model):
    eno =models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.FloatField()
    
    def __str__(self):
        return str(self.eno)+"  "+str(self.ename)+"  "+str(self.esal)
class Testapp_User(models.Model):
    username=models.CharField(max_length=20, primary_key=True)
    password=models.CharField(max_length=20)

class newEmployee(models.Model):
    eno =models.IntegerField()
    ename=models.CharField(max_length=30)
    bdate=models.CharField(max_length=15)
    eaddress=models.CharField(max_length=150)
    estate=models.CharField(max_length=40)
    enum=models.IntegerField()
    erole=models.CharField(max_length=25)
    esal=models.FloatField()
    ejoin=models.CharField(max_length=20)




class advanceForm(models.Model):
    eno =models.IntegerField()
    ename=models.CharField(max_length=30)
    erole=models.CharField(max_length=25)
    edate=models.CharField(max_length=20)
    eadvance=models.FloatField()

class salaryForm(models.Model):
    eno =models.IntegerField()
    ename=models.CharField(max_length=30)
    emonth=models.CharField(max_length=15)
    edate=models.CharField(max_length=150)
    erole=models.CharField(max_length=40)
    ebasic=models.FloatField()
    epf=models.FloatField()
    eadvance=models.FloatField()
    enet=models.FloatField()
    