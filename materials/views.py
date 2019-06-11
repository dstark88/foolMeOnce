from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
# from django.urls import reverse
from django.views import generic
from django.template import loader
import json

# def index(request):
with open("./materials/quotes_api.json", encoding='utf-8') as json_data:
    data = json.load(json_data)

for quote in data['quotes']:
    print(quote["CompanyName"])

    # return render(request, 'materials/index.html', {'data':data})



# for quote in data['quotes']:
#     print(quote)


# def index(request):
    # with open('quotes_api.json', 'r', encoding='utf-8') as json_file:
    # data = json.load(json_file)

    # for quotes_api in data['quotes_api']:
    #     print(quotes_api['CompanyName'], quotes_api['ExchangeName'])

    # return HttpResponse("Hello, world. You're at the materials index.")

        # return render(request, "materials/index.html", {'data':data})
# def detail(request, article_id):
#     return HttpResponse("You're looking at article %s." % article_id)

# def results(request, article_id):
#     response = "You're looking at the results of article %s."
#     return HttpResponse(response % article_id)
# C:\\Users\\stark\\Desktop\\Code\\codeChallenges\\motleyFool\\foolMeOnce\\materials\\quotes_api.json", 'r', encoding='utf-8'

# class IndexView(generic.ListView):
#     template_name = 'materials/index.html'
#     context_object_name = 'latest_article_list'

# def get_queryset(self):
#     """
#     Return the last five published articles (not including those set to be
#     published in the future).
#     """
#     return Article.objects.filter(
#         pub_date__lte=timezone.now()
#     ).order_by('-pub_date')[:5]


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)


# class DetailView(generic.DetailView):
#     model = Article
#     template_name = 'materials/detail.html'


# class ResultsView(generic.DetailView):
#     model = Article
#     template_name = 'materials/results.html'


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