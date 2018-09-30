from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import ast


# renders the landing page of the application
def index(request):
    # get all the users
    users = User.objects.all()
    context = {
        "users": users
    }
    return render(request, "first_app/index.html", context)


# renders a page that provides options for getting coffee or lunch
def success(request):
    if "id" in request.session:
        return render(request, "first_app/success.html")
    return redirect("/")


# this function sends all the existing users to the success page
def successId(request):
    if request.method == "POST":
        userID = request.POST['userList']
        user = User.objects.get(id=userID)
        request.session['first_name'] = user.first_name
        request.session['last_name'] = user.last_name
        request.session['id'] = user.id
        return redirect('/success')
    return redirect('/')


# this function creates a new user
def registration(request):
    if request.method == "POST":
        result = User.objects.registration(request)
        if result[0] == False:
            for error in result[1]:
                messages.add_message(request, messages.INFO, error)
        else:
            user = User.objects.get(id=result[1].id)
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            request.session['id'] = user.id
            return redirect("/success")
    return redirect("/")


# this function generates random colleague for coffee
def getCoffee(request):
    if "id" in request.session:
        userList = User.objects.exclude(id=request.session['id'])
        if (len(userList) < 1):
            error = "Wait for others to join the system"
            messages.add_message(request, messages.INFO, error)
        else:
            generateCoffeeFriend = User.objects.getCoffee(request.session['id'])
            if generateCoffeeFriend[0] == True:
                coffeeFriend = User.objects.get(id=generateCoffeeFriend[1])
                context = {
                    "coffee_friend": coffeeFriend
                }
                return render(request, "first_app/coffeeFriend.html", context)
            else: 
                messages.add_message(request, messages.INFO, generateCoffeeFriend[1][0])
        return redirect('/success')
    return redirect("/")


# this function generates 3-5 colleague for lunch
def getLunch(request):
    if "id" in request.session:
        min_friend_number = 2
        max_friend_number = 4
        lunchFriends = User.objects.getLunch(request.session['id'], min_friend_number, max_friend_number)
        if lunchFriends[0] == False:
            error = lunchFriends[1]
            messages.add_message(request, messages.INFO, error)
        else:
            context = {
                "lunch_friends": lunchFriends[1]
            }
            return render(request, "first_app/lunchFriends.html", context)
        return redirect('/success')
    return redirect("/")


# this removes the current user from the session
def resetUser(request):
    if 'first_name' in request.session:
        request.session.pop('first_name')
        request.session.pop('last_name')
        request.session.pop('id')
    return redirect("/")

