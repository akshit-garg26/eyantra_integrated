from django.urls import path 
from . import views
urlpatterns = [
    path('', views.index, name='index_symposium'),
    path('model/<slug:pk>', views.model, name='model'),
    path('exhibition', views.exhibition, name='exhibition'),
    path('lobby', views.lobby, name='lobby'),
    # path('upload', views.upload_model, name='upload'),
    # path('editModel/<int:entry_id>', views.edit_model, name='editModel'),
    # path('editPage', views.edit_page, name='editPage'),
    path('modelPage/<slug:pk>', views.model_page, name='model_page'),
    path("ok",views.ok,name="ok")
]
