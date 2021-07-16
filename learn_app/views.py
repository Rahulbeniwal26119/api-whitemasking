from django.db.models import query
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
import requests
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import DullAPI, BlockList
from .serializers import DullSerializer, BlockListSerializer
from rest_framework import status


@login_required
def product_detail(request, pk):
    product = get_object_or_404(DullView, pk=pk)
    return render("Allowed")


class BlocklistPermission(permissions.BasePermission):
    """
        Global permission check for blocked apis 
    """

    def has_permission(self, request, view):
        ip_addr = request.META["REMOTE_ADDR"]
        blocked = BlockList.objects.filter(ip_address=ip_addr).exists()
        return not blocked


class DullView(generics.ListCreateAPIView):

    queryset = DullAPI.objects.all()
    serializer_class = DullSerializer
    # permission_classes = [BlocklistPermission]

    def get(self, request, format=None):
        print(self.get_queryset())
        ip_addr = request.META["REMOTE_ADDR"]
        blocked = BlockList.objects.filter(ip_address=ip_addr).exists()
        if blocked:
            return Response("ip {}  not allowed".format(ip_addr), status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(self.serializer_class(DullAPI.objects.all(), many=True).data)


class GetAnotherApiData(APIView):
    # serializer_class = DullSerializer

    def get(self, request, format=None):

        r = requests.get('http://www.localhost:8001/')

        return Response(r.json())
