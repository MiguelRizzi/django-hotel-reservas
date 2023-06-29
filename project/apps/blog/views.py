
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from .forms import ReseñaForm
from .models import Reseña

# Create your views here.
class ReseñaDetail(LoginRequiredMixin, DetailView):
    model = Reseña

class ReseñaList(LoginRequiredMixin, ListView):
    model = Reseña


class ReseñaCreateView(LoginRequiredMixin, CreateView):
    model = Reseña
    form_class = ReseñaForm
    success_url = reverse_lazy("blog:reseña_list")
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
class ReseñaUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Reseña
    success_url = reverse_lazy("blog:reseña_list")
    form_class = ReseñaForm

    
class ReseñaDelete(LoginRequiredMixin, DeleteView):
    model = Reseña
    success_url = reverse_lazy("blog:reseña_list")

