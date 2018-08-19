from django.contrib import admin
from .models import ApiData, UseraccountData, VenueData, TokenData, PhotoData, VenueTypeData, MenuData, ActivityData, OpenHours


# Register your models here.
#admin.site.register(OpenHours)
admin.site.register(ApiData)
#admin.site.register(VenueData)
admin.site.register(PhotoData)



class OpenHoursAdmin(admin.ModelAdmin):
    #pass
    list_display = ('venue', 'days', 'open', 'closed', 'open_alt',
                    'closed_alt')
    fields = ['venue', 'days', ('open', 'closed'), ('open_alt','closed_alt')] #controls how the fields are displayed
admin.site.register(OpenHours, OpenHoursAdmin)


# Register the Admin classes for VenueTypeData using the decorator
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
    list_display = ('name', 'description','streetname', 'city','postcode', 'verified')


    fieldsets = (
        ('Venue Infomation', {
            'fields' : [('name', 'description'), ('streetname','city'),
                       ('postcode','neighborhood'),('loc_lat', 'loc_lng', 'capacity'),
                       ('type','activities'),('wheelchairavail', 'outdoorsitting'),
                       ('smookingavailability','micro_brewery'),('menu','price_start')
                      ]
            }),
            ('Contact Info', {
                    'fields' : [('managername', 'email'),('website','phonenumber'),
                              ('verified')]
            }),
    )


    # @admin.register(BookInstance)
    # class BookInstanceAdmin(admin.ModelAdmin):
    #     list_filter = ('status', 'due_back')
    #     #grouping fields
    #     fieldsets = (
    #         (None, {
    #             'fields': ('book', 'imprint', 'id')
    #         }),
    #         ('Availability', {
    #             'fields': ('status', 'due_back')
    #         }),
    #     )


    # fields = [('name', 'description'),('streetname', 'city'),
    #           ('postcode','neighborhood'),
    #           ('loc_lat', 'loc_lng'),('display_menu', 'display_type','display_activities'),
    #            ('wheelchairavail', 'capacity', 'outdoorsitting'),
    #            ('smookingavailability','micro_brewery'),
    #            ('price_start','hits'), ('managername', 'email'),('website','phonenumber')
    #            ] #controls how the fields are displayed

    # fieldsets = (
    #     ('Venu Infomation', {
    #         'fields': ('name', 'description')#, ('streetname', 'city')
    #                   # ('postcode', 'neighborhood'), ('loc_lat', 'loc_lng'),
    #                   # ('muen', 'type'), ('capacity', 'wheelchairavail'),
    #                   # ('capacity', 'wheelchairavail','outdoorsitting','smookingavailabilitymicro_brewery),
    #                   # ('price_start','hits')
    #     }),
    #     ('Contact Info', {
    #         'fields': ('managername', 'email')#, ('website','phonenumber')
    #     }),
