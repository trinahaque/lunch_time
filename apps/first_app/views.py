from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import ast


def index(request):
    # get all the users
    users = User.objects.all()
    # print "users", users
    context = {
        "users": users
    }
    return render(request, "first_app/index.html", context)

def success(request):
    return render(request, "first_app/success.html")

def successId(request):
    if request.method == "POST":
        userID = request.POST['userList']
        user = User.objects.get(id=userID)
        request.session['first_name'] = user.first_name
        request.session['id'] = user.id
        return redirect('/success')
    return redirect('/')

def registration(request):
    if request.method == "POST":
        result = User.objects.registration(request)
        if result[0] == False:
            for error in result[1]:
                messages.add_message(request, messages.INFO, error)
        else:
            user = User.objects.get(id=result[1].id)
            request.session['first_name'] = user.first_name
            request.session['id'] = user.id
            return redirect("/success")
    return redirect("/")

def getCoffee(request):
    if "id" in request.session:
        userList = User.objects.exclude(id=request.session['id'])
        if (len(userList) < 1):
            request.session['message'] = "Wait for others to join the system"
        else:
            newCoffeeFriend = User.objects.getCoffee(request.session['id'])
            if newCoffeeFriend[0] == True:
                coffeeFriend = User.objects.get(id=newCoffeeFriend[1])
                request.session['coffee_friend_first_name'] = coffeeFriend.first_name
                request.session['coffee_friend_last_name'] = coffeeFriend.last_name
        return redirect('/success')
    return redirect("/")

def getLunch(request):
    if "id" in request.session:
        return redirect('/success')
    return redirect('/')

def resetUser(request):
    if 'first_name' in request.session:
        request.session.pop('first_name')
        request.session.pop('id')
    return redirect("/")

