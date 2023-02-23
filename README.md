# django-bootstrap-input-groups

This is an add-on for [django-bootstrap5](https://pypi.org/project/django-bootstrap5/) that enables rendering the widgets of 
multiple django form fields as a [Bootstrap input group](https://getbootstrap.com/docs/5.2/forms/input-group/).

## Preview

TODO

## Installation

TODO

## Usage
In your templates, load the template tag set `django_bootstrap_input_group`.  
Then you can render an input group of fields either by:
* declaring the groups in a `field_groups` attribute on your form and using the `bootstrap_grouped_form` 
template tag to render that form
* using the `bootstrap_input_group` template tag to render a single group

### Using `field_groups` form attribute:
Declare `field_groups` on your form:
```
from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    notes = forms.CharField()
    
    field_groups = [('Name', ('first_name', 'last_name')), 'notes']
```

Then in your templates:

```
{% load django_bootstrap_input_group %}

<form>
    {# Render a form as a grouped form #}
    {% bootstrap_grouped_form form %}
    
    {# Or for formsets #}
    {% bootstrap_grouped_formset formset %}
</form>
```

`field_groups` contains the names of form fields in the order that they should be rendered in, with nested lists 
(or tuples) of names representing a group. The nested list can be either a flat list, or a two-item list, where 
the first item is the label for the group and the second is the list of field names:
```
# No groups - just field names:
field_groups = ['first_name', 'last_name', 'notes']

# first_name and last_name make up a group, but no group label is specified:
field_groups = [('first_name', 'last_name'), 'notes']

# first_name and last_name make up a group, with the group label "Name":
field_groups = [('Name', ('first_name', 'last_name')), 'notes']
```
If no label is provided, the label of the first field in a group is used as the label for the group. 

### Using the input group template tag:
Or you can just render a group of fields directly, using the `bootstrap_input_group` template tag:
```
{% load django_bootstrap5 django_bootstrap_input_group %}

<form>
    {% bootstrap_input_group form.first_name form.last_name label="Name" %}
    {% bootstrap_field form.notes %}
</form>
```

### Template tag arguments
The `bootstrap_input_group` tag takes (bound) form fields as positional arguments. 
It also takes an optional keyword argument `label` which specifies the label for the group 
(if no label is provided, it defaults to the label of the first field in a group).  
Other than that, the `django_bootstrap_input_group` template tags take the same arguments as their 
`django_bootstrap5` counterparts  
(see here for a [list of the template tags and their parameters](https://django-bootstrap5.readthedocs.io/en/latest/templatetags.html)).

