from django.shortcuts import render
from django.http import HttpResponse
from .models import students
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StudentsSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def get_students(request):
    if request.method == 'GET':
        students_list = students.objects.all()
        serializer = StudentsSerializer(students_list, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def create_student(request):
    serializer = StudentsSerializer(data=request.data)
    if request.method == 'POST':
        name = request.data.get('name')
        roll = request.data.get('roll')
        email = request.data.get('email')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_student(request, pk):
    try:
        student = students.objects.get(pk=pk)
    except students.DoesNotExist:
        return HttpResponse(status=404)
    student.delete()
    return HttpResponse(status=204)


@api_view(['PUT'])
def update_student(request, pk):
    try:
        student = students.objects.get(pk=pk)
    except students.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'PUT':
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)