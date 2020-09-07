from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from .models import Account

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        # test if the test cookie workedi
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()

            # Log user in

            query = Account.objects.get(name=request.POST['username'])
            # make sure user exists
            if not query:
                return HttpResponse("Username is wrong")

            # password auth
            if not check_password(request.POST['password'], query.passhash):
                return HttpResponse("Password is wrong")

            # set session vars
            request.session['id'] = query.id
            request.session['score'] = query.score
            request.session['username'] = query.name



            return redirect('/')
        else:
            return HttpResponse("Please enable cookies and try again.")

    request.session.set_test_cookie()

    return render(request, 'login.html')


def logout(request):
    try:
        del request.session['id']
        del request.session['score']
        del request.session['username']
    except KeyError:
        pass
    return redirect('/')


def register(request):
    if request.method == 'POST':
        # get vars
        name = request.POST['username']
        password = request.POST['password']

        # abort if they are bad inputs
        if not (name and password):
            return HttpResponse("Input is Invalid")

        # abort if account exists
        query = Account.objects.filter(name=request.POST['username'])
        if len(query) > 0:
            return HttpResponse("Account already exists")

        # hash it
        hash = make_password(password, salt=None, hasher='default')

        # chash it
        Account.objects.create(name=name, passhash=hash, score=0)

        # push it by salt and peppa
        return redirect('/')

    else:
        return render(request, 'register.html')
