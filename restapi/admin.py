from django.contrib import admin
from .models import ApiData, UseraccountData, VenueData, TokenData, PhotoData


# Register your models here.
#admin.site.register(UseraccountData)
admin.site.register(ApiData)
admin.site.register(VenueData)
admin.site.register(PhotoData)
