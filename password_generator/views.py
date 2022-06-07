from django.http import HttpResponse


def password_generator(request, password_lenght: int = 100):
    return HttpResponse("Hello, world. You're at the polls index.")
