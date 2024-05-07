import os
import json
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.models import MarketItem

def fix_date_format(date_str):
    # 먼저, 모든 비숫자를 '-'로 변환
    corrected_str = ''.join(['-' if not c.isdigit() else c for c in date_str])
    
    # '-'를 기준으로 날짜를 분리하고, 부적절한 빈 부분을 '01'로 대체
    parts = [part if part else '01' for part in corrected_str.split('-')]
    
    # YYYY, MM, DD 형식으로 맞추기
    if len(parts[0]) == 4:
        year = parts[0]
        month = parts[1].zfill(2)
        day = parts[2].zfill(2)
    else:
        # 예상치 못한 형식 처리
        return '0001-01-01'  # 잘못된 날짜 데이터가 있을 경우 기본값 반환

    corrected_date = f"{year}-{month}-{day}"
    return corrected_date

def load_data_from_json():
    with open('price.json', 'r', encoding='utf-8') as file:
        data = json.load(file)['DATA']
        for item in data:
            try:
                corrected_date = fix_date_format(item['p_date'])
                formatted_date = datetime.strptime(corrected_date, "%Y-%m-%d").date()
            except ValueError as e:
                print(f"날짜 형식 오류: {item['p_date']} - YYYY-MM-DD 형식이어야 합니다.")
                print(f"오류 세부사항: {str(e)}")
                continue

            MarketItem.objects.create(
                m_gu_name=item['m_gu_name'],
                m_type_code=item['m_type_code'],
                a_name=item['a_name'],
                a_price=int(item['a_price']) if item['a_price'].isdigit() else 0,
                p_seq=item['p_seq'],
                m_type_name=item['m_type_name'],
                a_unit=item.get('a_unit', ''),
                m_gu_code=item['m_gu_code'],
                add_col=item.get('add_col', ''),
                m_name=item['m_name'],
                p_date=formatted_date,
                p_year_month=item['p_year_month'],
                a_seq=item['a_seq'],
                m_seq=item['m_seq'],
            )
    print("Data loaded successfully!")

if __name__ == '__main__':
    load_data_from_json()
