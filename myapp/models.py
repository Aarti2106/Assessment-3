from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    
class User (models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.PositiveSmallIntegerField()
    password=models.CharField(max_length=100)
    cpassword=models.CharField(max_length=100)
    photo=models.ImageField(upload_to="upload_new_photo/")
    usertype=models.CharField(max_length=100,default="admin")
    def __str__(self):
        return self.name
class Products(models.Model):
    category=(
            ('men','men'),
            ('women','women'),
            ('kid','kid'),
        )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product_category=models.CharField(max_length=100,choices=category)
    product_name=models.CharField(max_length=100)
    product_stock=models.PositiveSmallIntegerField()
    product_desc=models.TextField()
    product_expire_date=models.CharField(max_length=100)
    product_image=models.ImageField(upload_to="product_pic/")

    def __str__(self):
        return self.user.name+" - "+self.product_category
def delete_product(request,pk):
    product=Product.objects.get(pk=pk)
    product.delete()
    return redirect('products')