from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):    #yaane traveler bel class diagram
    class Meta:
        db_table = 'User'
    receive_promotions = models.BooleanField(
        default=False
    )
    birthdate = models.DateField(
        null=True,blank=True
    )

class City(models.Model):
    class Meta:
        db_table = 'City'
    name = models.CharField(max_length=40)   

class Hotel(models.Model): #bss naamoul extend la models.Model , django bi sir fio yaamoul interaction maa l database
    #ma hatayna id la2n django automatically bye5la2la id lal class
    class Meta:
        db_table = 'Hotel'
    name = models.CharField(max_length=40)
    rating = models.DecimalField(decimal_places=1,max_digits=2)
    image = models.URLField()
    city = models.ForeignKey(City,on_delete=models.CASCADE)


class Room(models.Model):
    ROOM_CATEGORIES = [
        ('standard', 'Standard Room'),  #first is how is stored in db , second is what the user sees
        ('deluxe', 'Deluxe Room'),
        ('suite', 'Suite'),
        ('executive', 'Executive Room'),
        ('family', 'Family Room'),
        ('junior_suite', 'Junior Suite'),
        ('connecting', 'Connecting Rooms'),
        ('honeymoon', 'Honeymoon Suite'),
        ('penthouse', 'Penthouse Suite'),
        ('accessible', 'Accessible Room'),
    ]
    class Meta:
        db_table = 'Room'
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=5,decimal_places=1)
    number = models.IntegerField()
    image = models.URLField()
    category = models.CharField(max_length=20,null=True,blank=True,choices=ROOM_CATEGORIES)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.number}. {self.category} for {self.capacity} people'
    

class Airline(models.Model):
    class Meta:
        db_table = 'Airline'
    name = models.CharField(max_length=40)

class AirPort(models.Model):
    class Meta:
        db_table = 'AirPort'
    name = models.CharField(max_length=40)

class Flight(models.Model):
    class Meta:
        db_table = 'Flight'
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    is_Refundable = models.BooleanField()
    image = models.URLField()
    airport_from = models.ForeignKey(AirPort,on_delete=models.CASCADE ,related_name="departure")    
    airport_to = models.ForeignKey(AirPort,on_delete=models.CASCADE ,related_name="arrival")


class Country(models.Model):
    class Meta:
        db_table = 'Country'
    name = models.CharField(max_length=50)


class Booking(models.Model):
    class Meta:
        db_table = 'Booking'
    date = models.DateField()
    cost = models.DecimalField(decimal_places=2,max_digits=6)  #lezim zabeta hay champ calcule
    cancel_date = models.DateField()

class RoomBooked(models.Model):
    class Meta:
        db_table = 'RoomBooked'    
        unique_together = [('room','booking')]    
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking,on_delete=models.CASCADE)
    checkin = models.DateTimeField()
    checkout = models.DateTimeField()

class Payment(models.Model):
    class Meta:
        db_table = 'Payment'
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateTimeField()
    booking = models.ForeignKey(Booking,on_delete=models.CASCADE)











    