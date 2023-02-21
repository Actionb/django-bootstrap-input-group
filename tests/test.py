from django import forms
from django.template import engines
from django.test import TestCase

from django_bootstrap5.widgets import RadioSelectButtonGroup

from django_bootstrap_input_group.fields import GroupMultiField
from django_bootstrap_input_group.widgets import GroupMultiWidget


class SeiteWidget(GroupMultiWidget):

    def decompress(self, value):
        if value is None:
            return ['', '']
        return value.split(" ")


class SeitenumfangField(GroupMultiField):

    widget = SeiteWidget

    def __init__(self, **kwargs):
        fields = [
            forms.IntegerField(widget=forms.NumberInput(attrs={'type': 'tel'})),
            forms.ChoiceField(
                choices=[(None, '---'), ('f', 'f'), ('ff', 'ff')],
                widget=RadioSelectButtonGroup
            )
        ]
        super().__init__(fields, **kwargs)

    def compress(self, data_list):
        return " ".join(data_list)


class Form(forms.Form):
    seite = SeitenumfangField()


class BootstrapTestCase(TestCase):
    """TestCase with render function for template code."""

    def render(self, text, context=None, load_bootstrap=True):
        """Return rendered result of template with given context."""
        prefix = "{% load django_bootstrap5 %}" if load_bootstrap else ""
        template = engines["django"].from_string(f"{prefix}{text}")
        return template.render(context or {})


class Test(BootstrapTestCase):

    def test(self):
        form = Form()
        self.assertFalse(self.render('{% bootstrap_form form %}', context={'form': Form()}))


class RenderForm(forms.Form):
    name = forms.CharField()
    page = forms.IntegerField()
    size = forms.ChoiceField(choices=[('f', 'f'), ('ff', 'ff')])
    other = forms.CharField(widget=forms.Textarea)

    field_groups = ['name', ('page', 'size'), 'other']


class TestFieldRenderer(BootstrapTestCase):

    def test(self):
        form = RenderForm()
        self.assertFalse(
            self.render('{% bootstrap_grouped_form form %}', context={'form': form}),
        )
