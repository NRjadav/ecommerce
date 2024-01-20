from django.db import models

# Create your models here.


class user(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True,max_length=30)
    password=models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.name

class main_category(models.Model):
    name=models.CharField(max_length=30)

     
    def __str__(self) -> str:
        return self.name


class sub_category(models.Model):
    main_category=models.ForeignKey(main_category,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)

     
    def __str__(self) -> str:
        return self.name

class price(models.Model):
    price=models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.price
    
class color(models.Model):
    color=models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.color

class product(models.Model):
    main_category=models.ForeignKey(main_category,on_delete=models.CASCADE)
    price1=models.ForeignKey(price,on_delete=models.CASCADE,blank=True,null=True)
    color=models.ForeignKey(color,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='image')
    price=models.IntegerField()
    
    def __str__(self) -> str:
        return self.name

class add_cart(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE,blank=True,null=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    qty=models.IntegerField()
    total_price=models.IntegerField()
    def __str__(self) -> str:
        return self.name

class contact_info(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=100)

class billing_details(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    mobile_no=models.IntegerField()
    address_line=models.CharField(max_length=100)
    country=models.CharField(max_length=60)
    city=models.CharField(max_length=60)
    state=models.CharField(max_length=60)
    zipcode=models.IntegerField()


