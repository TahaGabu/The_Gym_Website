from rest_framework import serializers
from gymApp.models import gym

#Creating Serializers 
class gymSerializer(serializers.ModelSerializer):
    class Meta:
        model = gym
        fields= "__all__"