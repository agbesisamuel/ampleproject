from django.conf.urls import url
from restapi.views import  PhotoDataListView,PhotoDataDetailView, ApiKeyListView, APIKeyDetailView,TokenDataListView, TokenDataDetailView, UseraccountDataListView, UseraccountDataDetailView,  VenueSearchDetailsView #, VenueSearchtListView
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

    # url(r'^useraccount/$', views.UseraccountDataListView.as_view()),
    # url(r'^useraccount/(?P<pk>[0-9]+)/$', views.UseraccountDataDetailView.as_view()),
    #
    # url(r'^token/$', views.TokenDataListView.as_view()),
    # url(r'^token/(?P<pk>[0-9]+)/$', views.TokenDataDetailView.as_view()),

    url(r'^venue/$', views.VenueDataListView.as_view()),
    url(r'^venue/(?P<pk>[0-9]+)/$', views.VenueDataDetailView.as_view()),
    url(r'^venue/search(?P<name>.+)/$', VenueSearchDetailsView.as_view()), #working


    url(r'^photo/$', views.PhotoDataListView.as_view()),
    url(r'^photo/(?P<pk>[0-9]+)/$', views.PhotoDataDetailView.as_view()),

    #test for login and authentication
    # url(r'^user/?$', UserRetrieveUpdateAPIView.as_view()),
    # url(r'^users/?$', RegistrationAPIView.as_view()),
    # url(r'^users/login/?$', LoginAPIView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
