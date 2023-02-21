from django import forms


class GroupMultiWidget(forms.MultiWidget):

    template_name = "input_group/input_group.html"
