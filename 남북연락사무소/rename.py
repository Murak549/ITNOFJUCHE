import os

# 현재 디렉토리의 파일 목록을 가져옵니다.
files = os.listdir()

for file in files:
    # 파일 이름을 '-'를 기준으로 분리합니다.
    parts = file.split('-')
    
    # 첫 번째 부분이 숫자인지 확인합니다.
    if parts[0].isdigit():
        number = int(parts[0])
        
        # 숫자가 909 이상인 경우에만 이름을 변경합니다.
        if number >= 909:
            # 숫자에 25를 더하고, 나머지 부분은 그대로 둡니다.
            new_name = str(number + 26) + '-' + '-'.join(parts[1:])
            
            # 파일 이름을 변경합니다.
            os.rename(file, new_name)
