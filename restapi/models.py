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
from django.urls import reverse



#API key shall be used to authenticate apps.
#A table of different key and app versions shall be held in this model
class ApiData(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE )
    appid = models.AutoField(primary_key=True, verbose_name="API Id")
    apikey = models.CharField(max_length=100, blank=False, verbose_name="API Key")
    apVersion = models.CharField(max_length=100, blank=False, verbose_name="API Version")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")

    class Meta:
        ordering = ('created',)
        db_table = '"apidata"'
        verbose_name_plural ="Api Key"

    def __str__(self):
        return str(self.apikey)


class UseraccountData(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE )
    #user = models.OneToOneField(user)
    userid = models.AutoField(primary_key=True, verbose_name="User ID")
    fullname = models.CharField(max_length=50, blank=False, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email Address")
    password = models.CharField(max_length=15, blank=False, verbose_name="Password")
    phonenumber = models.CharField(max_length=15, blank=True, verbose_name="Phone Number")
    apikey = models.CharField(max_length=100, blank=False, verbose_name="Api Key")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")

    class Meta:
        ordering = ('fullname',)
        db_table = '"useraccountdata"'
        verbose_name_plural ="User Accounts"

    def __str__(self):
         return '%s %s' % (self.userid, self.fullname)

class TokenData(models.Model):
    tokenid = models.AutoField(primary_key=True, verbose_name="Token ID")
    token = models.CharField(max_length=100, blank=False, verbose_name="Token")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    expiry = models.DateTimeField(verbose_name="Expiring Date")
    user = models.ForeignKey(UseraccountData, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)
        db_table = '"tokendata"'
        verbose_name_plural ="Tokens"

    def __str__(self):
        return '%s %s' % (self.tokenid, self.token)



class ActivityData(models.Model):
    activityid = models.AutoField(primary_key=True, verbose_name="Photo ID")
    title = models.CharField(max_length=100, blank=False, verbose_name="Title")
    subtitle = models.CharField(max_length=100, blank=False, verbose_name="Sub Title")
    image = models.ImageField(upload_to="venues/%Y/%m/", blank=True, null=True, verbose_name="Image")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    class Meta:
        ordering = ('title',)
        db_table = '"activitydata"'
        verbose_name_plural ="Activities"

    def __str__(self):
        return '%s %s' % (self.activityid, self.title)

class VenueTypeData(models.Model):
    venuetypeid = models.AutoField(primary_key=True, verbose_name="Venue type ID")
    description = models.CharField(max_length=100, blank=False, verbose_name="Description")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    class Meta:
        ordering = ('description',)
        db_table = '"venuetypedata"'
        verbose_name_plural ="Venue Type"

    def __str__(self):
        return '%s %s' % (self.venuetypeid, self.description)

class MenuData(models.Model):
    menuid = models.AutoField(primary_key=True, verbose_name="Menu ID")
    name = models.CharField(max_length=100, blank=False, verbose_name="Menu Name")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    class Meta:
        ordering = ('menuid',)
        db_table = '"menudata"'
        verbose_name_plural ="Menu Types"

    def __str__(self):
        return '%s %s' % (self.menuid, self.name)



class VenueData(models.Model):
    venueid = models.AutoField(primary_key=True, verbose_name="Venue ID")
    googleplacesId = models.CharField(max_length=100, blank=True, verbose_name="Google Place ID")
    OSMID = models.CharField(max_length=100, blank=True, verbose_name="OSM ID")
    name = models.CharField(max_length=100, blank=False, verbose_name="Venue Name")
    description = models.CharField(max_length=150, blank=True, verbose_name="Venue Description")
    menu =models.ManyToManyField(MenuData, help_text='Select menu for this venue')
    type = models.ManyToManyField(VenueTypeData, help_text='Select venue type')
    loc_lat = models.CharField(max_length=20, blank=True, verbose_name="Latitude") #Cordinates
    loc_lng = models.CharField(max_length=20, blank=True, verbose_name="Longitude")
    streetname = models.CharField(max_length=100, blank=False, verbose_name="Street Name")
    city = models.CharField(max_length=100, blank=False, verbose_name="City")
    postcode = models.CharField(max_length=100, blank=False, verbose_name="Post Code")
    neighborhood = models.CharField(max_length=100, blank=True, verbose_name="Neighborhood")
    capacity = models.IntegerField(verbose_name="Venue Capacity")
    activities = models.ManyToManyField(ActivityData, help_text='Select activities for this Venue')
    wheelchairavail = models.BooleanField(default=False, verbose_name="Wheel Chair Availability")
    outdoorsitting =models.BooleanField(default=False, verbose_name="Outdoor Sitting")
    smookingavailability =models.BooleanField(default=False, verbose_name="Smooking Availability")
    micro_brewery =models.BooleanField(default=False, verbose_name="Micro Brewery")

    # open_now = models.BooleanField(default=False, verbose_name="Open Now")
    #openperiods = models.ManyToManyField(OpenHours, help_text='Select opening periods')
    website = models.CharField(max_length=200, blank=True, verbose_name="Website Address")
    managername = models.CharField(max_length=25500, blank=True, verbose_name="Managers' Name")

    phonenumber = models.CharField(max_length=20, blank=False, verbose_name="Phone Number")
    email = models.EmailField(max_length=100, blank=True)
    price_start = models.CharField(max_length=100, blank=True, verbose_name="Start Price")
    hits = models.IntegerField(verbose_name="Hits")
    verified = models.BooleanField(default=False, verbose_name="Verified by Administrator")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    #user = models.ForeignKey(UseraccountData, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)
        db_table = '"venuedata"'
        verbose_name_plural ="Venues"

    def __str__(self):
        return '%s %s' % (self.venueid, self.name)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('venue-detail', args=[str(self.venueid)])

    def display_activities(self):
        """Create a string for the Genre. This is required to display activities in Admin."""
        return ', '.join(activities.title for activities in self.activities.all()[:5])

    def display_menu(self):
        """Create a string for the Genre. This is required to display menu in Admin."""
        return ', '.join(menu.name for menu in self.menu.all()[:5])

    def display_type(self):
        """Create a string for the Genre. This is required to display type in Admin."""
        return ', '.join(type.description for type in self.type.all()[:5])

    # def display_openperiods(self):
    #    """Create a string for the Genre. This is required to display type in Admin."""
    #    return ', '.join(openperiods.type for type in self.openperiods.all()[:5])


WEEK_DAYS = (
   ('0', 'SUNDAY'),
   ('1', 'MONDAY'),
   ('2', 'TUESDAY'),
   ('3', 'WEDNESDAY'),
   ('4', 'THURSDAY'),
   ('5', 'FRIDAY'),
   ('6', 'SATURDAY'),
)
class OpenHours(models.Model):

    id = models.AutoField(primary_key=True, verbose_name="ID")
    venue = models.ForeignKey(VenueData, on_delete=models.SET_NULL, null=True, verbose_name="Venue")
    days = models.CharField(max_length=10, choices=WEEK_DAYS, blank=False, verbose_name="Day of week")
    open = models.TimeField(blank=True, verbose_name="Open time")
    closed =models.TimeField(blank=True, verbose_name="Closing time")
    open_alt =models.TimeField(blank=True, verbose_name="Alt open time")
    closed_alt = models.TimeField(blank=True, verbose_name="Alt closing time")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    class Meta:
        ordering = ('days',)
        db_table = '"openhours"'
        verbose_name_plural ="Opening hours"

    def __str__(self):
        return str(self.id)

class PhotoData(models.Model):
    photoid = models.AutoField(primary_key=True, verbose_name="Photo ID")
    back_image = models.ImageField(upload_to="venues/%Y/%m/", blank=True, null=True, verbose_name="Background Image")
    fore_image = models.ImageField(upload_to="venues/%Y/%m/", blank=True, null=True, verbose_name="Profile Gallery")
    width = models.IntegerField(verbose_name="Image width")
    height = models.IntegerField(verbose_name="Image height")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    venue = models.ForeignKey(VenueData, related_name='venuephoto', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)
        db_table = '"photodata"'
        verbose_name_plural ="Venue Pictures"

    def __str__(self):
        return '%s %s' % (self.photoid, self.venue)
