import datetime
from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField

#from django.utils import timezone
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
#from djangotoolbox.fields import ListField

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight



#API key shall be used to authenticate apps.
#A table of different key and app versions shall be held in this model
class ApiData(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE )
    appid = models.AutoField(primary_key=True)
    apikey = models.CharField(max_length=100, blank=False)
    apVersion = models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
        db_table = '"apidata"'
        verbose_name_plural ="Api Key"

    def __str__(self):
        return str(self.apikey)


class UseraccountData(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE )
    #user = models.OneToOneField(user)
    userid = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=50, blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=15, blank=False)
    phonenumber = models.CharField(max_length=15, blank=True)
    apikey = models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('fullname',)
        db_table = '"useraccountdata"'
        verbose_name_plural ="User Accounts"

    def __str__(self):
         return '%s %s' % (self.userid, self.fullname)

class TokenData(models.Model):
    tokenid = models.AutoField(primary_key=True)
    token = models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    expiry = models.DateTimeField()
    user = models.ForeignKey(UseraccountData, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)
        db_table = '"tokendata"'
        verbose_name_plural ="Tokens"

    def __str__(self):
        return '%s %s' % (self.tokenid, self.token)

class VenueData(models.Model):
    PRICE_RANGE = (
        ('0', 'FREE'),
        ('1', 'INEXPENSIVE'),
        ('2', 'MODERATE'),
        ('3', 'EXPENSIVE'),
        ('4', 'VERY EXPENSIVE'),
    )


    venueid = models.AutoField(primary_key=True, verbose_name="Venue ID")
    googleplacesId = models.CharField(max_length=100, blank=True, verbose_name="Google Place ID")
    OSMID = models.CharField(max_length=100, blank=True, verbose_name="OSM ID")
    name = models.CharField(max_length=100, blank=False, verbose_name="Venue Name")
    description = models.CharField(max_length=100, blank=True, verbose_name="Venue Description")
    menu =JSONField(verbose_name="Wheel Chair Availability")
    type = ArrayField(models.CharField(max_length=50, blank=True, verbose_name="Type")
    loc_lat = models.CharField(max_length=20, blank=True, verbose_name="Latitude") #Cordinates
    loc_lng = models.CharField(max_length=20, blank=True, verbose_name="Longitude")
    streetname = models.CharField(max_length=100, blank=False, verbose_name="Street Name")
    city = models.CharField(max_length=100, blank=False, verbose_name="City")
    postcode = models.CharField(max_length=100, blank=False, verbose_name="Post Code")
    neighborhood = models.CharField(max_length=100, blank=True, verbose_name="Neighborhood")
    capacity = models.IntegerField(verbose_name="Venue Capacity")
    wheelchairavail = models.BooleanField(default=False, verbose_name="Wheel Chair Availability")
    outdoorsitting =models.BooleanField(default=False, verbose_name="Outdoor Sitting")
    smookingavailability =models.BooleanField(default=False, verbose_name="Smooking Availability")
    micro_brewery =models.BooleanField(default=False, verbose_name="Micro Brewery")
    open_now = models.BooleanField(default=False, verbose_name="Open Now")
    open_periods = JSONField(verbose_name="Open Periods")
    website = models.CharField(max_length=200, blank=True, verbose_name="Website Address")
    phonenumber = models.CharField(max_length=20, blank=False, verbose_name="Phone Number")
    email = models.EmailField(max_length=100, blank=True)
    price_start = models.CharField(max_length=100, blank=True, verbose_name="Start Price
    hits = models.IntegerField(verbose_name="Hits")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    #user = models.ForeignKey(UseraccountData, on_delete=models.CASCADE)
    class Meta:
        ordering = ('created',)
        db_table = '"venuedata"'
        verbose_name_plural ="Venues"

    def __str__(self):
        return '%s %s' % (self.venueid, self.name)

class PhotoData(models.Model):
    photoid = models.AutoField(primary_key=True)
    imageobject = models.ImageField(upload_to="venues/%Y/%m/", blank=True, null=True)
    width = models.IntegerField()
    height = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    venue = models.ForeignKey(VenueData, related_name='venuephoto', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)
        db_table = '"photodata"'
        verbose_name_plural ="Venue Pictures"

    def __str__(self):
        return '%s %s' % (self.photoid, self.venue)
