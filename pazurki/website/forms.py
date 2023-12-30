from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Workers, Adopt_form, Animal, Connector

GENDER_CHOICES = (
            ('', 'Gender'),
            ('Male', 'Male'),
            ('Female', 'Female'),
         )
BOOL_YN = (
        ('', '-----'),
        (True, 'Yes'),
        (False, 'No')
    )
SIZE_CHOICES=(
        ('', 'Size'),
        ('Small','Small'),
        ('Medium','Medium'),
        ('Big','Big'),
    )
SPECIES_CHOICES=(
        ('', 'Species'),
        ('Cat','Cat'),
        ('Dog','Dog'),
    )
STATUS_CHOICES=(
        ('', 'Status'),
        ('For adoption','For adoption'),
        ('Not available','Not available'),
    )

# class Add_profile(forms.ModelForm):
#     sex = forms.ChoiceField(label="", choices=GENDER_CHOICES,
#                             widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Sex'}))
#
#     class Meta:
#         model = Workers
#         fields = ['sex']

#dodawanie pracownika
class Add_user(UserCreationForm):

    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}))
    is_staff=forms.ChoiceField(label="Is staff",choices=BOOL_YN, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Staff'}))
    is_active=forms.ChoiceField(label="Is active",choices=BOOL_YN, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Active'}))
    is_superuser=forms.ChoiceField(label="Is superuser",choices=BOOL_YN, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Superuser'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'password1', 'password2','is_staff','is_active','is_superuser']

    def __init__(self, *args, **kwargs):
        super(Add_user, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


#pracownik może edytować podstawowe dane
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'}))
    first_name = forms.CharField(label="", max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    last_name = forms.CharField(label="", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}))
    is_staff=forms.ChoiceField(label="Is staff",choices=BOOL_YN, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Staff'}))
    is_active = forms.ChoiceField(label="Is active", choices=BOOL_YN,
                                  widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Active'}))
    is_superuser = forms.ChoiceField(label="Is superuser", choices=BOOL_YN,
                                     widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Superuser'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','is_staff','is_active','is_superuser']

#pracownik może edytować swój profil
class UpdateProfileForm(forms.ModelForm):
    sex = forms.ChoiceField(label="", choices=GENDER_CHOICES,
                            widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Sex'}))

    class Meta:
        model = Workers
        fields = ['sex']

#dodawanie nowego zwierzęcia
class AddAnimal(forms.ModelForm):
    name=forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Name", "class": "form-control"}), label="")
    status =forms.ChoiceField(label="",choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Status'}))
    breed = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Breed", "class": "form-control"}), label="")
    species = forms.ChoiceField(label="", choices=SPECIES_CHOICES,
                            widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Species'}))
    sex = forms.ChoiceField(label="", choices=GENDER_CHOICES,
                            widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Sex'}))
    age = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Age", "class":"form-control"}), label="")
    size = forms.ChoiceField(label="",choices=SIZE_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Size'}))
    vaccinations =forms.ChoiceField(label="Vaccinations:",choices=BOOL_YN, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'vaccinations'}))
    sterilization = forms.ChoiceField(label="Sterilization:",choices=BOOL_YN, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'sterilization'}))
    friendly_kids =forms.ChoiceField(label="Friendly to kieds:",choices=BOOL_YN, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'friendly_kids'}))
    friendly_others = forms.ChoiceField(label="Friendly to others:",choices=BOOL_YN, widget=forms.Select(attrs={'class': 'form-control','placeholder': 'friendly_others'}))

    class Meta:
        model = Animal
        exclude = ("user",)

#kwestionariusz adopcyjny edycja dla pracownikow tylko
class Adopt(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "First Name", "class": "form-control"}), label="")
    surname = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Last Name", "class": "form-control"}), label="")
    telephone = forms.CharField(required=True,max_length=9,
                            widget=forms.widgets.TextInput(attrs={"placeholder": "Phone", "class": "form-control"}),
                            label="")
    class Meta:
        model = Adopt_form
        exclude = ["user",]

#kwestonariusz adopcyjny do wypelnienia bez pola statusu
class UserAdopt(Adopt):
    class Meta(Adopt.Meta):
        exclude = ["status",]


#update polaczenia pracownika ze zwierzeciem
class WorkerUpdateForm(forms.ModelForm):
    class Meta:
        model = Connector
        fields = '__all__'