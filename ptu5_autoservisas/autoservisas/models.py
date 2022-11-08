from django.db import models
import uuid
# Create your models here.


class CarModel(models.Model):
    brand = models.CharField('brand', max_length = 200, help_text = 'Enter name of car brand')
    model = models.CharField('model', max_length = 200)
    year = models.DateField('manufacture year')

    def __str__(self):
        return f"{self.brand} : {self.model} -- {self.year}"

class Car(models.Model):
    car_nr = models.CharField('car number', max_length=50, help_text = 'Enter car number')
    vin_code = models.CharField('VIN code', max_length=17, null=True, blank=True,
        help_text='<a href="https://www.autocheck.com/vehiclehistory/vin-basics" target="_blank">VIN code</a> consisting of 17 symbols')
    client = models.CharField('cliens name', max_length = 255)
    car_model = models.ForeignKey(CarModel, on_delete = models.SET_NULL, null = True, blank = True)


    def __str__(self):
        return f"{self.client} - {self.car_nr}, {self.car_model}"

class Service(models.Model):
    name = models.CharField('service name', max_length = 255, help_text = "Write down service name")
    price = models.DecimalField('price', max_digits = 18, decimal_places = 2)

    def __str__(self):
        return f"{self.name} - {self.price}€."



class Order(models.Model):
    unique_id = models.UUIDField('unique ID', default = uuid.uuid4, editable = False)
    date = models.DateField('orders date')
    total_sum = models.DecimalField('price', max_digits = 18, decimal_places = 2)
    car = models.ForeignKey(Car, on_delete = models.SET_NULL, null = True, blank = True)

    def __str__(self):
        return f"{self.unique_id} - {self.total_sum}€."


class OrderLine(models.Model):
    service = models.ManyToManyField(Service, help_text = 'Choose service', verbose_name = 'service(s)')
    order = models.ForeignKey(Order, on_delete = models.CASCADE, null = True, blank = True)
    amount = models.IntegerField('amount of services')
    price = models.DecimalField('price', max_digits = 18, decimal_places = 2)


    # def total_price(self):
    #     return self.price * self.amount
    

    def __str__(self):
        return f"{self.service.name}, {self.order} - {self.price}€."


#     created = models.DateTimeField(auto_now_add=True)
#   modified = models.DateTimeField(auto_now=True)


