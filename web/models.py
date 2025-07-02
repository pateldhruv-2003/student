from django.db import models

# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class student(models.Model):
    
    gender=(
        ('male','male'),
        ('female','female'),
    )
    Ahemedabad='Ahemedabad'
    Surendranagar='Surendranagar'
    Surat='Surat'
    Bhavnagar='Bhavnagar'
    Gandhinagar='Gandhinagar'
    City=(
        (Ahemedabad,'Ahemedabad'),
        (Surendranagar,'Surendranagar'),
        (Surat,'Surat'),
        (Bhavnagar,'Bhavnagar'),
        (Gandhinagar,'Gandhinagar')
            
    )
    fname=models.CharField(max_length=100,default="")
    lname=models.CharField(max_length=100,default="")
    rno=models.IntegerField(default=0)
    std=models.IntegerField(default=0)
    gender=models.CharField(max_length=200,choices=gender,default="male")
    city=models.CharField(max_length=50,choices=City,default="Ahemaedabad")
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="uploads/",default="")
    courses= models.CharField(max_length=100,default=0)

    
    
    def __str__(self):
        return self.fname
    
class fees(models.Model):
    Cash='Cash'
    Online='Online'
    Card='Card'
    pay_method=(
        (Cash,'Cash'),
        (Online,'Online'),
        (Card,'Card')
    )
    student= models.ForeignKey(student, on_delete=models.CASCADE, related_name='fees')
    payment= models.DecimalField(max_digits=10, decimal_places=4)
    date_paid= models.DateField()
    take= models.CharField(max_length=50)
    pay_method=models.CharField(max_length=50,choices=pay_method)
    
    def __str__(self):
        return self.take
            
    
class product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField()
    review = models.TextField()
    image = models.ImageField(upload_to="uploads/",default="")

    def __str__(self):
        return self.name
                
             
class contact(models.Model):
    fname = models.CharField(max_length=300)
    lname = models.CharField(max_length=300)
    email = models.CharField(max_length=200,default="")
    group = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    image = models.ImageField(upload_to="uploads/",default="")
    birth = models.DateField()
   
    
    def __str__(self):
        return self.fname         
    
    
    
    