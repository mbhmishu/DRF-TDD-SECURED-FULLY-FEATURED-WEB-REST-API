from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Expense,ExpenseCategory
from .serializers import CreatExpenseSerial,ExpenseCategoryListCreatSirializer,ExpenseCategorySirializer
from rest_framework import permissions
from .permission import IsOwner
from rest_framework.generics import get_object_or_404


# Create your views here.


class ExpenseListCreateView(ListCreateAPIView):
    serializer_class = CreatExpenseSerial
    queryset = Expense.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    

class ExpenseDetailsView(RetrieveUpdateDestroyAPIView):
    serializer_class = CreatExpenseSerial
    queryset = Expense.objects.all()
    permission_classes = (permissions.IsAuthenticated,IsOwner)
    lookup_field = "id"

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)



class ExpCatagoriListCreat(generics.ListCreateAPIView):
    queryset = ExpenseCategory.objects.filter()
    serializer_class = ExpenseCategoryListCreatSirializer 
    permission_classes = (permissions.IsAuthenticated,IsOwner)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)






class ExpCatagoriItemList(RetrieveUpdateDestroyAPIView):
    queryset = ExpenseCategory.objects.prefetch_related("categoris").filter()
    serializer_class = ExpenseCategorySirializer
    permission_classes = (permissions.IsAuthenticated,IsOwner)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_object(self):
        catagori_id = self.kwargs.get('catagori_id', None)
        return get_object_or_404(self.queryset,id=catagori_id,owner=self.request.user)




 

class CatagoriItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.select_related("expense_set").filter()
    serializer_class = CreatExpenseSerial
    permission_classes = (permissions.IsAuthenticated,IsOwner)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_object(self):
        catagori_id = self.kwargs.get('catagori_id', None)
        expense_id = self.kwargs.get('expense_id', None)
        expense_category = get_object_or_404(ExpenseCategory.objects.filter(id=catagori_id))
        return get_object_or_404(self.queryset,category=expense_category,id=expense_id,owner=self.request.user)


   