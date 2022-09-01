from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser

# from rest_framework import permissions

# Create your views here
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
def hello_world(request, pk=None):
    if request.method == 'GET':
        print("\n<<<<<<<<<<<<<<<<<<<<<<<<<GET>>>>>>>>>>>>>>>>>>>>>>>>")
        # id=request.data.get('id') #Here we are getting directly parsed data from //request.deta//. This is the beauty of //@api_view// decorator
        id=pk #We have to write //id=request.data.get('id')// if we not use //pk// in GET, PUT, PATCH and DELETE
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)

        stu=Student.objects.all()
        serializer=StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    if request.method == 'POST':
        print("\n<<<<<<<<<<<<<<<<<<<<<<<<<POST>>>>>>>>>>>>>>>>>>>>>>>>")
        serializer=StudentSerializer(data=request.data) #We have all data in //request.data//
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data inserted successfully!!!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)


    if request.method == 'PUT':
        print("\n<<<<<<<<<<<<<<<<<<<<<<<<<PUT>>>>>>>>>>>>>>>>>>>>>>>>>>")
        # id=pk #We have to write //id=request.data.get('id')// if we not use //pk// in GET, PUT, PATCH and DELETE
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data updated successfully!!!'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


    if request.method == 'PATCH':
        print("\n<<<<<<<<<<<<<<<<<<<<<<<<<PATCH>>>>>>>>>>>>>>>>>>>>>>>>>>")
        id=pk #We have to write //id=request.data.get('id')// if we not use //pk// in GET, PUT, PATCH and DELETE
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data updated successfully(partially)!!!'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


    if request.method =='DELETE':
        print("\n<<<<<<<<<<<<<<<<<<<<<<<<<DELETE>>>>>>>>>>>>>>>>>>>>>>>>>>")
        id=pk #We have to write //id=request.data.get('id')// if we not use //pk// in GET, PUT, PATCH and DELETE
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg' : 'Data deleted successfully!!!'}, status=status.HTTP_200_OK)





# from ast import Return
# from urllib import response
# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# Create your views here.
# @api_view()  #//@api_view()// and //@api_view(['GET'])// both are same
# def hello_world(request):
#     return Response({'msg' : 'Hii this is Anand!!'})

# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg' : 'Hii this is Anand!!'})

# @api_view(['GET','POST'])
# def hello_world(request):
#     if request.method == 'GET':
#         return Response({'msg' : 'This is from GET request!!'})
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg' : 'This is from POST request!!', 'data' : request.data}) #//'data' : request.data// is written to see the requested data