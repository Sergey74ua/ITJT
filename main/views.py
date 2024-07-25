from django.shortcuts import render

def index(request):
    data = {
        'title': 'ITJT: IT - Job Training'
    }
    return render(request, 'main/index.html', data)

def about(request):
    data = {
        'title': 'ITJT: about'
    }
    return render(request, 'main/about.html', data)

def contact(request):
    data = {
        'title': 'ITJT: about'
    }
    return render(request, 'main/contact.html', data)