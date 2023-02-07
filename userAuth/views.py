from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'userAuth/main.html')

def sign_in(request):

    if request.method=="POST":
        pass

    return render(request, 'userAuth/signin.html')

def register(request):

    if request.method=="POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email_address']
        username = request.POST['uname']
        pwd = request.POST['pd']
        conf_pwd = request.POST['conf_pd']

        print("IT WORKS!")

    return render(request, 'userAuth/register.html')

def logout(request):
    pass
