from django import forms

from .widgets import GroupMultiWidget


class GroupMultiField(forms.MultiValueField):

    widget = GroupMultiWidget

    def __init__(self, fields, widget=None, **kwargs):
        self.widget = (widget or self.widget)(widgets=[f.widget for f in fields])
        super().__init__(fields, **kwargs)
