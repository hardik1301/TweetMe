from rest_framework import serializers

from .models import Tweet
from django.conf import settings

MAX_TWEET_LENGTH=settings.MAX_TWEET_LENGTH
TWEET_ACTION_OPTIONS=settings.TWEET_ACTION_OPTIONS

class TweetActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField() 

    def validated_action(self, value):
        value =value.lower().strip()
        if not value in TWEET_ACTION_OPTIONS:
            raise serializers.ValidationError("This is not a valid action for tweet")
        return value

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tweet
        fields=['content']

    def validate_content(self,value):

        if len(value) > MAX_TWEET_LENGTH:
            raise serializers.ValidationError("This tweet is too long")
        return value

    
