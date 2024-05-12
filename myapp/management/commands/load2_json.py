from django.core.management.base import BaseCommand
import json
from django.utils.dateparse import parse_datetime
from myapp.models import News
import datetime

class Command(BaseCommand):
    help = 'Loads data from a JSON file into the database'

    def handle(self, *args, **options):
        # JSON 파일의 경로를 정확하게 지정해주세요.
        path_to_json = 'info.json'
        with open(path_to_json, 'r', encoding='utf-8') as file:
            data = json.load(file)
            news_entries = data['DATA']
            for entry in news_entries:
                # reg_date가 타임스탬프 형태로 제공된다고 가정하고 처리
                # 예: JSON에서 제공하는 reg_date가 밀리초 단위의 타임스탬프라고 가정
                reg_date_timestamp = entry['reg_date'] / 1000  # 초 단위로 변환
                reg_date = datetime.datetime.fromtimestamp(reg_date_timestamp).isoformat()
                
                News.objects.create(
                    n_seq=entry['n_seq'],
                    n_title=entry['n_title'],
                    reg_date=parse_datetime(reg_date),  # ISO 형식 문자열을 datetime 객체로 파싱
                    n_view_count=entry.get('n_view_count', 0),
                    file_path=entry.get('file_path', ''),
                    n_contents=entry['n_contents']
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded news into the database'))
