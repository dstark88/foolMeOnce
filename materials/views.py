from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the materials index.")

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Article 
# Choice 


class IndexView(generic.ListView):
    template_name = 'materials/index.html'
    context_object_name = 'latest_article_list'

# def get_queryset(self):
#     """
#     Return the last five published articles (not including those set to be
#     published in the future).
#     """
#     return Article.objects.filter(
#         pub_date__lte=timezone.now()
#     ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Article
    template_name = 'materials/detail.html'


class ResultsView(generic.DetailView):
    model = Article
    template_name = 'materials/results.html'


# def vote(request, article_id):
#     article = get_object_or_404(article, pk=article_id)
#     try:
#         selected_choice = article.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the article voting form.
#         return render(request, 'materials/detail.html', {
#             'article': article,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('materials:results', args=(article.id,)))