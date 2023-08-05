
from django.urls import path
from .import views

    

urlpatterns = [
    path('', views.ExpenseListCreateView.as_view(), name='expenses'),
    path('<int:id>',views.ExpenseDetailsView.as_view(),name='expense_details'),

    path('catagori/',views.ExpCatagoriListCreat.as_view(),name='expense_catagori_list'),
    path('catagori/<int:catagori_id>/',views.ExpCatagoriItemList.as_view(),name='expense_item_list'),
    path('catagori/<int:catagori_id>/<int:expense_id>',views.CatagoriItemDetail.as_view(),name='expense_item_list'),
    
]
