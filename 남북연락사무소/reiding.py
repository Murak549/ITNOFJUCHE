import re
import os

# 현재 디렉토리의 파일 목록을 가져옵니다.
files = os.listdir()

# 입력 파일 이름과 출력 파일 이름을 지정합니다.
input_filename = 'input.txt'
output_filename = 'output.txt'

# 입력 파일을 엽니다.
with open(input_filename, 'r') as infile:
    # 출력 파일을 씁니다.
    with open(output_filename, 'w') as outfile:
        # 입력 파일의 각 줄을 읽습니다.
        for line in infile:
            # id=XXX 또는 name="STATE_XXX" 패턴을 찾습니다.
            match = re.search(r'(id=|name="STATE_)(\d+)', line)
            if match:
                # 숫자 부분을 찾아서 26을 더합니다.
                number = int(match.group(2))
                if number >= 909:
                    new_number = str(number + 26)
                    # 원래 줄에서 숫자 부분을 새 숫자로 교체합니다.
                    new_line = line.replace(match.group(2), new_number)
                    # 변경된 줄을 출력 파일에 씁니다.
                    outfile.write(new_line)
                else:
                    # 숫자가 909 미만인 경우 줄을 그대로 복사합니다.
                    outfile.write(line)
            else:
                # 패턴이 없는 경우 줄을 그대로 복사합니다.
                outfile.write(line)
