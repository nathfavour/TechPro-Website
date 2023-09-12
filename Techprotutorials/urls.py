from django.contrib import admin
from django.urls import path, include
from Frontend import views

urlpatterns = [
    path('api/', include('Frontend.urls')),
    path('submit_kyc/', views.submit_kyc, name='submit_kyc'),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('apply/', views.apply, name='apply'),
    path('kyc/', views.kyc, name='kyc'),
]
