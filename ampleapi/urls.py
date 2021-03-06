"""ampleapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
# from rest_framework_jwt.views import obtain_jwt_token
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#imports for media files
from django.conf import settings
#from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
    path('', admin.site.urls),
    url (r'^', include('restapi.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^auth/', include('authentication.urls')), #'

    #Social login
    url(r'^accounts/', include('allauth.urls')),


]

# for media
# if settings.DEBUG:
#     urlpatterns += [
#         url(r'^media/(?P<path>.*)$', serve, {
#             'document_root' : settings.MEDIA_ROOT,
#         }),
#     ]
