# SEEK 채용 공고 수집

호주 SEEK의 Victoria 지역 채용 공고에서 회사·위치·근무 형태·급여·상세 설명을 수집해 CSV로 저장하는 스크립트입니다.

## 수행 배경

Seeka Technology 소프트웨어 개발 인턴 업무로 진행했습니다. 인턴 기간은 2025년 1월–5월이며, 원격근무로 데이터 수집·처리 업무를 수행했습니다.

## 코드와 결과

| 파일 | 역할 |
| --- | --- |
| [seek.py](scripts/seek.py) | 목록과 상세 페이지를 순회해 채용 정보 수집 |
| [requirements.txt](requirements.txt) | Python 의존성 |
| [자동 실행 설정](.github/workflows/seek_crawl.yml) | `master` push를 계기로 스크립트 실행 |
| `jobs.csv` | 실행 중 생성되는 수집 결과 |

현재 코드는 첫 25개 목록 페이지를 순회합니다. 스프레드시트 적재·역량 추출은 다른 인턴 저장소에서 다루며, 이 저장소의 출력은 CSV입니다.

## 실행 조건

Python, Chrome과 호환되는 ChromeDriver가 필요합니다. `CHROMEDRIVER_PATH`를 설정하면 해당 드라이버를 사용하며, 생략하면 Selenium의 기본 드라이버 탐색을 사용합니다. 워크플로는 설치한 드라이버 경로를 명시합니다.

```bash
python -m pip install -r requirements.txt
python scripts/seek.py
```

수집 대상 페이지의 구조에 의존하므로 현재 사이트에 맞는 선택자와 실행 환경을 확인해야 합니다. 저장소의 workflow는 `master` push에 연결돼 있으며, 워크플로의 경로 필터는 Python 소스·의존성 변경에만 반응하므로 문서 변경으로 수집을 실행하지 않습니다.

## 관련 인턴 업무

[Jora 수집](https://github.com/Skullking2520/jora_scrapping) · [YourCareer 수집](https://github.com/Skullking2520/yourcareer-au-scrapping) · [직무 역량 추출](https://github.com/Skullking2520/Skillls_extract)

## 저장소 관리

실행 결과·인증 파일은 버전 관리에서 제외합니다. 공개 소스와 수집 데이터의 공개 범위는 구분하며, 인턴 업무 데이터·시트 접근 권한은 포함하지 않습니다. 현재 파일의 제외 규칙은 이미 추적된 자료나 과거 커밋의 노출을 제거하지 않습니다.

## 저장소 구성

이번 정리에서 수집 코드을 `scripts/`로 옮겼습니다. 의존성과 설정 예시는 루트에 두며, 실행 명령의 기준 경로는 저장소 루트입니다.
