import pandas as pd

def remove_first_row_for_dates():
    # 2024년 1월 1일부터 6월 30일까지 반복
    for date in pd.date_range(start="2024-01-01", end="2024-06-30"):
        date_str = date.strftime("%Y%m%d")  # 예: 20240101
        file_name = f"filtered_data_{date_str}.csv"  # 파일명 생성

        try:
            # CSV 파일 읽기 (첫 번째 줄 삭제)
            df = pd.read_csv(file_name, skiprows=2)
            
            # 같은 파일명으로 저장 (덮어쓰기)
            df.to_csv(file_name, index=False)
            print(f"✅ 처리 완료: {file_name}")

        except FileNotFoundError:
            print(f"⚠️ 파일 없음: {file_name} (건너뜀)")
        except Exception as e:
            print(f"❌ 오류 발생: {file_name} - {e}")

# 실행
remove_first_row_for_dates()
