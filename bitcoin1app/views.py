from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .serializers import BitcoinSerializer
from .models import Bitcoin
from rest_framework import viewsets

class BitcoinViewSet(viewsets.ViewSet):
    def list(self, request):
        bitcoin = Bitcoin.objects.all()
        serializer = BitcoinSerializer(bitcoin, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BitcoinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        try:
            course =Bitcoin.objects.get(pk=pk)
        except Bitcoin.DoesNotExist:
            raise NotFound("Bitcoin not found")
        serializer = BitcoinSerializer(course)
        return Response(serializer.data)

    def update(self, request, pk):
        try:
            course = Bitcoin.objects.get(pk=pk)
        except Bitcoin.DoesNotExist:
            raise NotFound("Bitcoin not found")
        serializer = BitcoinSerializer(course, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk):
        try:
            course = Bitcoin.objects.get(pk=pk)
        except Bitcoin.DoesNotExist:
            raise NotFound("Bitcoin not found")
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
