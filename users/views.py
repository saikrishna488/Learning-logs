from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def user_logout(request):
    logout(request)

    # return redirect('users:login')
    return render(request, 'registration/logged_out.html')


def register(request):

    if request.method != 'POST':
        form = UserCreationForm()

    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            
            login(request, new_user)

            return redirect('learning_logs:index')
        
    context = {'form': form}
    return render(request, 'registration/register.html', context)
        