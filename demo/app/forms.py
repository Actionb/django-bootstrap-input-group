from django import forms

from django_bootstrap5.widgets import RadioSelectButtonGroup


class OrderMenu(forms.Form):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    main = forms.ChoiceField(
        label="Main Dish",
        choices=[('egg', 'Egg'), ('bacon', 'Bacon'), ('sausage', 'Sausage')],
    )
    side = forms.ChoiceField(
        choices=[('spam1', 'Spam'), ('egg', 'Spam, Egg, Spam'), ('spam2', 'Spam')],
        widget=RadioSelectButtonGroup
    )
    amount = forms.IntegerField(help_text='Specify number of servings', min_value=1)
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows': '2'}), required=False)

    field_groups = [
        ('Name', ('first_name', 'last_name')),
        ('main', 'side', 'amount'),
        'notes'
    ]

    class Media:
        css = {'all': ['django_bootstrap_input_group/css/bootstrap_input_group.css']}


MenuFormset = forms.formset_factory(OrderMenu, extra=2)
