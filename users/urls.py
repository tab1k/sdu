from django.urls import path
from users.views import SignInView

app_name = 'users'

urlpatterns = [
    path('', SignInView.as_view(), name='signin'),
]