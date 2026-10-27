# SEEK 채용 공고 수집

호주 SEEK의 Victoria 지역 채용 공고에서 회사·위치·근무 형태·급여·상세 설명을 수집해 CSV로 저장하는 스크립트입니다.

Seeka Technology 인턴 기간(2025.01–05)에 작성한 코드입니다.

**시작점:** [seek.py](scripts/seek.py) · **출력:** `jobs.csv` · **수집 범위:** 목록 페이지 1–25

## 코드와 결과

| 파일 | 역할 |
| --- | --- |
| [seek.py](scripts/seek.py) | 목록과 상세 페이지를 순회해 채용 정보 수집 |
| [requirements.txt](requirements.txt) | Python 의존성 |
| [수동 실행 설정](.github/workflows/seek_crawl.yml) | 명시적인 수동 실행으로 스크립트 실행 |
| `jobs.csv` | 실행 중 생성되는 수집 결과 |

현재 코드는 첫 25개 목록 페이지를 순회합니다. 스프레드시트 적재·역량 추출은 다른 인턴 저장소에서 다루며, 이 저장소의 출력은 CSV입니다.

## 실행 조건

Python, Chrome과 호환되는 ChromeDriver가 필요합니다. `CHROMEDRIVER_PATH`를 설정하면 해당 드라이버를 사용하며, 생략하면 Selenium의 기본 드라이버 탐색을 사용합니다. 워크플로는 Selenium의 기본 드라이버 탐색을 사용하며, 특정 Chrome 버전에 고정한 드라이버를 내려받지 않습니다.

```bash
python -m pip install -r requirements.txt
python scripts/seek.py
```

수집 대상 페이지의 구조에 의존하므로 현재 사이트에 맞는 선택자와 실행 환경을 확인해야 합니다. 워크플로는 Actions의 수동 실행만 허용합니다. `confirm_external_access`를 체크해야 수집이 시작되며, push·문서 변경·PR 병합으로는 수집하지 않습니다.

## 관련 인턴 업무

[Jora 수집](https://github.com/Skullking2520/jora_scrapping) · [YourCareer 수집](https://github.com/Skullking2520/yourcareer-au-scrapping) · [직무 역량 추출](https://github.com/Skullking2520/Skillls_extract)

## 코드와 자료의 범위

업무 수집 원본과 인증정보는 실행 예제로 제공하지 않습니다. 생성 CSV는 버전 관리에서 제외하며, 제외 규칙은 과거 이력을 제거하지 않습니다.

이번 정리에서 수집 코드를 `scripts/`로 옮겼습니다. 의존성과 설정 예시는 루트에 두며, 실행 명령의 기준 경로는 저장소 루트입니다.
