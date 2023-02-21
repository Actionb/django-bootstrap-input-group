from django import forms

from django_bootstrap5.widgets import RadioSelectButtonGroup


class MenuForm(forms.Form):
    main = forms.ChoiceField(
        choices=[('egg', 'Egg'), ('bacon', 'Bacon'), ('sausage', 'Sausage')],
        widget=RadioSelectButtonGroup
    )
    side = forms.ChoiceField(
        choices=[('spam1', 'Spam'), ('egg', 'Spam, Egg, Spam'), ('spam2', 'Spam')]
    )
    amount = forms.IntegerField(help_text='Specify number of dishes', min_value=1)

    dessert = forms.CharField(required=False)
    topping = forms.ChoiceField(
        choices=[('spam1', 'Spam'), ('bacon', 'Bacon, Spam'), ('spam2', 'Spam')],
        widget=RadioSelectButtonGroup,
        required=False
    )

    notes = forms.CharField(widget=forms.Textarea, required=False)

    field_groups = [
        ('Main Dish', ['main', 'side', 'amount']),
        ('', ['dessert', 'topping']),
        'notes'
    ]

    class Media:
        css = {'all': ['django_bootstrap_input_group/css/bootstrap_input_group.css']}


MenuFormset = forms.formset_factory(MenuForm, extra=2)
