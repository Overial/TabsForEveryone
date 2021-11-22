from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy

from .models import Tab


# View for login functionality
class CustomLoginView(LoginView):
    # Specify the template
    template_name = 'tfe/login.html'
    # Specify needed fields for form
    fields = '__all__'
    # Redirect already authenticated user from that view
    redirect_authenticated_user = True

    # Redirect user if success
    def get_success_url(self):
        return reverse_lazy('tfe:tabs')


# View for register
class RegisterPageView(FormView):
    template_name = 'tfe/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tfe:tabs')

    # Save user
    def form_valid(self, form):
        user = form.save()

        if user is not None:
            login(self.request, user)
        return super(RegisterPageView, self).form_valid(form)

    # Redirect registered user
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tfe:tabs')
        return super(RegisterPageView, self).get(*args, **kwargs)


# View for tab list functionality
class TabList(ListView):
    model = Tab
    context_object_name = 'tabs'
    template_name = 'tfe/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        # Tabs count
        context['tab_count'] = context['tabs'].count()

        # User searching
        title_search_input = self.request.GET.get('search_area') or ''
        if title_search_input:
            context['tabs'] = context['tabs'].filter(
                # title__icontains=search_input,
                title__startswith=title_search_input,
            )

        context['title_search_input'] = title_search_input

        return context


class TabDetail(DetailView):
    model = Tab
    fields = '__all__'
    context_object_name = 'tab'


class TabCreate(LoginRequiredMixin, CreateView):
    model = Tab
    fields = ['band', 'album', 'title', 'instrument', 'description', 'tab_image', 'audio_file']
    success_url = reverse_lazy('tfe:tabs')


class TabUpdate(LoginRequiredMixin, UpdateView):
    model = Tab
    fields = '__all__'
    success_url = reverse_lazy('tfe:tabs')


class TabDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Tab
    context_object_name = 'tab'
    success_url = reverse_lazy('tfe:tabs')
    permission_required = 'tfe.can_delete_tabs'
