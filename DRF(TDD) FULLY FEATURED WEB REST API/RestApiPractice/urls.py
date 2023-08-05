
from django.contrib import admin
from django.urls import path, include

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Rest API Project Practices (Income Expenses)",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.mbhmishu.com/policies/terms/",
      contact=openapi.Contact(email="contact@mbhmishu.local"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/',include('authentication_app.urls')),
    path('expenses/',include('expense_app.urls')),
    path('incomes/',include('income_app.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
   
]
