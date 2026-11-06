from django.shortcuts import render


def user(request):
    context = {
        'id': request.GET.get('id', '1'),
        'name': request.GET.get('name', 'Madina'),
        'age': request.GET.get('age', '15'),
        'address': request.GET.get('address', 'Nukus'),
        'email': request.GET.get('email', 'madina@gmail.com'),
        'phone': request.GET.get('phone', '+998883485551'),
    }

    return render(request, 'users/user.html', context)