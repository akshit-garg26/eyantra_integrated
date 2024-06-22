from django.urls import path # we gonna define path to different web pages
from . import views

# we can determine which path we have to go based on the path user types in.
urlpatterns = [
    path("india",views.indiaMap,name="indiaMap"),
    path("indiaLobby",views.indiaLobby,name="indiaLobby"),
    path("ok",views.ok,name="ok"),
]