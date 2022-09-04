from django.db import models
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render,redirect
import bcrypt

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['username']) < 6:
            errors["username"] = "Username should be at least 6 characters"
        if len(postData['password']) < 7:
            errors["password"] = "Password should be at least 7 characters"
        return errors

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=45)
    password = models.TextField()
    login_date = models.DateTimeField()
    objects = UserManager() 

#____Methods____
def get_all_users():
    return User.objects.all()


def get_user(user_id):
    return User.objects.get(id=user_id)

    
def save_user(formvalue): #request.POST
    errors = User.objects.basic_validator(formvalue.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(formvalue, value)
        # redirect the user back to the form to fix the errors
        #return redirect('/app1/register')
    else:
        user_password = formvalue.POST['password']
        hash1 = bcrypt.hashpw(user_password.encode(), bcrypt.gensalt()).decode()
        print(user_password)
        User.objects.create(username = formvalue.POST['username'] ,password = hash1 ,login_date=datetime.now()   )
        messages.success(formvalue, "User successfully Saved")
        
def get_alluser():
    return User.objects.all()
    
def remove_user(user_id):
    User1 = User.objects.get(id=user_id)
    User1.delete()

def update_user(user_id):
    User1 = User.objects.get(id=user_id)
    return User1

def update_user_data(value): #request.POST
    User2 = User.objects.get(id=value.POST['id'])
    User2.username = value.POST['username']
    User2.password = value.POST['password']
    print("aaaaaaaaaaaaaa$$$$$$$$$$$",User2.username, User2.password, User2.login_date) 
    User2.save()


def user_login(formvalue): #request.POST   
        user_exist = User.objects.filter(username=formvalue.POST['username'])
        #print(user_exist.password)
        #print(formvalue.POST['password'].encode() )
        if user_exist:
            logged_user = user_exist[0] 
            if bcrypt.checkpw(formvalue.POST['password'].encode(), user_exist[0].password.encode()):
                print("password match")
                loggedin(formvalue)
                return redirect('/app1/Viewall')
                #messages.success(formvalue, "User successfully Logged")
            else:
                print("failed password")   
                return False            
        else:
            #print(user_exist[0].password)
            print("testtttttt")
            return False       

        #querycount = User.objects.filter(username=value.POST['username'], password=value.POST['password']).count()
        #if (querycount == 1):
        #    loggedin(value) 
        #    print("Nasriii")             
        #else: 
        #    print("not Logged in",querycount) 
        #    print("yessss") 



def loggedin(value):
    value.session['username'] = value.POST['username']
    value.session['loggedin'] = 1

def loggedout(value):
    del value.session['username']
    del value.session['loggedin']


#make sure of indenation
# close any datbase IDE beacuse it may lock the DB