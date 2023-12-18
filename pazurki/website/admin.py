from django.contrib import admin
from django.contrib.auth.models import User
from .models import Animal
from .models import Workers
from .models import Connector
from .models import Adopt_form
from .models import Adoption_history

admin.site.register(Animal)
admin.site.register(Adopt_form)
admin.site.register(Connector)
admin.site.register(Workers)
admin.site.register(Adoption_history)

# Mix Profile info into User info
class ProfileInline(admin.StackedInline):
	model = Workers

# Extend User Model
class UserAdmin(admin.ModelAdmin):
	model = User
	fields = ["username","first_name","last_name","password","is_staff","is_active","is_superuser"]
	inlines = [ProfileInline]

# Unregister initial User
admin.site.unregister(User)

# Reregister User and Profile
admin.site.register(User, UserAdmin)
