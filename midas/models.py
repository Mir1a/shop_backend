from django.db import models

# Create your models here.

class item(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=500)
    description = models.TextField(max_length=1000, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    code = models.CharField(max_length=15)
    color = models.CharField(max_length=20)
    weight = models.DecimalField(max_digits=10, decimal_places=1)
    height = models.DecimalField(max_digits=10, decimal_places=1)
    width = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class user(models.Model):
    models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    #avatar = models.ImageField(upload_to='avatars')
    favorite = models.ForeignKey(to=item, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.id

class order(models.Model):
    models.AutoField(primary_key=True)
    item = models.ForeignKey(to=item, on_delete=models.CASCADE, null=True)
    amount_items = models.IntegerField()
    user = models.OneToOneField(to=user, on_delete=models.CASCADE, null=True)
    sum_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.id

class transaction(models.Model):
    models.AutoField(primary_key=True)
    code = models.CharField(max_length=50)
    user = models.ManyToManyField(to=user, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)
    order = models.OneToOneField(to=order, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.id



class supplies(models.Model):
    models.AutoField(primary_key=True)
    #словарь сделать

    def __str__(self):
        return self.id

