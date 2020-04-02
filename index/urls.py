from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    path("posts/",views.post),
    path("view/<str:tit>",views.view)
]