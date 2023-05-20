from pydub import AudioSegment

def convert_mp3_to_ogg(mp3_file, ogg_file):
    # MP3 파일 로드
    audio = AudioSegment.from_mp3(mp3_file)
    
    # OGG 파일로 변환하여 저장
    audio.export(ogg_file, format="ogg")

mp3_file = input("mp3 파일이름(확장자 제외)")+".mp3"
ogg_file = mp3_file+".ogg"
convert_mp3_to_ogg(mp3_file, ogg_file)