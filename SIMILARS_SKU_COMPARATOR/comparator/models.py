from django.db import models
#select max(char_length(lien_image)) from CATALOG 
class Sku(models.Model):
        sku_id = models.CharField(max_length=200)
        sku_one_picture_url = models.CharField(max_length=200,default='')
        sku_one_picture_url = models.CharField(max_length=200,default='')
        sku_two_picture_url = models.CharField(max_length=200,default='')
        sku_two_picture_url = models.CharField(max_length=200,default='')
        sku_one_picture_url = models.CharField(max_length=200,default='')
        sku_one_picture_url = models.CharField(max_length=200,default='')
        sku_three_picture_url = models.CharField(max_length=200,default='')
        sku_three_picture_url = models.CharField(max_length=200,default='')
        sku_four_picture_url = models.CharField(max_length=200,default='')
        sku_four_picture_url = models.CharField(max_length=200,default='')
        sku_five_picture_url = models.CharField(max_length=200,default='')
        sku_five_picture_url = models.CharField(max_length=200,default='')
        sku_six_picture_url = models.CharField(max_length=200,default='')
        sku_six_picture_url = models.CharField(max_length=200,default='')
        def __str__(self):              # __unicode__ on Python 2
                return self.sku_id
