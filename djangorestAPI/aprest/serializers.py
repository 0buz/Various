from rest_framework import serializers
from .models import Aprest, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


#Aprest Serializer class uses our model and outputs the table fields ==========
class AprestSerializer(serializers.HyperlinkedModelSerializer):    #updated from serializers.ModelSerializer
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='aprest-highlight', format='html')

    class Meta:
        model = Aprest
        fields = ('url','id', 'highlight','title', 'code', 'linenos', 'language', 'style', 'owner')   #added 'url', 'highlight' fields


class UserSerializer(serializers.HyperlinkedModelSerializer):     #updated from serializers.ModelSerializer
    #aprests = serializers.PrimaryKeyRelatedField(many=True, queryset=Aprest.objects.all())
    aprests = serializers.HyperlinkedRelatedField(many=True, view_name='aprest-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url','id','username','aprests')   #added 'url' field






