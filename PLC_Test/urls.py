"""PLC_Test URL Configuration

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
from django.conf.urls import url
from django.urls import path
from PLC_Test_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/get_data', views.get_data),
    path('api/set_data', views.set_data),
    path('api/new_test', views.new_test),
    path('testing', views.testing),
    path('test_results', views.test_results),
    path('test_delete', views.test_delete),
    path('upload', views.upload),
    url(r'^$', views.index),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
