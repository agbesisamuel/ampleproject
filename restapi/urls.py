from django.conf.urls import url
from restapi.views import   ApiKeyListView, APIKeyDetailView,TokenDataListView, TokenDataDetailView, UseraccountDataListView, UseraccountDataDetailView,  VenueSearchDetailsView #, PhotoDataListView,PhotoDataDetailView,
from restapi.views import ActivityDataListView, ActivityDataDetailView, VenueTypeDataListView, VenueTypeDataDetailView, MenuDataDataListView, MenuDataDetailView, StartPriceDetailView, StartPriceDataListView
from restapi.views import OpenHoursListView, OpenHoursDetailView, MoodListView, MoodDetailView, TimePhaseListView, TimePhaseDetailView
from rest_framework.urlpatterns import format_suffix_patterns
from restapi import views
from django.urls import include

#test for login and authentication
# from .views import (
#     LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView
# )


urlpatterns = [
    #url(r'^', admin.site.urls),

    url(r'^apikey/$', views.ApiKeyListView.as_view()),
    url(r'^apikey/(?P<pk>[0-9]+)/$', views.APIKeyDetailView.as_view()),

    url(r'^venue/$', views.VenueDataListView.as_view()),
    url(r'^venue/(?P<pk>[0-9]+)/$', views.VenueDataDetailView.as_view()),
    url(r'^venue/search(?P<name>.+)/$', VenueSearchDetailsView.as_view()), #working

    url(r'^activities/$', views.ActivityDataListView.as_view()),
    url(r'^activities/(?P<pk>[0-9]+)/$', views.ActivityDataDetailView.as_view()),
    #url(r'^activities/search(?P<name>.+)/$', VenueSearchDetailsView.as_view()), #working

    url(r'^venuetypedata/$', views.VenueTypeDataListView.as_view()),
    url(r'^venuetypedata/(?P<pk>[0-9]+)/$', views.VenueTypeDataDetailView.as_view()),

    url(r'^menudata/$', views.MenuDataDataListView.as_view()),
    url(r'^menudata/(?P<pk>[0-9]+)/$', views.MenuDataDetailView.as_view()),

    url(r'^startprice/$', views.StartPriceDataListView.as_view()),
    url(r'^startprice/(?P<pk>[0-9]+)/$', views.StartPriceDetailView.as_view()),

    url(r'^timephase/$', views.TimePhaseListView.as_view()),
    url(r'^timephase/(?P<pk>[0-9]+)/$', views.TimePhaseDetailView.as_view()),

    url(r'^mood/$', views.MoodListView.as_view()),
    url(r'^mood/(?P<pk>[0-9]+)/$', views.MoodDetailView.as_view()),

    url(r'^openhours/$', views.OpenHoursListView.as_view()),
    url(r'^openhours/(?P<pk>[0-9]+)/$', views.OpenHoursDetailView.as_view()),

    url(r'^email/$', views.email), #, name='send_email'
    url(r'^simpleemail/$', views.send_email),


    # url(r'^photo/$', views.PhotoDataListView.as_view()),
    # url(r'^photo/(?P<pk>[0-9]+)/$', views.PhotoDataDetailView.as_view()),
    #test for login and authentication
    # url(r'^user/?$', UserRetrieveUpdateAPIView.as_view()),
    # url(r'^users/?$', RegistrationAPIView.as_view()),
    # url(r'^users/login/?$', LoginAPIView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
