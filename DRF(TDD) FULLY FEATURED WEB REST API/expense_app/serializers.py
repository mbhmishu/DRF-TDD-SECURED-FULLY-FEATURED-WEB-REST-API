from rest_framework import serializers
from .models import Expense,ExpenseCategory




class CreatExpenseSerial(serializers.ModelSerializer):
    category = serializers.CharField(source='category.catagory_name', read_only=True)
    
    class Meta:
        model = Expense
        fields = ('id', 'amount', 'category','description','owner','expens_date','created_at','updated_at')
        read_only_fields = ('id','owner','created_at','updated_at')

    def create(self, validated_data):
        category_name = validated_data.pop('category', '')
        owner = validated_data.get('owner','')
        category, _ = ExpenseCategory.objects.get_or_create(catagory_name=category_name,owner=owner)
        expense = Expense.objects.create(**validated_data, category=category)
        return expense



class ExpenseListSerial(serializers.ModelSerializer):
    
    class Meta:
        model = Expense
        fields = ('id', 'amount','description','owner','expens_date','created_at','updated_at')
        read_only_fields = ('id','owner','created_at','updated_at')



class ExpenseCategorySirializer(serializers.ModelSerializer):

    categoris = ExpenseListSerial(many=True, read_only=True)

    class Meta:
        model =ExpenseCategory
        fields = '__all__'
        read_only_fields = ('id','Created','updated','categoris')


class ExpenseCategoryListCreatSirializer(serializers.ModelSerializer):

    class Meta:
        model =ExpenseCategory
        fields = '__all__'
        read_only_fields = ('id','Created','updated','total_expenses','owner')



    
