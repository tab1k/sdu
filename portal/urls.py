from django.contrib import admin
from django.urls import path, include
from portal.views import PortalIndexView, GradesView

app_name = 'portal'

urlpatterns = [
    path('', PortalIndexView.as_view(), name='home'),
    path('grades/', GradesView.as_view(), name='grades')
]
