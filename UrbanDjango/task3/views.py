from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'third_task/home.html')

def shop(request):
    games = {
        'games': [
            'Atomic Heart',
            'Cyberpunk 2077',
            'PayDay 2',
        ]
    }
    return render(request, 'third_task/shop.html', games)

def cart(request):
    return render(request, 'third_task/cart.html')
