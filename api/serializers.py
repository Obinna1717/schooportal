from rest_framework import serializers
from accounts.models import Student
from accounts.models import Lecturer
from payments.models import SchoolFee
from results.models import Result
from courses.models import Course


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
        

class SchoolFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolFee
        fields = '__all__'        