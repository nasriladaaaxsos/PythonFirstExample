from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    path('', views.Index),   
    path('LoginUser', views.LoginUser),
    path('Get/<int:id>', views.GetUser), 
    path('Save', views.SaveUser),
    path('register', views.register),   
    path('Viewall', views.ViewAll), 
    path('Remove/<int:id>', views.DeleteUser), 
    path('Update', views.UpdateUserData),   
    path('Update/<int:id>', views.UpdateUser),
    path('logout',views.logout),
]