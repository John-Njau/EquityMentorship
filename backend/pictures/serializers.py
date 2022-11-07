# import serializers
from rest_framework import serializers

from .models import Picture

from cloudinary.models import CloudinaryField

class PictureSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    image = CloudinaryField('2022 Mentorship Pictures')

    def create(self, validated_data):
        return Picture.objects.create(**validated_data)