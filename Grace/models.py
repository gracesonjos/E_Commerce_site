from django.db import models



class idgen(models.Model):
    categoryid = models.IntegerField()
    shopeid = models.IntegerField()
    productid=models.IntegerField()
    coustomerid=models.IntegerField()
    reviewid=models.IntegerField()
    orderid=models.IntegerField()
    agentid=models.IntegerField()

    
    class Meta:
        db_table= "idgen"


class tbl_category(models.Model):
    category_id = models.CharField(primary_key=True,max_length=225)
    category_name = models.CharField(max_length=100)
    photo = models.CharField(max_length=225)
    description = models.CharField(max_length=225)
    
    class Meta:
        db_table= "tbl_category"


class tbl_shope(models.Model):
    shope_id = models.CharField(primary_key=True,max_length=225)
    shope_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    pincode = models.IntegerField()
    phone_number= models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    photo = models.CharField(max_length=225)
    username = models.CharField(max_length=200)

    class Meta:
        db_table= "tbl_shope"


class tbl_product(models.Model):
    product_id = models.CharField(primary_key=True,max_length=225)
    category_id= models.ForeignKey(tbl_category, on_delete=models.CASCADE)
    shope_id= models.ForeignKey(tbl_shope, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    photo = models.CharField(max_length=225)
    stock = models.IntegerField()
    
    class Meta:
        db_table= "tbl_product"


class tbl_coustomer(models.Model):
    coustomer_id = models.CharField(primary_key=True,max_length=225)
    coustomer_name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    pincode = models.IntegerField()
    phone_number= models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=200)

    class Meta:
        db_table= "tbl_coustomer"

class tbl_login(models.Model):
    username = models.CharField(primary_key=True,max_length=225)
    password = models.CharField(max_length=100)
    category = models.CharField(max_length=200)
    hint = models.CharField(max_length=200)

    class Meta:
        db_table= "tbl_login"

class tbl_review(models.Model):
    review_id = models.CharField(primary_key=True,max_length=225)
    review = models.CharField(max_length=225)
    review_date = models.CharField(max_length=200)
    product_id = models.ForeignKey(tbl_product, on_delete=models.CASCADE)
    coustomer_id = models.ForeignKey(tbl_coustomer, on_delete=models.CASCADE)

    class Meta:
        db_table= "tbl_review"

class tbl_order(models.Model):
    order_id = models.CharField(primary_key=True,max_length=225)
    product_id = models.ForeignKey(tbl_product, on_delete=models.CASCADE)
    status = models.CharField(max_length=225)
    order_date = models.CharField(max_length=200)
    oder_quandity=models.IntegerField()
    coustomer_id = models.ForeignKey(tbl_coustomer, on_delete=models.CASCADE)
    delivery_adress =models.CharField(max_length=200)
    total_amount=models.IntegerField()
    
    class Meta:
        db_table= "tbl_order"


class tbl_deliveryagent(models.Model):
    agent_id = models.CharField(primary_key=True,max_length=225)
    agent_name = models.CharField(max_length=100)
    phone_number= models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=200)

    class Meta:
        db_table= "tbl_deliveryagent"



# Create your models here.
