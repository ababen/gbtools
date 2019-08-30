"""gbtools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from expenses import views

urlpatterns = [
    path('', views.ExpenseList.as_view(), name='expenses_list'),
    path('expenses/<int:pk>', views.ExpenseDetail.as_view(), name='expenses_detail'),
    # path('create/', views.ExpenseCreate.as_view(), name='expenses_create'),
    path('create/', views.create, name='expenses_create'),
    path('update/<int:pk>', views.ExpenseUpdate.as_view(), name='expenses_update'),
    path('delete/<int:pk>', views.ExpenseDelete.as_view(), name='expenses_delete'),
    path('download', views.download, name='download'),
    path('admin/', admin.site.urls),
]
