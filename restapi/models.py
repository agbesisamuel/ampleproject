import datetime
from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField
from django.core.validators import MaxValueValidator, MinValueValidator

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
        verbose_name_plural ="Menu Items"

    def __str__(self):
        return '%s %s' % (self.menuid, self.name)



class VenueData(models.Model):

    venueid = models.AutoField(primary_key=True, verbose_name="Venue ID")
    #googleplacesId = models.CharField(max_length=100, blank=True, verbose_name="Google Place ID")
    OSMID = models.CharField(max_length=100, blank=True, verbose_name="OSM ID")
    name = models.CharField(max_length=100, blank=False, unique=False, verbose_name="Venue Name")
    description = models.CharField(max_length=150, blank=False, verbose_name="Venue Description")
    #menu_item =models.ManyToManyField(MenuData, help_text='Select menu item for this venue', verbose_name="Menu Item")
    type = models.ManyToManyField(VenueTypeData, help_text='Select venue type')
    loc_lat = models.CharField(max_length=20, blank=False, verbose_name="Latitude") #Cordinates
    loc_lng = models.CharField(max_length=20, blank=False, verbose_name="Longitude")
    streetname = models.CharField(max_length=100, blank=False, verbose_name="Street Name")
    streetnumber = models.CharField(max_length=10, blank=False, verbose_name="Street Number")
    city = models.CharField(max_length=100, blank=False, verbose_name="City")
    postcode = models.CharField(max_length=100, blank=False, verbose_name="Post Code")
    area = models.CharField(max_length=100, blank=True, verbose_name="Area")
    capacity = models.IntegerField(verbose_name="Venue Capacity")
    activities = models.ManyToManyField(ActivityData, blank=True,  help_text='Select activities for this Venue')
    wheelchairavail = models.BooleanField(default=False, verbose_name="Wheel Chair Availability")
    outdoorsitting =models.BooleanField(default=False, verbose_name="Outdoor Sitting")
    smookingavailability =models.BooleanField(default=False, verbose_name="Smooking Availability")
    micro_brewery =models.BooleanField(default=False, verbose_name="Micro Brewery")

    back_image_one = models.ImageField(upload_to="venues/%Y/%m/", blank=True, null=True, verbose_name="Background Image One")
    back_image_two = models.ImageField(upload_to="venues/%Y/%m/", blank=True, null=True, verbose_name="Background Image Two")
    fore_image_one = models.ImageField(upload_to="venues/%Y/%m/", blank=True, null=True, verbose_name="Profile Gallery One")
    fore_image_two = models.ImageField(upload_to="venues/%Y/%m/", blank=True, null=True, verbose_name="Profile Gallery Two")
    # width = models.IntegerField(verbose_name="Image width")
    # height = models.IntegerField(verbose_name="Image height")

    # open_now = models.BooleanField(default=False, verbose_name="Open Now")
    #openperiods = models.ManyToManyField(OpenHours, help_text='Select opening periods')
    #OpenHours = JSONField(verbose_name="Open Periods")
    website = models.CharField(max_length=200, blank=True, null=True, verbose_name="Website Address")
    managername = models.CharField(max_length=25500, blank=True, null=True, verbose_name="Managers' Name")

    phonenumber = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone Number")
    email = models.EmailField(max_length=100, blank=True, null=True)
    hits = models.IntegerField(verbose_name="Hits", default=0)
    verified = models.BooleanField(default=False, verbose_name="Verified by Administrator")
    note_to_admin = models.TextField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    #user = models.ForeignKey(UseraccountData, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)
        db_table = '"venuedata"'
        verbose_name_plural ="Venues"

    def __str__(self):
        return '%s %s' % (self.venueid, self.name)

    # def get_image_url(self):
    #     img = self.photodata_set.first()
    #     return img.back_image.url if img else img

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('venue-detail', args=[str(self.venueid)])

    def display_activities(self):
        """Create a string for the Genre. This is required to display activities in Admin."""
        return ', '.join(activities.title for activities in self.activities.all()[:5])



    # def display_menu(self):
    #     """Create a string for the Genre. This is required to display menu in Admin."""
    #     return ', '.join(menu.name for menu in self.menu.all()[:5])

    def display_type(self):
        """Create a string for the Genre. This is required to display type in Admin."""
        return ', '.join(type.description for type in self.type.all()[:5])


    # def display_openperiods(self):
    #    """Create a string for the Genre. This is required to display type in Admin."""
    #    return ', '.join(openperiods.type for type in self.openperiods.all()[:5])


