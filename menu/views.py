from django.shortcuts import render


def generate_password_template(request):
    return render(request, 'menu/generate_password.html')
