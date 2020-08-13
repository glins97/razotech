from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey

class IOTDevice(models.Model):
    space = models.ForeignKey('Space', on_delete=models.CASCADE)
    mac = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    circuit = models.IntegerField(default=0)

    def __str__(self):
        return '{}: {}'.format(self.space, self.description)

class Lamp(IOTDevice):
    status = models.IntegerField(default=0, verbose_name='intensity')

    def __str__(self):
        return '{}: {}-> {}'.format(self.space, self.description, self.status)

class AirConditioning(IOTDevice):
    status = models.IntegerField(default=0)
    temperature = models.FloatField(default=28)
    configuration = models.TextField(blank=True, null=True)

class AccessDevice(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    mac = models.CharField(max_length=255)
    verified = models.BooleanField(default=False)
    
    def __str__(self):
        return '{}'.format(self.person)

class Mobile(AccessDevice):
    pass

class Web(AccessDevice):
    pass
    
class Building(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return '{}: {}'.format(self.code, self.name)

class Space(models.Model):
    building = models.ForeignKey('Building', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{}: {}'.format(self.building.name, self.name)

class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return '{}'.format(self.name)
    
class Access(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, max_length=255, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}: {}'.format(self.person, self.building)
    
class Request(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    device = models.ForeignKey(IOTDevice, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    
    def __str__(self):
        return '{}, {}: {}'.format(self.person.name, self.device, self.status)