from rest_framework import serializers
from restapi.models import ApiData, UseraccountData, VenueData, TokenData, PhotoData #, OpeningPeriods
from django.contrib.auth.models import User

#### apiSerializer, useraccountSerializer
class apiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiData
        fields = ('pk', 'apikey', 'apVersion', 'created',)


class useraccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UseraccountData
        fields = ('pk', 'fullname','email','password','phonenumber', 'created',)

#new
class venueSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenueData
        fields = '__all__'


class tokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenData
        fields = '__all__'


class photoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoData
        fields = '__all__'
