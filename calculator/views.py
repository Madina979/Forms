from django.shortcuts import render, redirect
from .forms import CalculatorForm

SYMBOLS = {
    'add': '+',
    'sub': '−',
    'mul': '×',
    'div': '÷'
}


def fmt(number):
    """25.0 -> 25, 2.5 -> 2.5"""
    return int(number) if float(number).is_integer() else number


def calculator(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['first']
            b = form.cleaned_data['second']
            op = form.cleaned_data['operation']

            if op == 'add':
                result = a + b
            elif op == 'sub':
                result = a - b
            elif op == 'mul':
                result = a * b
            else:
                result = a / b

            request.session['calc'] = {
                'first': a,
                'second': b,
                'symbol': SYMBOLS[op],
                'result': result,
            }
            return redirect('calculator_result')
    else:
        form = CalculatorForm()

    return render(request, 'calculator.html', {'form': form})


def calculator_result(request):
    data = request.session.get('calc')
    if data is None:
        return redirect('calculator')

    context = {
        'first': fmt(data['first']),
        'second': fmt(data['second']),
        'symbol': data['symbol'],
        'result': fmt(data['result']),
    }
    return render(request, 'calculator_result.html', context)