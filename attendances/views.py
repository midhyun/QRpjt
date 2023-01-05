from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from attendances.models import Attendances, AttendancesCount, GroupInfo, BelongGroup
from attendances.serializers import AttendancesSerializer, AttendancesCountSerializer, GroupInfoSerializer, BelongGroupSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
# Create your views here.
"""
generics VIEW
"""
class AttendancesList(generics.ListCreateAPIView):
    queryset = Attendances.objects.all()
    serializer_class = AttendancesSerializer


class AttendancesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendances.objects.all()
    serializer_class = AttendancesSerializer

"""
CBV VIEW
"""
# class AttendancesList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         attendances = Attendances.objects.all()
#         serializer = AttendancesSerializer(attendances, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = AttendancesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class AttendancesDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Attendances.objects.get(pk=pk)
#         except Attendances.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         attendances = self.get_object(pk)
#         serializer = AttendancesSerializer(attendances)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         attendances = self.get_object(pk)
#         serializer = AttendancesSerializer(attendances, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         attendances = self.get_object(pk)
#         attendances.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)