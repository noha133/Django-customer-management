from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=250, null=True)
    phone = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250, null=True)
    data_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name



class product(models.Model):
    CATEGORY = (
        ('SuperMarket', 'SuperMarket'),
        ('Fashion', 'Fashion'),
        ('Electronics', 'Electronics'),
        ('Beauty', 'Beauty'),
    )
    name = models.CharField(max_length=250, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=250, null=True)
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name



class order(models.Model):
    STATUS = (('Pending' , 'Pending'),
              ('Out for delivery' , 'Out for delivey'),
              ('Delivered' ,  'Delivered'))
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.product.name


