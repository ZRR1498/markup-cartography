from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, FormView

from .forms import *
from .utils import DataMixin
from .services import output


class Home(DataMixin, ListView):
    model = User
    template_name = 'markup/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))


class GetMarkUp(DataMixin, FormView):
    form_class = PushNumber
    template_name = 'markup/add_markup.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Разметка объекта")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        check_map = output(form.cleaned_data['number'])
        if check_map is False:
            return redirect('add_markup')
        return redirect('look_map')


class LookMap(DataMixin, FormView):
    form_class = PushNumber
    template_name = 'markup/look_map.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Разметка объекта", map='map_folium.html')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        check_map = output(form.cleaned_data['number'])
        if check_map is False:
            return redirect('add_markup')
        return redirect('look_map')


class Map(DataMixin, FormView):
    form_class = PushNumber
    template_name = 'markup/map_folium.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Разметка объекта")
        return dict(list(context.items()) + list(c_def.items()))


class StartMap(DataMixin, FormView):
    form_class = PushNumber
    template_name = 'markup/map_start.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Глобальная карта")
        return dict(list(context.items()) + list(c_def.items()))


class HistoryMarkUp(DataMixin, ListView):
    model = User
    template_name = 'markup/history_markup.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="История разметок")
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'markup/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация пользователя")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'markup/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class Contact(DataMixin, ListView):
    model = User
    template_name = 'markup/contact.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Контакты")
        return dict(list(context.items()) + list(c_def.items()))