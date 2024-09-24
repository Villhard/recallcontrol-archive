from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
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
