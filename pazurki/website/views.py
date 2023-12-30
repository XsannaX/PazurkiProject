from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Workers,Adopt_form,Animal, Connector, Adoption_history
from django.http import HttpResponseRedirect
from .forms import Add_user,Adopt, UpdateUserForm,UpdateProfileForm, AddAnimal,UserAdopt,WorkerUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .filters import AnimalFilter
from django.core.paginator import Paginator,EmptyPage


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
	form = UserAdopt(request.POST or None)
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

#usuniecie zwierzecia
def delete_animal(request, pk):

    animal_record = Animal.objects.get(id_animal=pk)
    animal_record.delete()
    messages.success(request, "Record Deleted Successfully...")
    return redirect('view_all_animals')

#dodanie zwierzecia
def add_animal(request):
    form = AddAnimal(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            add_animal = form.save()
            messages.success(request, "Record Added...")
            return redirect('home')
    return render(request, "add_animal.html", {'form':form})

#update zwierzecia
def update_animal(request, pk):
    current_record = Animal.objects.get(id_animal=pk)
    form = AddAnimal(request.POST or None, instance=current_record)
    if form.is_valid():
        form.save()
        messages.success(request, "Record Has Been Updated!")
        return redirect('home')
    return render(request, 'update_animal.html', {'form': form})

#podglad wszystkich form adopcyjnych
def view_adoption_form(request):
    adoption=Adopt_form.objects.all()
    return render(request,"view_adoption_form.html",{'records':adoption})

#konkretna forma adopcyjna
def adoption_record(request, pk):
    adoption_record=Adopt_form.objects.get(id_adopt_form=pk)
    return render(request,"adoption_record.html",{'adoption_record':adoption_record})

#update konkretnej formy adopcyjnej
def update_adoption_form(request,pk):
    current_record = Adopt_form.objects.get(id_adopt_form=pk)
    form = Adopt(request.POST or None, instance=current_record)
    if form.is_valid():
        form.save()
        messages.success(request, "Record Has Been Updated!")
        return redirect('home')
    return render(request, 'update_adoption_form.html', {'form': form})

#wyswietlanie strony psów(Animals/Dogs)
def dogs(request):
    animals = Animal.objects.filter(species='dog',status="For adoption").values()
    myFilter = AnimalFilter(request.GET,queryset=animals)
    context = {'myFilter': myFilter}
    p = Paginator(myFilter.qs,6)
    page_num=request.GET.get('page')
    page_obj=p.get_page(page_num)

    # try:
    #     page_obj=p.page(page_num)
    # except EmptyPage:
    #     page_obj=p.page(1)

    context = {'myFilter': myFilter,'page_obj':page_obj}
    return render(request, "dogs.html", context=context)

#wyswietlanie strony kotow(Animals/Cats)
def cats(request):
    animals = Animal.objects.filter(species='cat',status="For adoption").values()
    myFilter = AnimalFilter(request.GET, queryset=animals)
    context = {'myFilter': myFilter}
    p = Paginator(myFilter.qs, 6)
    page_num = request.GET.get('page')
    page_obj = p.get_page(page_num)

    # try:
    #     page_obj=p.page(page_num)
    # except EmptyPage:
    #     page_obj=p.page(1)

    context = {'myFilter': myFilter, 'page_obj': page_obj}
    return render(request, "cats.html", context=context)

#strona how to adopt(Animals/how to adopt)
def how_adopt(request):
    return render(request, "how_adopt.html")

#strona under my care(Animals/Under my care)
def under_my_care(request):
    all_animals = Connector.objects.all()

    current_worker=request.user
    worker_name = current_worker.username if current_worker else '',
    worker_name = ''.join(worker_name)
    worker_name = worker_name.replace(",", "")
    # form=WorkerUpdateForm(request.POST)
    # if form.is_valid():
    #     form.save()
    #     messages.success(request, "Record Has Been Updated!")

    #context= {'all_animals':all_animals,'form': form,'worker_name':worker_name}
    return render(request, "under_my_care.html",{'all_animals':all_animals,'worker_name':worker_name})


#wyswietlanie historii adopcjii
def adoption_history(request):
    history = Adoption_history.objects.all()
    context = {'history':history}
    return render(request, "adoption_history.html", context=context)


#wyswietlanie polaczenie pracownicy-zwierzeta(Animals/under my care)
def connector(request,pk):
    connector = Connector.objects.get(id_connector=pk)
    form = WorkerUpdateForm(request.POST or None, instance=connector)
    if form.is_valid():
        form.save()
        messages.success(request, "Record Has Been Updated!")
        return redirect('under_my_care')
    return render(request, "connector.html", {'form': form})