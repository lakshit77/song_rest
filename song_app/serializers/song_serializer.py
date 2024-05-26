from rest_framework import serializers
from song_app.models import Song
from song_app.status_code import rating_validation
from song_app.consts import MESSAGE
from django.core.validators import MinValueValidator, MaxValueValidator

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"


class PartialUpdateSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    def validate_rating(self, value):
        if value < 0 or value > 5:
            raise serializers.ValidationError(rating_validation[MESSAGE])
        return value
    class Meta:
        model = Song
        fields = ['rating']
