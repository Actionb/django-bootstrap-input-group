from django.urls import reverse
from django.views.generic import FormView

from .forms import MenuForm, MenuFormset


class BaseView(FormView):
    template_name = 'app/base.html'
    url_name = ""
    is_formset = False

    def setup(self, request, *args, layout="default", **kwargs):
        kwargs['layout'] = layout
        super().setup(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['layout'] = self.kwargs['layout']
        context['url_name'] = self.url_name
        context['is_formset'] = self.is_formset
        if self.is_formset:
            context['switch_url'] = reverse('menu', kwargs=self.kwargs)
            context['switch_text'] = 'View as Form'
        else:
            context['switch_url'] = reverse('menu_formset', kwargs=self.kwargs)
            context['switch_text'] = 'View as Formset'
        return context

    def get_success_url(self):
        return reverse(self.url_name, kwargs=self.kwargs)


class MenuView(BaseView):
    form_class = MenuForm
    url_name = 'menu'


class MenuFormsetView(BaseView):
    form_class = MenuFormset
    url_name = 'menu_formset'
    is_formset = True
