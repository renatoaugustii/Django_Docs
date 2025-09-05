from django.urls import path
from . import views, htmx_views

app_name = 'app_webdoc'

urlpatterns = [

     path('', views.webdoc, name="documentation"),  

]


htmx_urlpatterns = [
   #Inserir aqui as urls do htmx
]

urlpatterns += htmx_urlpatterns