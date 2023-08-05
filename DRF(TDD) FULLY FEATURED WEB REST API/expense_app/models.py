from django.db import models
from authentication_app.models import User
from django.db.models import Sum

# Create your models here.

class ExpenseCategory(models.Model):
    catagory_name = models.CharField(max_length=255 )
    description = models.TextField(blank=True,null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses_category')
    Created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def total_expenses(self):
        # Using Django's aggregation function 'Sum' to calculate the total expenses for this category
        total_expenses = self.categoris.aggregate(total_expenses=Sum('amount'))['total_expenses']
        return total_expenses or 0
    

    def __str__(self):
        return f"{self.catagory_name}'\n {self.total_expenses}"
    
    

    

class Expense(models.Model):
    category = models.ForeignKey(ExpenseCategory,on_delete=models.CASCADE,related_name='categoris')
    amount = models.DecimalField(max_digits=10, decimal_places=2, max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    expens_date = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering: ['-updated_at']

    def __str__(self):
        return str(self.owner)+'s expense'
    
    @property
    def category_name(self):
        return self.category.catagory_name
    





    