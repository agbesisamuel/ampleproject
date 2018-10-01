import django_filters.rest_framework
from django.shortcuts import render
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend


from restapi.models import ApiData, UseraccountData, VenueData, TokenData, ActivityData, VenueTypeData, MenuData, StartPrice
from restapi.models import TimePhase, Mood, OpenHours
from restapi.serializers import apiSerializer, useraccountSerializer, venueSerializer, tokenSerializer #, photoSerializer
from restapi.serializers import activitydataSerializer, venuetypedataSerializer, menudataSerializer, startpriceSerializer
from restapi.serializers import moodSerializer, timephaseSerializer, openhoursSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import RetrieveAPIView



#Sending email
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect


def email(request):

    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['receiver@gmail.com',]

    send_mail( subject, message, email_from, recipient_list )

    return redirect('redirect to a new page')

def send_email(request):
    subject = request.POST.get('subject', 'Hello')
    message = request.POST.get('message', 'How are you?')
    from_email = request.POST.get('from_email', settings.EMAIL_HOST_USER)
    #from_email = settings.EMAIL_HOST_USER
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['agbesisamuel@gmail.com'])
            #send_mail(subject, message, from_email, ['agbesisamuel@gmail.com'], fail_silently=True)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')


def sendSimpleEmail(request,emailto):
   res = send_mail("hello paul", "comment tu vas?", "ampleappdk@gmail.com", ['agbesisamuel@yahoo.com'])
   return HttpResponse('%s'%res)
###

## ActivityData views
class ActivityDataListView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = ActivityData.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = activitydataSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #testing [permission]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ActivityDataDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = ActivityData.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = activitydataSerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

## VenueTypeData views
class VenueTypeDataListView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = VenueTypeData.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = venuetypedataSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #testing [permission]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VenueTypeDataDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = VenueTypeData.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = venuetypedataSerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


## VenueTypeData views
class MenuDataDataListView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = MenuData.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = menudataSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #testing [permission]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MenuDataDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = MenuData.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = menudataSerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

#################


## StartPrice views
class StartPriceDataListView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = StartPrice.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = startpriceSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #testing [permission]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StartPriceDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = StartPrice.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = startpriceSerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


#for API Key Table
class ApiKeyListView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = ApiData.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = apiSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #testing [permission]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class APIKeyDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = ApiData.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = apiSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #testing [permission]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

#for user table
class UseraccountDataListView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = UseraccountData.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = useraccountSerializer

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #testing [permission]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class UseraccountDataDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = UseraccountData.objects.all()
    serializer_class = useraccountSerializer

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #testing [permission]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

## Token views
#display all token records
class TokenDataListView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = TokenData.objects.all()
    serializer_class = tokenSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #testing [permission]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

#display record using pk
class TokenDataDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = TokenData.objects.all()
    serializer_class = tokenSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #testing [permission]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

## Venue views

#search venues based on all on some of these parameter
class VenueSearchDetailsView( mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                            mixins.RetrieveModelMixin, generics.ListAPIView,
                            generics.GenericAPIView):

    queryset = VenueData.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = venueSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('googleplacesId','venueid','name','streetname','city','loc_lat','loc_lng')
    #serializer_class = venueSerializer
    def get(self, request, *args, **kwargs): #search records not loading into form
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class VenueDataListView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = VenueData.objects.all()

    serializer_class = venueSerializer
    permission_classes = (IsAuthenticated,)
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #testing [permission]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VenueDataDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = VenueData.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = venueSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #testing [permission]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# Time phase
class TimePhaseListView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = TimePhase.objects.all()
    serializer_class = timephaseSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #testing [permission]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TimePhaseDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = TimePhase.objects.all()
    serializer_class = timephaseSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
###



#Mood view
class MoodListView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = Mood.objects.all()
    serializer_class = moodSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #testing [permission]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MoodDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Mood.objects.all()
    serializer_class = moodSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
###


#Open hours
class OpenHoursListView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = OpenHours.objects.all()
    serializer_class = openhoursSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #testing [permission]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OpenHoursDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = OpenHours.objects.all()
    serializer_class = openhoursSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
###


## Photo views
# class PhotoDataListView(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#
#     queryset = PhotoData.objects.all()
#     serializer_class = photoSerializer
#     #permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #testing [permission]
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class PhotoDataDetailView(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#
#     queryset = PhotoData.objects.all()
#     serializer_class = photoSerializer
#     #permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #testing [permission]
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
