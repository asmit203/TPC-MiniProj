from rest_framework import serializers
from users.models import Student, Credits

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('email', 'password')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('roll_no','name', 'email', 'password')


class PostViewSetSerializer(serializers.ModelSerializer):

    def create(self, validated_data,roll):
        # document = validated_data.get('document')  # read validated data
        post = Student.objects.filter(roll_no=roll).create(**validated_data)  # saving post object
        return post

    class Meta:
        model = Student
        fields = 'resume'
