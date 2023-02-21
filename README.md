# django-compact-radioselect
A radio select widget for Django apps that hides the radio buttons and aligns the
options horizontally.  
The widget looks and behaves like a [segmented control](https://primer.style/design/components/segmented-control).  

Best used when there are between 2 and 5 options to choose from and the option
labels are short and consistent. (See the excellent flowchart in [this article](https://medium.com/tap-to-dismiss/a-better-segmented-control-9e662de2ef57))

## Preview

TODO

## Installation

1. Install package: `pip install django-compact-radioselect`

2. Add to `INSTALLED_APPS` in your Django `settings.py`:
```
INSTALLED_APPS = [
    ...
    'django_compact_radioselect',
]
```

## Usage 
Use the widget in place of a RadioSelect widget:
```
from django import forms

from django_compact_radioselect.widgets import CompactRadioSelect


class OrderForm(forms.Form):
    dish = forms.ChoiceField(
        choices=[
            ('egg', 'Egg and Spam'),
            ('bacon', 'Bacon and Spam'),
            ('sausage', 'Sausage and Spam')
        ],
        widget=CompactRadioSelect
    )
```

## HTML and styling

This package provides some rudimentary styling for the widget. 
If you want to add your own styles, the labels of the options are selectable through 
the class `compact-radio-label` and the radio buttons are selectable through the
class `compact-radio-input`. Each option is wrapped in a div with the class `compact-radio-option`.
And finally, the whole group of options is wrapped in a div with the class `compact-radio-container`.

```
<div class="compact-radio-container">
    <div class="compact-radio-option">
        <input type="radio" name="menu" value="egg" class="compact-radio-input">
        <label class="compact-radio-label">Egg and Spam</label>
    </div>
    <div class="compact-radio-option">
        ...
    </div>
</div>
```

## Why not call this a segmented control?

According to the GitHub Primer design guide, segmented controls should be used with buttons that apply their effect 
immediately. 
> A segmented control is treated like a list where each list item contains a button.   
> Do not treat a segmented control like any of the following ARIA roles:
>  * radiogroup, which would require a save button to apply the changes.  
>  * ...
> 
> [...] Designs that treat segmented controls like tabs or radio buttons would be confusing for users who interact with the web using assistive technologies.

https://primer.style/design/components/segmented-control#accessibility

This widget uses radio buttons which apply their effect only after hitting a save or submit button. Maybe that's a 
minor difference, but in order to not confuse, this widget is not called a segmented control widget even though it
is very close. (In other words: this is a Zebra, not a Horse)

## Mentions
Toggle Radios by Adam Culpepper: https://github.com/adamculpepper/toggle-radios