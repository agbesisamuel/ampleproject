from django.contrib import admin
from .models import ApiData, UseraccountData, VenueData, TokenData, VenueTypeData, MenuData, ActivityData, StartPrice # PhotoData,
from .models import OpenHours, TimePhase, Mood


# Register your models here.
#admin.site.register(OpenHours)
admin.site.register(ApiData)
#admin.site.register(VenueData)
#admin.site.register(PhotoData)





# class OpenHoursAdmin(admin.ModelAdmin):
#     #pass
#     list_display = ('venue', 'days', 'open', 'closed', 'open_alt',
#                     'closed_alt')
#     fields = ['venue', 'days', ('open', 'closed'), ('open_alt','closed_alt')] #controls how the fields are displayed
# admin.site.register(OpenHours, OpenHoursAdmin)


# Register the Admin classes for VenueTypeData using the decorator
@admin.register(StartPrice)
class StartPriceAdmin(admin.ModelAdmin):
    pass


@admin.register(OpenHours)
class OpenHourseAdmin(admin.ModelAdmin):
    pass

@admin.register(TimePhase)
class TimePhaseAdmin(admin.ModelAdmin):
    pass

@admin.register(Mood)
class MoodAdmin(admin.ModelAdmin):
    pass



@admin.register(VenueTypeData)
class VenueTypeDataAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for MenuData using the decorator
@admin.register(MenuData)
class MenuDataAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for ActivityData using the decorator
@admin.register(ActivityData)
class ActivityDataAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for VenueData using the decorator
@admin.register(VenueData)
class VenueAdmin(admin.ModelAdmin):
    #pass
    # list_display = ('name', 'description','streetname', 'city','postcode', 'neighborhood',
    #                 'loc_lat', 'loc_lng','display_menu', 'display_activities', 'display_type','capacity', 'wheelchairavail',
    #                 'capacity', 'wheelchairavail','outdoorsitting','smookingavailability',
    #                 'micro_brewery','price_start','hits', 'managername', 'email','website','phonenumber'
    #                 )
    list_filter = ('venueid','name', 'description')
    list_display = ('name', 'description','streetname', 'city','postcode', 'display_type', 'verified','display_activities')


    fieldsets = (
        ('Venue Infomation', {
            'fields' : [('name', 'description'), ('streetname','city'),
                       ('postcode','loc_lat', 'loc_lng', 'capacity'),
                       ('type','activities'),('wheelchairavail', 'outdoorsitting'),
                       ('smookingavailability','micro_brewery'), ('note_to_admin')
                      ]
            }),
            ('Photo Gallery', {
                    'fields' : [('back_image_one', 'back_image_two'),
                                ('fore_image_one','fore_image_two')

                                ]
            }),
            ('Contact Info', {
                    'fields' : [('managername', 'email'),('website','phonenumber'),
                              ('verified')]
            }),
    )
