"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path ,include
from django.conf.urls.static import static
from django.conf import settings
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contactus/',views.ContactUs.as_view(),name='contact'),
    path('busness/',views.Busnesssclass.as_view(),name='busness'),
    path('politics/',views.Politicsclass.as_view(),name='politics'),
    path('signup/',views.register_user,name='signup'),
    path('',views.Home,name='Home'),
    path('login/',views.Loginclass.as_view(),name='login'),
  
    path('logout',views.user_logout,name='logout'),
    path('accounts/',include('myapp.urls')),
    path('updatebusness/<int:pk>',views.UpdateBusness.as_view(),name='updatebusness'),
    path('updatepolitics/<int:pk>',views.UpdatePolitics.as_view(),name='updatepolitics'),
    path('deletepolitics/<int:pk>',views.DeletePolitics.as_view(),name='deletepolitics'),
    path('deletebusness/<int:id>/',views.DeleteBusness,name='deltebusness'),






]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 