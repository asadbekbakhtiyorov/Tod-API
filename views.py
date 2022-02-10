from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Plan
from .serializer import PlanSerializer

# Create your views here.


class PlanListAPIView(ListCreateAPIView):
    serializer_class = PlanSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        plans = Plan.objects.filter(user=self.request.user)
        return plans


# class PlanCreateAPIView(CreateAPIView):
#     queryset = Plan.objects.all()
#     serializer_class = PlanSerializer


class GetPlan(RetrieveAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer