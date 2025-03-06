from .serializers import FarmDataSerializer, FarmDataRetrieveSerializer
from .models import FarmData
from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.

class CreateFarmDataView(CreateAPIView):
    permission_classes = []
    serializer_class = FarmDataSerializer
    queryset = FarmData.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:

            if serializer.is_valid():
                self.perform_create(serializer)

                data = {
                    "message": "Farm Data Uploaded Successfully",
                    "data": serializer.data,
                }

                return Response(data, status=status.HTTP_201_CREATED)

            return Response(
                {
                    "message": "Failed to upload Farm Data, Validation error occurred.",
                    "error": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            return Response(
                {
                    "message": "Failed to upload Farm Data. Exception error occurred",
                    "error": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class GetAllFarmDatas(ListAPIView):
    permission_classes = []
    serializer_class = FarmDataRetrieveSerializer
    queryset = FarmData.objects.all()

class FarmDataReadUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = []
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = FarmDataRetrieveSerializer
    queryset = FarmData.objects.all()