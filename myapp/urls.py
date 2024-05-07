from django.shortcuts import render
from .models import MarketItem

def search_item(request):
    query = request.GET.get('q', '')
    sort = request.GET.get('sort', 'asc')  # 정렬 파라미터 가져오기
    results = []

    if query:
        if sort == 'asc':
            results = MarketItem.objects.filter(a_name__icontains=query).order_by('a_price')
        elif sort == 'desc':
            results = MarketItem.objects.filter(a_name__icontains=query).order_by('-a_price')

    return render(request, 'index.html', {'query': query, 'results': results, 'sort': sort})
