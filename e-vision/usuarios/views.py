from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import LoginForm


def sign_in(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
                    return HttpResponseRedirect(reverse('portal'))
        return HttpResponseRedirect('home')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            nome = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=nome, password=password)
            
            if user:
                login(request, user)
                # messages.success(request, f'Hi {nome.title()}, welcome back!')

                if user.is_staff:
                    return HttpResponseRedirect(reverse('portal'))

                return HttpResponseRedirect(reverse('home'))

            messages.error(request, 'Usuario ou senha inválido!')

    form = LoginForm()
    return render(request, 'login.html', {'form': form})
    
    
def sign_out(request):
    logout(request)
    messages.success(request, 'Você foi desconectado.')
    return redirect('login')  


