from django.shortcuts          import render, redirect
from django.http               import HttpResponse
from django.template           import loader
from django.contrib.auth       import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from mainapp.forms import SignUpForm


def index( request ):
    template = loader.get_template( 'index.html' )
    context  = {}
    return HttpResponse( template.render( context, request ) )

@login_required
def dashboard( request ):
    template = loader.get_template( 'gentelella/dashboard.html' )
    context  = {}
    return HttpResponse( template.render( context, request ) )

@login_required
def profile( request ):
    template = loader.get_template( 'gentelella/profile.html' )
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
