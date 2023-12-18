
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_user,name='login_user'),
    path('logout/',views.logout_user,name='logout_user'),
    path('add_user/',views.add_user,name='add_user'),
    #path('add_profile/',views.add_profile,name='add_profile'),
    path('adopt/', views.adopt, name='adopt'),
    path('profile/',views.profile,name='profile'),
    path('view_all_animals/',views.view_all_animals,name='view_all_animals'),
    path('animal/<int:pk>', views.animal, name='animal'),
    path('delete_animal/<int:pk>', views.delete_animal, name='delete_animal'),
    path('add_animal/', views.add_animal, name='add_animal'),
    path('update_animal/<int:pk>', views.update_animal, name='update_animal'),
    path('view_adoption_form/',views.view_adoption_form,name='view_adoption_form'),
    path('adoption_record/<int:pk>', views.adoption_record, name='adoption_record'),
    path('update_adoption_form/<int:pk>', views.update_adoption_form, name='update_adoption_form'),
]