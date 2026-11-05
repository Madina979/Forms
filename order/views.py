from django.shortcuts import render, redirect
from .forms import OrderForm

PRODUCTS = {
    'laptop': ('Ноутбук', 5_000_000),
    'phone': ('Телефон', 3_000_000),
    'headphones': ('Наушники', 200_000)
}
DELIVERY = {
    'pickup': ('Самовывоз', 0),
    'courier': ('Курьер', 30_000),
}
def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            product_name, price = PRODUCTS[data['product']]
            delivery_name, delivery_price = DELIVERY[data['delivery']]
            total = price * data['quantity'] + delivery_price
            request.session['order'] = {
                'name': data['name'],
                'product' : product_name,
                'quantity': data['quantity'],
                'price': price,
                'delivery': delivery_name,
                'total': total
            }
            return redirect('order_result')
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form' : form})

def order_result(request):
    order_data = request.session.get('order')
    if not order_data:
        return redirect('order')
    return render(request, 'order_result.html', {'order':order_data} )


