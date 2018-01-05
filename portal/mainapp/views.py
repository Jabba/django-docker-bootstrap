from django.shortcuts          import render, redirect
from django.http               import HttpResponse
from django.template           import loader
from django.contrib.auth       import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from mainapp.forms import SignUpForm


def index( request ):
    template = loader.get_template( 'index.html' )
    context  = {}
    return HttpResponse( template.render( context, request ) )

def dashboard( request ):
    template = loader.get_template( 'dashboard.html' )
    context  = {}
    return HttpResponse( template.render( context, request ) )

def signup( request ):
    if request.method == 'POST':
        form = SignUpForm( request.POST )
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get( 'username' )
            raw_password = form.cleaned_data.get( 'password1' )
            user = authenticate( username = username, password = raw_password )
            login( request, user )
            return redirect( '/login' )
    else:
        form = SignUpForm()
    return render( request, 'signup.html', { 'form': form } )
