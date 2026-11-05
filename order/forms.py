from django import forms

PRODUCT_CHOICES = [
    ('laptop', 'Ноутбук'),
    ('phone', 'Телефон'),
    ('headphones', 'Наушники'),
]

DELIVERY_CHOICES = [
    ('pickup', 'Самовывоз'),
    ('courier', 'Курьер'),
]

class OrderForm(forms.Form):
    name = forms.CharField(label='Имя покупателя:', max_length=30)
    phone_number = forms.CharField(label='Телефон:', max_length=30)
    product = forms.ChoiceField(label='Товар:', choices=PRODUCT_CHOICES)
    quantity = forms.IntegerField(label='Количество:', min_value=1)
    delivery = forms.ChoiceField(label='Доставка:', choices=DELIVERY_CHOICES)
    address = forms.CharField(label='Адрес:', max_length=100)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('delivery') == 'courier' and not cleaned_data.get('address'):
            self.add_error('address', 'Для курьера нужно указать адрес')
        return cleaned_data
