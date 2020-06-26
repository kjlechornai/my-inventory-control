from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Item

class HomeView(ListView):
    model = Item
    paginate_by = 12
    template_name = "home.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"

def search(request):
    qs = Item.objects.all()
    title_contains = request.GET.get('title-contains')
    if title_contains != ' ' and title_contains is not None:
        qs = qs.filter(title__icontains=title_contains)
    
    # paginator = Paginator(qs, 12)  # Show 12 contacts per page
    # page = request.GET.get('page', 1)
    # try:
    #     qs = paginator.page(page)
    # except PageNotAnInteger:
    #     qs = paginator.page(1)
    # except EmptyPage:
    #     qs = paginator.page(paginator.num_pages)
    context = {
        'queryset': qs,
        'query': title_contains
    }
    return render(request, "search.html", context)
