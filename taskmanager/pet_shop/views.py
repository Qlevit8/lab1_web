from .models import Pet
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from .forms import SignUp
from django.contrib.auth import logout
from .models import User


def index(request):
    pets = Pet.objects.order_by('pet_species__species_name')
    return render(request, 'pet_shop/index.html', {'pets': pets})


def sign_up2(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/profile/')
    else:
        form = SignUp()
    return render(request, 'pet_shop/sign_up.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('/pet-shop/')


def sign_up(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        remember_me = request.POST.get('remember_me')

        user_model = get_user_model()
        existing_user = User.objects.filter(email=email).exists()
        if existing_user:
            return redirect('/pet-shop/sign-in')

        user = user_model.objects.create_user(name=name, surname=surname, email=email,
                                              password=password, gender=gender, date_of_birth=date_of_birth)
        if user:
            user.save()
            login(request, user)
            if not remember_me:
                request.session.set_expiry(0)
            return redirect('/pet-shop/profile')

    return render(request, 'pet_shop/sign_up.html')


def sign_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        print(remember_me)
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            if not remember_me:
                request.session.set_expiry(0)
            return redirect('/pet-shop/profile')
    return render(request, 'pet_shop/sign_in.html')


def about(request):
    return render(request, 'pet_shop/about.html')


def profile(request):
    if request.user.is_authenticated:
        email = request.user.email
        sex = request.user.gender
        name = request.user.name
        surname = request.user.surname
        date_of_birth = request.user.date_of_birth
        return render(request, 'pet_shop/profile.html',
                      {'name': name, 'surname': surname, 'mail': email, 'sex': sex,
                       'date_of_birth': date_of_birth})
    else:
        return render(request, 'pet_shop/profile.html',
                      {'name': 'Name', 'surname': 'surname', 'mail': "hi@gmail.com", 'sex': 'male',
                       'date_of_birth': '02.03.2000'})
