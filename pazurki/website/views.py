from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Workers,Adopt_form,Animal
from django.http import HttpResponseRedirect
from .forms import Add_user,Adopt, UpdateUserForm,UpdateProfileForm, AddAnimal
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# home page
def home(request):
    return render(request, 'home.html',{})

#logowanie
def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in successfully!")
            return redirect('home')
        else:
            messages.success(request,"Invalid username or password! Please try again!")
            return redirect('login_user')
    return render(request, 'login_user.html', {})

#wylogowanie
def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out. See u soon;)")
    return redirect('home')

#dodaj pracownika
def add_user(request):
    form = Add_user()
    if request.method == "POST":
        form = Add_user(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            is_active = form.cleaned_data['is_active']
            is_staff = form.cleaned_data['is_staff']
            is_superuser = form.cleaned_data['is_superuser']
            # Log in user
            user = authenticate(username=username, password=password, first_name=first_name, last_name=last_name,
                                is_active=is_active, is_staff=is_staff, is_superuser=is_superuser)
            login(request, user)
            messages.success(request, ("You have successfully registered! Welcome!"))
            return redirect('home')

    return render(request, "add_user.html", {'form': form})

# def add_profile(request):
#     if request.user.is_authenticated:
#         current_user = User.objects.get(id=request.user.id)
#         profile_user = Workers.objects.get(user__id=request.user.id)
#         # Get Forms
#         user_form = Add_user(request.POST or None, request.FILES or None, instance=current_user)
#         profile_form = Add_profile(request.POST or None, request.FILES or None)
#         if user_form.is_valid():
#             user_form.save()
#             profile_form.save()
#
#             login(request,current_user)
#             messages.success(request, ("Your Profile Has Been Updated!"))
#             return redirect('home')
#
#         return render(request, "add_profile.html", {'user_form': user_form, 'profile_form':profile_form})
#     else:
#         messages.success(request, ("You Must Be Logged In To View That Page..."))
#         return redirect('home')
#update użytkownika i profilu
@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.workers)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was updated successfully')
            return redirect(to='home')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.workers)

    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})

#dodawanie wpisu w kwestionariuszu adopcyjnym
def adopt(request):
	form = Adopt(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			adopt = form.save()
			messages.success(request, "Your form was filled out successfully!")
			return redirect('home')
	return render(request, 'adopt.html', {'form':form})

#lista wszystkich zwierząt
def view_all_animals(request):
    animals=Animal.objects.all()
    return render(request,"view_all_animals.html",{'records':animals})

#pojedyncze zwierze
def animal(request, pk):
    animal_record=Animal.objects.get(id_animal=pk)
    return render(request,"animal.html",{'animal_record':animal_record})

def delete_animal(request, pk):

    animal_record = Animal.objects.get(id_animal=pk)
    animal_record.delete()
    messages.success(request, "Record Deleted Successfully...")
    return redirect('view_all_animals')

def add_animal(request):
    form = AddAnimal(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            add_animal = form.save()
            messages.success(request, "Record Added...")
            return redirect('home')
    return render(request, "add_animal.html", {'form':form})

def update_animal(request, pk):

    current_record = Animal.objects.get(id_animal=pk)
    form = AddAnimal(request.POST or None, instance=current_record)
    if form.is_valid():
        form.save()
        messages.success(request, "Record Has Been Updated!")
        return redirect('home')
    return render(request, 'update_animal.html', {'form': form})

def view_adoption_form(request):
    adoption=Adopt_form.objects.all()
    return render(request,"view_adoption_form.html",{'records':adoption})

def adoption_record(request, pk):
    adoption_record=Adopt_form.objects.get(id_adopt_form=pk)
    return render(request,"adoption_record.html",{'adoption_record':adoption_record})

def update_adoption_form(request,pk):
    current_record = Adopt_form.objects.get(id_adopt_form=pk)
    form = Adopt(request.POST or None, instance=current_record)
    if form.is_valid():
        form.save()
        messages.success(request, "Record Has Been Updated!")
        return redirect('home')
    return render(request, 'update_adoption_form.html', {'form': form})