from django.shortcuts import render, redirect, reverse
import bcrypt
from .models import User, Poke

#Get Current User
def get_current_user(request):
    session_id = request.session['user_id']

    current_user = User.objects.get(id=session_id)

    return current_user

#Render Landing Page
def index(request):
    print "Inside the index method"

    return render(request, 'pokes_app/index.html')

#Render Success Page
def success(request):
    print "Inside the success method."

    if 'user_id' in request.session:
        current_user = get_current_user(request)

        pokes = len(current_user.poked.all())
        friends = current_user.friends.all()
        exclude_ids = list(friends.values_list('id', flat=True))
        exclude_ids.append(current_user.id)

        users = User.objects.exclude(id__in=exclude_ids)

        context = {
            'current_user': current_user,
            'users': users,
            'friends': friends,
            'pokes': pokes,
        }

        return render(request, 'pokes_app/success.html', context)

    return redirect(reverse('landing'))

#Render Removal Confirmation Page
def confirm_remove(request, id):
    print "Inside the confirm_remove method."

    if 'user_id' in request.session:
        friend = User.objects.get(id=id)

        context = {
            'friend': friend
        }

        return render(request, 'pokes_app/confirm_remove.html', context)

    return redirect(reverse('success'))

#Add Friend to current user
def add_friend(request, id):
    print "Inside the add_friend method."

    if request.method == "POST":
        current_user = get_current_user(request)
        user = User.objects.get(id=id)

        current_user.friends.add(user)

    return redirect(reverse('success'))

#Remove Friend from current user
def remove_friend(request, id):
    print "Inside the remove_friend method."

    if request.method == "POST":
        current_user = get_current_user(request)
        user = User.objects.get(id=id)

        current_user.friends.remove(user)

        print current_user.friends.all()

    return redirect(reverse('success'))

#Current user pokes another user
def poke(request, id):
    print "Inside the poke method."

    if request.method == "POST":
        current_user = get_current_user(request)
        user = User.objects.get(id=id)

        poke = Poke.objects.create(poker=current_user, pokee=user)

    return redirect(reverse('success'))

#Reset current user's poke counts
def reset_pokes(request):
    print "Inside the reset_pokes method."

    if request.method == "POST":
        current_user = get_current_user(request)

        current_user.poked.all().delete()

    return redirect(reverse('success'))

#Logout current user
def logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id')

    return redirect(reverse('landing'))
    
def create(request):
    print "Inside the create method"

    if request.method == "POST":
        form_data = request.POST

        errors = User.objects.validate(form_data)

        #If form_data has no errors
        if not errors:
            password = str(form_data['password'])
            hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())

            user = User.objects.create(
                first_name = form_data['first_name'],
                last_name = form_data['last_name'],
                email = form_data['email'],
                password = hashed_pw
            )

            request.session['user_id'] = user.id

            return redirect(reverse('success'))

        print errors

    return redirect(reverse('landing'))

#Login a user
def login(request):
    print "Inside the login method."

    if request.method == "POST":
        form_data = request.POST

        check = User.objects.login(form_data)

        if type(check) == type(User()):
            request.session['user_id'] = check.id
            return redirect(reverse('success'))

        print check

    return redirect(reverse('landing'))