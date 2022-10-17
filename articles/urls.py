from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path("update/<int:_pk>", views.update, name="update"),
    path("detail/<int:_pk>", views.detail, name="detail"),
    path("delete/<int:_pk>", views.delete, name="delete"),
    path('create', views.create, name='create'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)