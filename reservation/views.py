from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Reservation
from .serializers import ReservationSerializer

from datetime import datetime
# Create your views here.

def copy_request_data(data):
    req_data = {}

    print(data)
    for key, value in data.items():
        req_data[key] = value

    return req_data

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        req_data = copy_request_data(request.data)

        end_time_str = request.data.get('end_time')
        end_time_obj = datetime.strptime(end_time_str, '%H:%M')
        end_time_formatted = end_time_obj.strftime('%H:%M:%S')

        start_time_str = request.data.get('start_time')
        start_time_obj = datetime.strptime(start_time_str, '%H:%M')
        start_time_formatted = start_time_obj.strftime('%H:%M:%S')

        #예약한 시간에 다시 예약할려하면 예외처리

        req_data["start_time"] = start_time_formatted
        req_data["end_time"] = end_time_formatted

        serializer = self.get_serializer(data=req_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def list(self, request, *args, **kwargs):
        queryset = Reservation.objects.filter(building=request.query_params.get('building'), floor=request.query_params.get('floor'), day=request.query_params.get('day'), month=request.query_params.get('month'), year=request.query_params.get('year'), room=request.query_params.get('room'))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
