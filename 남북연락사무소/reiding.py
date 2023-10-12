import re
import os

# 현재 디렉토리의 파일 목록을 가져옵니다.
files = os.listdir()

for filename in files:
    # 파일 이름이 숫자-지명.txt 형식인지 확인합니다.
    match = re.match(r'(\d+)-.+.txt', filename)
    if match:
        number = int(match.group(1))
        # 숫자가 935 이상인 경우에만 내용을 변경합니다.
        if number >= 935:
            # 파일을 엽니다.
            with open(filename, 'r+', encoding='UTF8') as file:
                content = file.read()
                # id=XXX 또는 name="STATE_XXX" 패턴을 찾습니다.
                content = re.sub(r'(id=|name="STATE_)(\d+)', lambda m: m.group(1) + str(int(m.group(2)) + 26), content)
                # 변경된 내용으로 파일을 덮어씁니다.
                file.seek(0)
                file.write(content)
                file.truncate()
