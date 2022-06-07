from rest_framework import serializers

from .models import students

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = ('id','name','roll','email')

    def create(self, validated_data):
        return students.objects.create(**validated_data)


