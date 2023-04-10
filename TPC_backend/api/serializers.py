from rest_framework import serializers
from users.models import Student, Alumni, Company

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


