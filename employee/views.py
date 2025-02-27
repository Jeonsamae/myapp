from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.response import Response
from rest_framework import status

class EmployeeView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)

        return Response(status=status.HTTP_200_OK, data=serializer.data)