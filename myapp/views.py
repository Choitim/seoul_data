from django.shortcuts import render
from .models import MarketItem

def search_item(request):
    query = request.GET.get('q', '')
    sort = request.GET.get('sort', 'asc')  # 정렬 파라미터 가져오기
    results = []

    if query:
        # 사용자가 선택한 정렬 방식에 따라 쿼리셋을 정렬합니다.
        # 가격이 0원이 아닌 상품만 필터링합니다.
        if sort == 'asc':
            results = MarketItem.objects.filter(a_name__icontains=query, a_price__gt=0).order_by('a_price')
        elif sort == 'desc':
            results = MarketItem.objects.filter(a_name__icontains=query, a_price__gt=0).order_by('-a_price')
        # 정렬 방식이 명시되지 않은 경우 기본적으로 가격이 0원이 아닌 상품만 표시합니다.
        else:
            results = MarketItem.objects.filter(a_name__icontains=query, a_price__gt=0)

    # 정렬된 결과를 컨텍스트에 추가하여 템플릿으로 전달합니다.
    return render(request, 'index.html', {'query': query, 'results': results, 'sort': sort})
