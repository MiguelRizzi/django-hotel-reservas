from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from .forms import InfoUsuarioForm
from .models import InfoUsuario

# Create your views here.
class InfoUsuarioDetail(LoginRequiredMixin, DetailView):
    model = InfoUsuario
    
class InfoUsuarioCreate(LoginRequiredMixin, CreateView):
    model = InfoUsuario
    form_class = InfoUsuarioForm
    success_url = reverse_lazy('home:index')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
   
    
class InfoUsuarioUpdate(LoginRequiredMixin, UpdateView):
    model= InfoUsuario
    form_class = InfoUsuarioForm
    success_url = reverse_lazy('home:index')

    
class InfoUsuarioDelete(LoginRequiredMixin, DeleteView):
    model= InfoUsuario
    success_url = reverse_lazy("home:index")
