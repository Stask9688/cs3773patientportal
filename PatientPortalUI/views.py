from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import string
import random


# Create your views here.

def home(request):
    return render(request, 'home.html')


def send_email(email, new_password, username):
    message = "Your username and temporary password are as follows:\n\n" + \
              "Username: " + username + "\nPassword: " + new_password + "\n\n" + \
              "Be sure to change the password when you log in.\n" + \
              "If you did not request a password reset, contact the Patient Portal help line at 1-800-867-5309"
    # Create the message
    response = send_mail(
        'Password reset',
        message,
        'patientportal',
        [email],
        fail_silently=False,
    )
    return HttpResponse('%s' % response)


def randomword(length):
    return ''.join(random.choice(string.ascii_letters + string.digits + "!@#$%^&*()") for i in range(length))


def password_reset_page(request):
    return render(request, "password_reset.html")


@csrf_exempt
def reset_submit(request):
    email_exists = User.objects.filter(email=request.POST['email']).exists()
    if not email_exists:
        return render(request, "password_reset_fail.html")
    new_password = randomword(10)
    user = User.objects.get(email=request.POST['email'])
    user.set_password(new_password)
    user.save()
    send_email(request.POST['email'], new_password, user.username)

    return render(request, "password_reset_success.html")
