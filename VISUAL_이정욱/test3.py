import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from datetime import datetime, timedelta
import time  # time 모듈 임포트

# 날짜 범위 설정 (2024-06-01부터 2024-12-31까지)
start_date = datetime(2025, 2, 1)
end_date = datetime(2025, 2, 3)

# 날짜를 하루씩 증가시키면서 반복
current_date = start_date

while current_date <= end_date:
    # 날짜를 YYYYMMDD 형식으로 변환
    date_str = current_date.strftime("%Y%m%d")

    # URL 정의
    url = f"https://www.airportal.go.kr/servlet/aips.life.airinfo.RbBejCTL?gubun=c_getList&airport=RKPC&al_icao=&current_date={date_str}&depArr=D&fp_id="
    response = requests.get(url)

    # HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # width="2"인 td 태그 및 bgcolor 속성이 있는 td 태그 삭제
    for td in soup.find_all('td'):
        if td.get('width') == '2' or td.get('bgcolor'):
            td.decompose()  # 해당 태그 삭제

    # 수정된 HTML을 txt 파일로 저장
    with open(f'filtered_response_{date_str}.txt', 'w', encoding='utf-8') as txtfile:
        txtfile.write(str(soup))

    # td width가 140인 경우를 기준으로 인덱스를 구분하여 데이터 추출
    data = []
    row = []

    # td width="140"을 기준으로 새 인덱스 시작
    for td in soup.find_all('td'):
        width = td.get('width')

        if width == '140':  # td width가 140인 경우 새로운 인덱스를 시작
            if row:  # 기존의 row가 있다면 데이터를 추가
                # 열의 개수가 10개를 넘지 않도록 10개로 맞추기
                if len(row) > 10:
                    row = row[:10]  # 10개로 자르기
                data.append(row)
            row = []  # 새 인덱스를 시작하므로 row 초기화

        # 텍스트 추출 후 비어있으면 NaN 처리
        text = td.get_text(strip=True)
        if text == "":  # 비어있는 경우 NaN으로 처리
            text = "NaN"

        row.append(text)  # 현재 행에 데이터 추가

    # 마지막 데이터 추가
    if row:
        # 열의 개수가 10개를 넘지 않도록 10개로 맞추기
        if len(row) > 10:
            row = row[:10]  # 10개로 자르기
        data.append(row)

    # 컬럼 이름 추가
    columns = ['항공사', '항공편명', '목적지', '계획', '예상', '출발', '구분', '현황', '비정상원인', '비고']

    # 데이터를 DataFrame으로 변환 (행렬 형태로 변경)
    df = pd.DataFrame(data, columns=columns)

    # CSV 파일로 저장
    df.to_csv(f'filtered_data_{date_str}.csv', index=False, encoding='utf-8')

    print(f"필터링된 HTML이 filtered_response_{date_str}.txt 파일로 저장되었고, 데이터가 filtered_data_{date_str}.csv 파일로 저장되었습니다.")

    # 하루 증가
    current_date += timedelta(days=1)

    # 요청 간에 1초 대기
    time.sleep(1)  # 1초 간격
