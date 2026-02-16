from django.shortcuts import render

def home(request): 
    context = {
        'data': [],
    }
    return render(request, 'home.html', context)

def about(request): 
    context = {
        'data': [],
    }
    return render(request, 'about.html', context)

def programs(request): 
    context = {
        'data': [],
    }
    return render(request, 'programs.html', context)

def faq(request): 
    context = {
        'data': [],
    }
    return render(request, 'faq.html', context)

def contact(request): 
    context = {
        'data': [],
    }
    return render(request, 'contact.html', context)

def login(request): 
    context = {
        'data': [],
    }
    return render(request, 'login.html', context)