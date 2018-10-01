from rest_framework import serializers
from restapi.models import ApiData, UseraccountData, VenueData, TokenData, ActivityData, VenueTypeData, MenuData
from restapi.models import StartPrice, Mood, TimePhase, OpenHours #, OpeningPeriods
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
    #Test
    venue_start_price = serializers.StringRelatedField(many=True)
    venue_opening_periods = serializers.StringRelatedField(many=True)
    venue_moods = serializers.StringRelatedField(many=True)
    # venue_name = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='menu'
    #  )
    #venuephoto = serializers.StringRelatedField(many=True)
    # venuephoto = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='photo-detail'
    # )
    ###
    class Meta:
        model = VenueData
        fields = '__all__'


class tokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenData
        fields = '__all__'


# class photoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PhotoData
#         fields = '__all__'


class activitydataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityData
        fields = '__all__'


class venuetypedataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenueTypeData
        fields = '__all__'

class menudataSerializer(serializers.ModelSerializer):
    menu_item = serializers.StringRelatedField(many=True)
    class Meta:
        model = MenuData
        fields = '__all__'

class startpriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartPrice
        fields = '__all__'


class timephaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimePhase
        fields = '__all__'

class moodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = '__all__'

class openhoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenHours
        fields = '__all__'
