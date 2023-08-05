from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import IncomeSerializer
from .models import Income
from rest_framework import permissions, views,status 
from rest_framework.response import Response
from expense_app.permission import IsOwner
import datetime

class IncomeListAPIView(ListCreateAPIView):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class IncomeDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = IncomeSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Income.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)



class IncomeSummaryAPIView(views.APIView):

    def get_source(self,income):
        return income.source
    
    def get_amount_for_incomesource(self,income_list,source):
        income = income_list.filter(source=source)
        amount =0

        for income in income:
            amoun += income.amount
        return { 'amount':str(amount)}
    

    def get(self, request):
        todays_date = datetime.date.today()
        ayear_ago =todays_date - datetime.timedelta(days=30*12)
        income = Income.objects.filter(owner=request.user, date__gte=ayear_ago,date__lte=todays_date)
       
        final = {}
        sources = list(set(map(self.get_source, income)))

        for i in income:
            for source in sources:
                final[source] = self.get_amount_for_incomesource(income,source)


        return Response({'income_source_data':final}, status=status.HTTP_200_OK)



