import re
import os

# 현재 디렉토리의 파일 목록을 가져옵니다.
files = os.listdir()

for filename in files:
    # 파일을 엽니다.
    with open(filename, 'r+', encoding='UTF8') as file:
        lines = file.readlines()
        # 변경된 내용을 저장할 리스트를 만듭니다.
        new_lines = []
        for line in lines:
            # manpower= 행은 제외합니다.
            if not line.strip().startswith('manpower=' or 'manpower ='):
                # 13256 이상의 숫자를 찾아서 16를 더합니다.
                line = re.sub(r'\b(\d{5,})\b', lambda m: str(int(m.group(1)) + 16 if int(m.group(1)) >= 13256 else m.group(1)), line)
            new_lines.append(line)
        # 변경된 내용으로 파일을 덮어씁니다.
        file.seek(0)
        file.writelines(new_lines)
        file.truncate()
