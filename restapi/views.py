import django_filters.rest_framework
from django.shortcuts import render
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend


from restapi.models import ApiData, UseraccountData, VenueData, TokenData, PhotoData #, OpeningPeriods
from restapi.serializers import apiSerializer, useraccountSerializer, venueSerializer, tokenSerializer, photoSerializer #, openingPeriodsSerializer
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
    filter_fields = ('googleplacesId','foursquareplacesId','venueid','name', 'open_now', 'streetname', 'price_level','rating', 'city')
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

## Photo views
class PhotoDataListView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = PhotoData.objects.all()
    serializer_class = photoSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #testing [permission]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PhotoDataDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = PhotoData.objects.all()
    serializer_class = photoSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #testing [permission]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


## for test login and authenticate
# class RegistrationAPIView(APIView):
#     # Allow any user (authenticated or not) to hit this endpoint.
#     permission_classes = (AllowAny,)
#     renderer_classes = (UserJSONRenderer,)
#     serializer_class = RegistrationSerializer
#
#     def post(self, request):
#         user = request.data.get('user', {})
#
#         # The create serializer, validate serializer, save serializer pattern
#         # below is common and you will see it a lot throughout this course and
#         # your own work later on. Get familiar with it.
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class LoginAPIView(APIView):
#     permission_classes = (AllowAny,)
#     renderer_classes = (UserJSONRenderer,)
#     serializer_class = LoginSerializer
#
#     def post(self, request):
#         user = request.data.get('user', {})
#
#         # Notice here that we do not call `serializer.save()` like we did for
#         # the registration endpoint. This is because we don't actually have
#         # anything to save. Instead, the `validate` method on our serializer
#         # handles everything we need.
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     permission_classes = (IsAuthenticated,)
#     renderer_classes = (UserJSONRenderer,)
#     serializer_class = UserSerializer
#
#     def retrieve(self, request, *args, **kwargs):
#         # There is nothing to validate or save here. Instead, we just want the
#         # serializer to handle turning our `User` object into something that
#         # can be JSONified and sent to the client.
#         serializer = self.serializer_class(request.user)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def update(self, request, *args, **kwargs):
#         user_data = request.data.get('user', {})
#
#         serializer_data = {
#             'username': user_data.get('username', request.user.username),
#             'email': user_data.get('email', request.user.email),
#
#             'profile': {
#                 'bio': user_data.get('bio', request.user.profile.bio),
#                 'image': user_data.get('image', request.user.profile.image)
#             }
#         }
#
#         # Here is that serialize, validate, save pattern we talked about
#         # before.
#         serializer = self.serializer_class(
#             request.user, data=serializer_data, partial=True
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
##
