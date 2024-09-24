from datetime import timedelta
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views import View
from django.shortcuts import redirect, render
from django.utils import timezone
from cards.models import Card
from cards.forms import CardForm


class IndexView(TemplateView):
    template_name = "cards/index.html"


class CardListView(ListView):
    model = Card
    queryset = Card.objects.all()
    context_object_name = "cards"
    template_name = "cards/card_list.html"


class CardCreateView(CreateView):
    model = Card
    form_class = CardForm
    template_name = "cards/card_form.html"
    success_url = "/cards/"
    extra_context = {"title": "Create Card"}


class CardUpdateView(UpdateView):
    model = Card
    form_class = CardForm
    template_name = "cards/card_form.html"
    success_url = "/cards/"
    extra_context = {"title": "Update Card"}


class CardDeleteView(DeleteView):
    model = Card
    success_url = "/cards/"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)


class CardStudyView(View):
    @staticmethod
    def _get_card():
        one_hour_ago = timezone.now() - timedelta(minutes=1)
        return (
            Card.objects.filter(is_active=True, updated_at__lt=one_hour_ago)
            .order_by("recalled_at")
            .first()
        )

    def get(self, request):
        card = self._get_card()
        return render(request, "cards/card_study.html", {"card": card})

    def post(self, request):
        card = self._get_card()
        knowledge_status = request.POST.get("knowledge_status")
        if knowledge_status == "known":
            card.recalled_at = timezone.now()
            card.save()
        else:
            card.save()
        return redirect("cards:card_study")
