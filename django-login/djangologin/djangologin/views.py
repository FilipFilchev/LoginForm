from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
# from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def success(request):
    return render(request, 'success.html', {'username': request.user.username})

def home(request):
    # return HttpResponse("Welcome to the Home Page!")
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print("About to set login success message...")
            messages.success(request, 'Hmm.. Try here!')
            print("Message set. Redirecting...")
            return redirect('success')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})

    return render(request, 'login.html')


# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             print("About to set registration success message...")
#             messages.success(request, 'Successfully registered and logged in!')
#             print("Message set. Redirecting...")
#             return redirect('home')  
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})


#manual register creation without library help


from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Check if passwords match
        if password1 == password2:
            # Check if user already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return render(request, 'register.html')
            else:
                # Create and save the user
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                auth_login(request, user)
                messages.success(request, 'Hmm.. Try here!')
                return redirect('success')
        else:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')

    return render(request, 'register.html')



