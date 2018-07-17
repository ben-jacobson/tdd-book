from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages
from accounts.models import Token
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib import auth, messages
#from django.contrib.auth import login as auth_login, logout as auth_logout
#import uuid

def send_login_email(request):
    to_email = request.POST['email']
    from_email = getattr(settings, "EMAIL_HOST_USER", None)        # this is how you access variables from Settings.py
    email_auth_user = from_email
    email_auth_pass = getattr(settings, "EMAIL_HOST_PASSWORD", None)

    token = Token.objects.create(email=to_email)
    url = request.build_absolute_uri( 
        reverse('login') + '?token=' + str(token.uid)
    )    

    send_mail(
        'Your login link for Superlists',
        f'Use this link to log in:\n\n{url}',
        from_email,
        [to_email],
        auth_user=email_auth_user,
        auth_password=email_auth_pass,
    )

    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )
    
    return redirect('/')


'''def login(request):
    print('login view', file=sys.stderr)
    uid = request.GET.get('uid')
    user = authenticate(uid=uid)
    if user is not None:
        auth_login(request, user)
    return redirect('/')'''

def login(request):
    user = auth.authenticate(uid=request.GET.get('token'))
    if user:
        auth.login(request, user)
    return redirect('/')





