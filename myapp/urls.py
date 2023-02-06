from django.urls import path
from myapp import views
urlpatterns = [
    path('profile/',views.Profile),
    path('busnessnews/',views.Busnesshome,name='busnesshome'),
    path("politicsnews/",views.PoliticsHome,name='politicshome'),
    path("BusnessDetail/<slug:slug>",views.BusnessDetail.as_view(), name="busnessdetail"),
    path("PoliticsDetail/<slug:slug>",views.PoliticsDetail.as_view(), name="PoliticsDetail"),
    path('busnessedit/',views.Business_edit,name='busness_edit'),
    path('politics_edit/',views.Politics_edit,name='politics_edit'),



]
