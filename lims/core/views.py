from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, DetailView

from .models import CustomUser
from .forms import PasswordResetValidateForm


class HomePageView(TemplateView):
    template_name = 'core/home.html'


class HelpPageView(TemplateView):
    template_name = 'core/help.html'


class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'core/profile.html'
    context_object_name = 'profile'
    pk_url_kwarg = 'profile_id'
    login_url = '/login/'


def logout_view(request):
    logout(request)
    return redirect(reverse("core:home"))


class PasswordResetView(View):
    template_name = 'core/password_reset.html'
    context = {
        'error': "",
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        email_for_reset = request.POST.get('email_for_reset')
        if email_for_reset and not CustomUser.objects.filter(email=email_for_reset).exists():
            self.context['error'] = 'Email does not exist. Check it or sign up.'
            return render(request, self.template_name, self.context)
        elif not email_for_reset:
            self.context['error'] = 'Введите электронную почту!'
            return render(request, self.template_name, self.context)
        else:
            user = CustomUser.objects.filter(email=email_for_reset).get()
            return redirect(reverse('core:password_reset_validate',  kwargs={'user_id': user.id}))


class PasswordResetValidateView(View):
    template_name = 'core/password_reset_validate.html'
    form = PasswordResetValidateForm

    def get(self, request, *args, **kwargs):
        context = {
            'form': self.form,
            'secret_question': CustomUser.objects.get(pk=kwargs['user_id']).secret_question,
            'user_id': kwargs['user_id'],
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        user_who_reset = CustomUser.objects.get(pk=kwargs['user_id'])
        if form.data.get('secret_answer') != user_who_reset.secret_answer:
            form.add_error('secret_answer', 'Secret answer is not correct')
        if form.is_valid():
            print(user_who_reset)
            user_who_reset.set_password(form.cleaned_data.get('password'))
            user_who_reset.save()
            return redirect(reverse('core:password_reset_completed'))
        else:
            return render(request, self.template_name, {
                'form': form,
                'secret_question': user_who_reset.secret_question,
                'user_id': kwargs['user_id'],
            })
