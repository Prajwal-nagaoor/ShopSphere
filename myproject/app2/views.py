from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from app1.models import cartmodel
# Create your views here.
def login_(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        u = authenticate(request, username = username, password=password)
        if u:
            login(request,u)
            return redirect('home')
        else:
            return render(request, 'login.html', {'status':True})

    return render(request, 'login.html', {'login_':True})
def register(request):
    if request.method == 'POST':
        
        first_name = request.POST.get('first_name', 'dummy name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        conf_pass = request.POST.get('conf_pass')

        # Password match check
        if password != conf_pass:
            return render(request, 'reg.html', {'pass_not_match': True})

        # Username exists check
        if User.objects.filter(username=username).exists():
            return render(request, 'reg.html', {'username_exits': True})

        # Create user
        u = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username
        )
        u.set_password(password)
        u.save()

        return redirect('login')

    return render(request, 'reg.html', {'login_': True})

def profile(request):
    cart_count = cartmodel.objects.filter(host = request.user).count()

    return render(request, 'profile.html',{'profile':True,'cart_count':cart_count})
def logout_(request):
    logout(request)
    return redirect('login')
def update(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        u = User.objects.get(username = request.user)
        u.first_name = first_name,  
        u.last_name = last_name,
        u.email = email,
        u.username = username
        u.save()
        return redirect('profile')      
    return render(request,'update.html')


        
        