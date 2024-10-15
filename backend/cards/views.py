from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    TemplateView,
    UpdateView,
)

from cards.forms import CardForm
from cards.models import Card


class IndexView(TemplateView):
    template_name = "cards/index.html"


class CardListView(LoginRequiredMixin, ListView):
    model = Card
    context_object_name = "cards"
    template_name = "cards/card_list.html"

    def get_queryset(self):
        return Card.objects.filter(owner=self.request.user)


class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    form_class = CardForm
    template_name = "cards/card_form.html"
    success_url = "/cards/"
    extra_context = {"title": "Создать карточку"}

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CardUpdateView(LoginRequiredMixin, UpdateView):
    model = Card
    form_class = CardForm
    template_name = "cards/card_form.html"
    success_url = "/cards/"
    extra_context = {"title": "Изменить карточку"}

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.owner != self.request.user:
            raise PermissionDenied("You do not have permission to edit this card")
        return obj

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CardDeleteView(LoginRequiredMixin, DeleteView):
    model = Card
    success_url = "/cards/"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.owner != self.request.user:
            raise PermissionDenied("You do not have permission to delete this card")
        return obj

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)


class CardStudyView(LoginRequiredMixin, View):
    def get(self, request):
        card = Card.study_objects.filter(owner=request.user).first()
        return render(request, "cards/card_study.html", {"card": card})

    def post(self, request):
        card = Card.objects.get(pk=request.POST.get("card_id"))
        knowledge_status = request.POST.get("knowledge_status")
        if knowledge_status == "known":
            card.recalled_at = timezone.now()
            card.save()
        else:
            card.save()
        return redirect("cards:card_study")
