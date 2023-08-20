from django.urls import path
from . import views

app_name = 'importer'
urlpatterns = [
    path('', views.importerInfo, name='importerSelection'),
    path('contact/<int:id>/', views.contactView, name = 'contact'),
    path('infosub1/<int:id>/', views.infosub1, name='infosub1'),
    path('infosub2/<int:id>/', views.infosub2, name='infosub2'),
    path('send-email/', views.sendEmail, name='sendEmail'),
]