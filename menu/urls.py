from django.urls import path

from menu import views

app_name = 'menu'

urlpatterns = [
    path(
        'generate_password',
        views.generate_password_template,
        name='generate_password'
    )
]
