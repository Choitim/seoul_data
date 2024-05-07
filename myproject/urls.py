"""
URL configuration for myproject project.

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
from django.urls import path
from myapp import views  # 올바른 임포트


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.search_item, name='home'),  # 홈페이지에 검색 기능을 그대로 유지
    path('search/', views.search_item, name='search_item'), # '/search/'에 대한 경로 추가
    path('', views.search_item, name='search_item'),  # 검색 기능을 위한 URL
]