class StartPrice(models.Model):
    transid = models.AutoField(primary_key=True, verbose_name="Id")
    menu= models.ForeignKey('MenuData', on_delete=models.CASCADE, related_name='menu_item', verbose_name="Menu Item")
    venue = models.ForeignKey('VenueData',related_name='venue_start_price', on_delete=models.CASCADE)
    start_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, verbose_name="Start Price")

    class Meta:
        ordering = ('transid',)
        db_table = '"startprice"'
        verbose_name_plural ="Start Price"

    def __str__(self):
        #return str(self.transid)
        return '%s %s %s' % (self.venue, self.menu, self.start_price)

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
    venue = models.ForeignKey(VenueData, related_name='venue_opening_periods', on_delete=models.SET_NULL, null=True, verbose_name="Venue")
    days = models.CharField(max_length=10, choices=WEEK_DAYS, blank=False, verbose_name="Day of week")
    open = models.TimeField(blank=True, verbose_name="Open time")
    close =models.TimeField(blank=True, verbose_name="Closing time")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    class Meta:
        ordering = ('venue',)
        db_table = '"openhours"'
        verbose_name_plural ="Opening hours"

    def __str__(self):
        return '%s %s %s  %s' % (self.venue, self.days, self.open, self.close)

#Phase Mood - Morning: 04:00 - 11:59, Afternoon, Evening, Night
class TimePhase(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    phase = models.CharField(max_length=100, blank=False, verbose_name="Time of the day")
    starttime =models.TimeField(blank=True, verbose_name="Start time")
    endtime = models.TimeField(blank=True, verbose_name="End time")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    class Meta:
        ordering = ('phase',)
        db_table = '"timephase"'
        verbose_name_plural ="Time Phase"

    def __str__(self):
        return '%s %s %s' % (self.phase, self.starttime, self.endtime)


#Moods
class Mood(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    phase = models.ForeignKey(TimePhase, on_delete=models.SET_NULL, null=True, verbose_name="Phase")
    venue = models.ForeignKey(VenueData, related_name='venue_moods', on_delete=models.SET_NULL, null=True, verbose_name="Venue")
    value = models.DecimalField(decimal_places=2, max_digits=5, null=True, validators=[MaxValueValidator(10), MinValueValidator(0.1)])
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    class Meta:
        ordering = ('id',)
        db_table = '"mood"'
        verbose_name_plural ="Mood"

    def __str__(self):
        return '%s %s %s' % (self.phase, self.venue, self.value)



# class PhotoData(models.Model):
#     photoid = models.AutoField(primary_key=True, verbose_name="Photo ID")
#     back_image = models.ImageField(upload_to="venues/%Y/%m/", blank=True, null=True, verbose_name="Background Image")
#     fore_image = models.ImageField(upload_to="venues/%Y/%m/", blank=True, null=True, verbose_name="Profile Gallery")
#     width = models.IntegerField(verbose_name="Image width")
#     height = models.IntegerField(verbose_name="Image height")
#     created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
#     venue = models.ForeignKey(VenueData, related_name='venuephoto', on_delete=models.CASCADE)
#
#     class Meta:
#         ordering = ('created',)
#         db_table = '"photodata"'
#         verbose_name_plural ="Venue Pictures"
#
#     def __str__(self):
#         return '%s %s' % (self.photoid, self.venue)
