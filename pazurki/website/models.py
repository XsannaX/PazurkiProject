from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# pracownik
class Workers(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    id_worker = models.AutoField(primary_key=True)
    sex = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.user.username

    # class Meta:
    # unique_together=('id_worker','user')


# Create Profile When New User Signs Up
# @receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Workers(user=instance)
        user_profile.save()


post_save.connect(create_profile, sender=User)


# zwierze
class Animal(models.Model):
    BOOL_YN = (
        (True, 'Yes'),
        (False, 'No')
    )
    YN_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    SIZE_CHOICES = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Big', 'Big'),
    )
    SPECIES_CHOICES = (
        ('Cat', 'Cat'),
        ('Dog', 'Dog'),
    )
    STATUS_CHOICES = (
        ('For adoption', 'For adoption'),
        ('Not available', 'Not available'),
    )
    id_animal = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True)
    breed = models.CharField(max_length=30, null=True)
    species = models.CharField(max_length=3, choices=SPECIES_CHOICES, null=True)
    sex = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    age = models.IntegerField(null=True)
    size = models.CharField(max_length=6, choices=SIZE_CHOICES, null=True)
    vaccinations = models.CharField(max_length=6, choices=YN_CHOICES, null=True, verbose_name='Vaccinated')
    sterilization = models.CharField(max_length=6, choices=YN_CHOICES, null=True, verbose_name='Sterilized')
    friendly_kids = models.CharField(max_length=6, choices=YN_CHOICES, null=True, verbose_name='Friendly to kids')
    friendly_others = models.CharField(max_length=6, choices=YN_CHOICES, null=True,
                                       verbose_name='Friendly to other animals')
    img = models.ImageField(blank=True, default="pfp2.jpg", upload_to='animal_pics/')

    def __str__(self):
        return self.name


# polaczenie pracownika ze zwierzeciem
class Connector(models.Model):
    id_connector = models.AutoField(primary_key=True)
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, blank=True, null=True)
    worker = models.ForeignKey(Workers, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.animal.name


# automatyczne stworzenie polaczenia po dodaniu zwierzecia
def create_connection(sender, instance, created, **kwargs):
    if created:
        animal_connection = Connector(animal=instance)
        animal_connection.save()


post_save.connect(create_connection, sender=Animal)


# kwestionariusz adopcyjny
class Adopt_form(models.Model):
    STATUS = (
        ('Processing', 'Processing'),
        ('Adopted', 'Adopted'),
    )
    id_adopt_form = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=True)
    surname = models.CharField(max_length=50, null=True)
    telephone = models.CharField(max_length=9, null=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=12, choices=STATUS, null=True, default='Processing')

    def __str__(self):
        return self.name + ' ' + self.surname

    # po zmienie statusu na 'adoptowany' zmienia status zwierzęcia na 'not available' oraz dodaje historie adopcji
    def save(self, *args, **kwargs):
        if (self.status == 'Adopted'):
            self.update_animal_status(),
            Adoption_history.objects.create(form=self)
        return super().save(*args, **kwargs)

    def update_animal_status(self):
        animal, _ = Animal.objects.update_or_create(
            adopt_form=self.id_adopt_form,
            defaults={
                "status": 'Not available',
            }
        )


# historia adopcji
class Adoption_history(models.Model):
    id_adoption_history = models.AutoField(primary_key=True)
    form = models.OneToOneField(Adopt_form, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.form.name
