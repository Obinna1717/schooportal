from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from courses.models import Course
from courses.serializers import CourseSerializer

from payments.models import SchoolFee
from results.models import Result

from accounts.models import Student, Lecturer
from api.serializers import ResultSerializer, SchoolFeeSerializer, StudentSerializer, LecturerSerializer


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseCreateAPIView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseUpdateAPIView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDeleteAPIView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class LecturerListAPIView(generics.ListAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    
class ResultListAPIView(generics.ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    
class PaymentListAPIView(generics.ListAPIView):
    queryset = SchoolFee.objects.all()
    serializer_class = SchoolFeeSerializer    
    