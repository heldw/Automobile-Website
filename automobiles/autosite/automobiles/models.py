from django.db import models

class Person(models.Model):
     user_id = models.CharField(max_length=200)
     first_name = models.CharField(max_length=200) 
     last_name = models.CharField(max_length=200)
     email = models.CharField(max_length=200)

     def __str__(self):
         return '%s %s' % (self.first_name, self.last_name)

     def get_absolute_url(self):
         return u'/automobiles/car/person'


class Car(models.Model):
     car_id = models.CharField(max_length=200)
     year = models.IntegerField(default=0) 
     make = models.CharField(max_length=200)
     model = models.CharField(max_length=200)
     price = models.IntegerField(default=0) 

     def __str__(self):
         return '%s %s' % (self.make, self.model)

     def get_absolute_url(self):
         return u'/automobiles/'

class Motorcycle(models.Model):
     motorcycle_id = models.CharField(max_length=200)
     year = models.IntegerField(default=0) 
     make = models.CharField(max_length=200)
     model = models.CharField(max_length=200)
     price = models.IntegerField(default=0) 
    
     def get_absolute_url(self):
         return u'/automobiles/car/motorcycles'

     def __str__(self):
         return '%s %s' % (self.make, self.model)

#class CarOwner(models.Model):
  #   person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key= True,)

   #  def get_absolute_url(self):
  #       return u'/automobiles/car/carowners'

#class MotorcycleOwner(models.Model):
 #    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key= True,)

class PersonOwnsCar(models.Model):
     Quantity = models.IntegerField(default=0)
     Person = models.ForeignKey(Person, on_delete=models.CASCADE)
     Car = models.ForeignKey(Car, on_delete=models.CASCADE)

     def get_absolute_url(self):
         return u'/automobiles/car/personownscars'

class PersonOwnsMotorcycle(models.Model):
     Quantity = models.IntegerField(default=0)
     Person = models.ForeignKey(Person, on_delete=models.CASCADE)
     Motorcycle = models.ForeignKey(Motorcycle, on_delete=models.CASCADE)

     def get_absolute_url(self):
         return u'/automobiles/car/personownsmotorcycles'

 


