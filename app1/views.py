from django.shortcuts import render,redirect
from . import models  # import model is important 
from django.contrib import messages

# Create your views here.
from django.shortcuts import render, HttpResponse

def Index(request): 
        print("indexx^^^^^^^")
        return render(request, "User.html")  

def LoginUser(request):
    if request.method == "POST": 
        errors = models.User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            print("Errors") 
            return redirect('/app1/')          
        else: 
            user1 = models.user_login(request)
            if user1 is not False:     
                print("HerereAmeeen")            
                return redirect('/app1/Viewall')  
            else:
                print("meshhoonAmeeen")   
                return redirect('/app1/')        
    print("Herere")
    return redirect('/app1/')   
        
def GetUser(request, id):
    context = {
    	"user": models.get_user(id),
    }
    return render(request, "GetUser.html", context)  

def register(request): 
        print("^^^^^^^",request.POST)
        return render(request, "SavedUser.html")  

def SaveUser(request):
    if request.method == "POST":  
        models.save_user(request)
        return redirect('/app1/register')

def ViewAll(request):
    context = {
    	"AllUsers": models.get_alluser(),
    }  
    return render(request, "AllUsers.html", context)  

def DeleteUser(request, id):
    context = {
    	"delete_user": models.remove_user(id),
    }  
    return render(request, "DeleteUser.html", context)  

def UpdateUser(request, id):
    print("^^^^^^^^^^",request.POST)  
    context = {
    	"updateuser": models.update_user(id),
    }  
    return render(request, "UpdateUser.html", context)  

def UpdateUserData(request):
    print("$$$$$$$$$$$",request.POST) 
    if request.method == "POST":
        print("$$$$$$$$$$$",request.POST) 
        models.update_user_data(request)
        return redirect('/app1/Viewall')


def logout(request):
    if 'username' in request.session:
        del request.session['username']
        del request.session['loggedin']
        print("Deleteee")     
    return redirect('/app1/')