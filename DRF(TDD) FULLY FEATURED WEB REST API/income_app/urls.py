from django.urls import path
from . import views


urlpatterns = [
    path('', views.IncomeListAPIView.as_view(), name="incomes"),
    path('<int:id>', views.IncomeDetailAPIView.as_view(), name="income"),
    path('yearly_income_source_summary', views.IncomeSummaryAPIView.as_view(), name="yearly-income-source-data"),
]