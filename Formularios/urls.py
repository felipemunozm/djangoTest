from django.urls import path

from . import views
app_name = 'formulario'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_pregunta>/',views.detalle, name='detalle'),
    path('<int:id_pregunta>/resultados/',views.resultado, name='resultados'),
    path('<int:id_pregunta>/votar/',views.votar, name='votar'),
]
