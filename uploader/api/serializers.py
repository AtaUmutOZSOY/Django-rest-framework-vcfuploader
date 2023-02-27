from rest_framework import serializers
from uploader.models import VcfFile

class VcfFileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField()
    document = serializers.FileField()
    uploaded_at = serializers.DateTimeField()

    def create(self, validated_data):
        print(validated_data)
        return VcfFile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        