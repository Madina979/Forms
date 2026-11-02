from django import forms

OPERATION_CHOICES = [
    ('add', '(+)'),
    ('sub', '(−)'),
    ('mul', '(×)'),
    ('div', '(÷)'),
]

class CalculatorForm(forms.Form):
    first = forms.FloatField(label='First number:')
    second = forms.FloatField(label='Second number:')
    operation = forms.ChoiceField(label='Operation', choices=OPERATION_CHOICES)

    def clean(self):
        cleaned_data = super().clean()
        operation = cleaned_data.get('operation')
        second = cleaned_data.get('second')

        if operation == 'div' and second == 0:
            self.add_error('second', 'Division by zero is not allowed!')

        return cleaned_data