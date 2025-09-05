from django.urls import path
from . import views, htmx_views

app_name = 'app_home'

urlpatterns = [

    path('',views.home, name="home"),

]


htmx_urlpatterns = [
   #Inserir aqui as urls do htmx
]

urlpatterns += htmx_urlpatterns