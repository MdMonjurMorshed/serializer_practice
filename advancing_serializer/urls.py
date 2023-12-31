"""
URL configuration for advancing_serializer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from advance_serilize.urls import urlpatterns_v1 as advance_serilize_v1

v1_urlpatterns=[
    path('advance-serilize/',include(advance_serilize_v1))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include([
        path('v1/',include(v1_urlpatterns))
    ]))

]
