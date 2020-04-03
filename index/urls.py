from django.urls import path
from . import views
urlpatterns = [
    path("",views.main.as_view()),
    path("posts/",views.posts.as_view()),
    path("view/<str:tit>",views.views.as_view())
]
