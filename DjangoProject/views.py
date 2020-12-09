from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import ContactForm, ReviewForm
from .models import Contact, Review


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'Login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'Register.html', {'form': form})


def home(request):
    return render(request, 'Home.html')


def about(request):
    return render(request, 'AboutCompany.html')


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {'form': form}
    return render(request, 'ContactUs.html', context)


def critique(request):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {'form': form}
    return render(request, 'ReviewUs.html', context)


def requests(request):
    contacts = Contact.objects.all()
    context = {'contacts': contacts}
    return render(request, 'Requests.html', context)


def responses(request):
    reviews = Review.objects.all()
    context = {'reviews': reviews}
    return render(request, 'Reviews.html', context)


def location(request):
    return render(request, 'Location.html')


def delcontact(request, id):
    name = Contact.objects.get(id=id)
    if request.method == 'POST':
        name.delete()
        return redirect('requests')
    return render(request, 'DelContact.html', {'name': name})


def upcontact(request, id):
    name = Contact.objects.get(id=id)
    form = ContactForm(request.POST or None, instance=name)
    if form.is_valid():
        form.save()
        return redirect('requests')

    context = {'name': name, 'form': form}
    return render(request, 'UpContact.html', context)


def delreview(request, id):
    name = Review.objects.get(id=id)
    if request.method == 'POST':
        name.delete()
        return redirect('responses')
    return render(request, 'DelReview.html', {'name': name})


def upreview(request, id):
    name = Review.objects.get(id=id)
    form = ReviewForm(request.POST or None, instance=name)
    if form.is_valid():
        form.save()
        return redirect('responses')

    context = {'name': name, 'form': form}
    return render(request, 'UpReview.html', context)
