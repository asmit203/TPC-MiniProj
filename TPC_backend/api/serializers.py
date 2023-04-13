from rest_framework import serializers
from users.models import Student, Alumni, Company

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('email', 'password')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('roll_no','name', 'email', 'password')
