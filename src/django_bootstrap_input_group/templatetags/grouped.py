from django import template

from django_bootstrap_input_group.renderer import InputGroupRenderer, GroupedFormRenderer, GroupedFormsetRenderer

register = template.Library()


@register.simple_tag
def bootstrap_grouped_form(form, **kwargs):
    return GroupedFormRenderer(form, **kwargs).render()


@register.simple_tag
def bootstrap_grouped_formset(formset, **kwargs):
    return GroupedFormsetRenderer(formset, **kwargs).render()


@register.simple_tag
def bootstrap_input_group(*fields, **kwargs):
    return InputGroupRenderer(fields, **kwargs).render()
