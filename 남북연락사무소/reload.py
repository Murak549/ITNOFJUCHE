import os
import shutil

def find_and_move_conflict_files(folder_a, folder_b, conflict_folder):
    # A 폴더의 파일 목록 가져오기
    files_a = set(os.listdir(folder_a))

    # B 폴더의 파일 목록 가져오기
    files_b = set(os.listdir(folder_b))

    # 겹치는 파일 찾기
    conflicting_files = files_a.intersection(files_b)

    # "C:\conflict" 폴더가 없으면 생성
    if not os.path.exists(conflict_folder):
        os.makedirs(conflict_folder)

    # 겹치는 파일을 "C:\conflict" 폴더로 이동
    for file in conflicting_files:
        src_path_a = os.path.join(folder_a, file)
        src_path_b = os.path.join(folder_b, file)
        dest_path = os.path.join(conflict_folder, file)

        # 파일을 "C:\conflict" 폴더로 이동
        shutil.move(src_path_a, dest_path)

        # B 폴더의 겹치는 파일도 이동 (똑같은 파일이 존재하는 경우)
        if os.path.exists(src_path_b):
            shutil.move(src_path_b, dest_path)

if __name__ == "__main__":
    # A 폴더와 B 폴더의 경로 설정
    folder_a = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Hearts of Iron IV"
    folder_b = "C:\\Users\\sk010\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\juche"
    
    # 겹치는 파일을 옮길 폴더 경로 설정
    conflict_folder = "C:\\conflict"

    # 겹치는 파일을 찾아서 이동
    find_and_move_conflict_files(folder_a, folder_b, conflict_folder)
