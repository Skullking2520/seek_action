# SEEK 채용 공고 수집

호주 SEEK의 Victoria 지역 채용 공고에서 회사·위치·근무 형태·급여·상세 설명을 수집해 CSV로 저장하는 스크립트입니다.

## 수행 배경

Seeka Technology 소프트웨어 개발 인턴 업무로 진행했습니다. 인턴 기간은 2025년 1월–5월이며, 원격근무로 데이터 수집·처리 업무를 수행했습니다.

## 코드와 결과

| 파일 | 역할 |
| --- | --- |
| [seek.py](seek.py) | 목록과 상세 페이지를 순회해 채용 정보 수집 |
| [requirements.txt](requirements.txt) | Python 의존성 |
| [자동 실행 설정](.github/workflows/seek_crawl.yml) | `master` push를 계기로 스크립트 실행 |
| `jobs.csv` | 실행 중 생성되는 수집 결과 |

현재 코드는 첫 25개 목록 페이지를 순회합니다. 스프레드시트 적재·역량 추출은 다른 인턴 저장소에서 다루며, 이 저장소의 출력은 CSV입니다.

## 실행 조건

Python, Chrome과 호환되는 ChromeDriver가 필요합니다. 현재 코드의 Driver 경로는 Linux의 `/usr/bin/chromedriver`로 지정돼 있습니다.

```bash
python -m pip install -r requirements.txt
python seek.py
```

수집 대상 페이지의 구조에 의존하므로 현재 사이트에 맞는 선택자와 실행 환경을 확인해야 합니다. 저장소의 workflow는 `master` push에 연결돼 있으며, README 변경도 실행 계기가 될 수 있습니다.

## 관련 인턴 업무

[Jora 수집](https://github.com/Skullking2520/jora_scrapping) · [YourCareer 수집](https://github.com/Skullking2520/yourcareer-au-scrapping) · [직무 역량 추출](https://github.com/Skullking2520/Skillls_extract)
