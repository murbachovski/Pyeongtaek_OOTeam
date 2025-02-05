# 필요한 라이브러리 임포트
import cv2  # OpenCV 라이브러리로 카메라에서 이미지를 캡처하고 저장하는 데 사용
from datetime import datetime  # 날짜와 시간을 다루는 라이브러리
import os  # 파일 및 디렉토리 작업을 위한 라이브러리
import time  # 시간 관련 함수들을 제공하는 라이브러리
import pyfiglet

def message_pyfiglet(sentence):
    sentence = pyfiglet.figlet_format(sentence)
    print(sentence)
    
# 초기 마지막 촬영 시간 (Epoch 기준으로 0으로 설정)
last_capture_time = 0

def capture_image(im0):
    global last_capture_time
    # 사진 찍기 간격 설정 (초 단위)
    CAPTURE_INTERVAL = 10
    # 설정된 사진 촬영 간격 출력
    print(f"사진 촬영 간격: {CAPTURE_INTERVAL}초")
    # 현재 시간 (초 단위, Epoch 기준으로 반환)
    current_time = time.time()
    print(f"current_time: {current_time}")
    # 저장 디렉토리 설정
    SAVE_DIR = "captured_images"
    # 현재 시간으로 파일 이름 생성 (YYYYMMDD_HHMMSS 형식)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # 파일 경로 설정
    file_path = os.path.join(SAVE_DIR, f"photo_{timestamp}.jpg")
    # 디렉토리가 없으면 생성, 이미 존재하면 무시
    os.makedirs(SAVE_DIR, exist_ok=True)
    
    if current_time - last_capture_time >= CAPTURE_INTERVAL:
        # 설정된 간격을 지났을 때만 사진 촬영
        message_pyfiglet("Start to get data")
        print(f"current_time: {current_time}")
        print(f"last_capture_time: {last_capture_time}")
        print(f"current_time - last_capture_time: {current_time - last_capture_time}")
        print(f"CAPTURE_INTERVAL: {CAPTURE_INTERVAL}")
        
        # 이미지를 저장
        cv2.imwrite(file_path, im0)
        
        # 저장된 사진의 경로 출력
        message_pyfiglet("Success to get data")
        message_pyfiglet(f"Path to get data: {file_path}")
        
        # 마지막 촬영 시간을 현재 시간으로 갱신
        print(f"last_capture_time: {last_capture_time}")
        last_capture_time = current_time
        print(f"last_capture_time: {last_capture_time}")
    else:
        message_pyfiglet("It's not time to get data")
        print("데이터 수집 시간이 아닙니다.")
        
        
    # CPU 과부하 방지를 위해 약간의 대기
    time.sleep(1)  # 1초마다 확인하여 간격이 지난 경우에만 촬영