from django.conf.urls import url

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from authentication.views import LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView


urlpatterns = [
    url(r'^get-token/', obtain_jwt_token), #login users to get token
    url(r'^token-refresh/', refresh_jwt_token),
    url(r'^token-verify/', verify_jwt_token),
    ######
    url(r'^user/?$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^user/register/?$', RegistrationAPIView.as_view()),


    url(r'^user/login/?$', LoginAPIView.as_view()), #this may not be important
]
