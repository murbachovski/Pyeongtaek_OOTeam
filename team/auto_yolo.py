# YOLO 모델과 OpenCV 라이브러리, os 라이브러리 임포트
from ultralytics import YOLO  # YOLO 모델을 불러오기 위한 라이브러리
import cv2  # OpenCV 라이브러리 (이미지 처리 및 저장을 위해 사용)
import os  # 파일 및 디렉토리 작업을 위한 os 라이브러리

# 1. YOLO 모델 로드 (미리 학습된 YOLO 모델을 불러옴)
model = YOLO("yolo11x.pt")  # "yolo11n.pt"라는 YOLO 모델 파일을 로드. 해당 모델은 객체 감지 모델로 학습된 상태임.

# 2. 이미지 폴더와 결과를 저장할 폴더 경로 설정
image_folder = "인풋 이미지 폴더 경로"  # 원본 이미지들이 저장된 폴더 경로
output_image_folder = "결과 이미지 저장 폴더 경로"  # 라벨링된 이미지를 저장할 폴더 경로
output_folder = "라벨링 저장 폴더 경로"  # 라벨 텍스트 파일을 저장할 폴더 경로

# 3. 결과 저장 폴더가 없으면 생성
os.makedirs(output_folder, exist_ok=True)  # 'output_labels' 폴더가 없으면 생성
os.makedirs(output_image_folder, exist_ok=True)  # 'output_images' 폴더가 없으면 생성

# 4. 이미지 파일 목록 가져오기 (.jpg, .jpeg, .png 파일만)
# image_folder 폴더 내에서 .jpg, .jpeg, .png 파일만 목록에 추가
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

# 5. 각 이미지에 대해 라벨링 수행
# 가져온 이미지 파일들에 대해 하나씩 처리
for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)  # 각 이미지 파일의 전체 경로를 생성
    
    # 6. 모델로 예측 (이미지에 대해 객체 감지 수행)
    results = model(image_path, classes=0)  # 모델을 사용하여 이미지를 분석, 객체 감지 결과를 반환
    
    # 7. 바운딩 박스, 레이블, 확신도 가져오기
    # results[0]은 첫 번째 이미지의 예측 결과
    boxes = results[0].boxes.xyxy  # 바운딩 박스 좌표 (x1, y1, x2, y2) 형태로 저장됨
    labels = results[0].boxes.cls  # 객체 클래스 레이블 (0부터 시작하는 클래스 ID)
    confidences = results[0].boxes.conf  # 각 객체의 확신도 (confidence score)

    # 8. 라벨링 결과를 텍스트 파일로 저장
    # 이미지 파일 이름을 기반으로 동일한 이름의 텍스트 파일을 생성
    label_file_path = os.path.join(output_folder, f"{os.path.splitext(image_file)[0]}.txt")
    with open(label_file_path, "w") as label_file:  # 텍스트 파일을 쓰기 모드로 열기
        # 바운딩 박스, 레이블, 확신도에 대해 순차적으로 처리
        for box, label, confidence in zip(boxes, labels, confidences):
            # YOLO 형식으로 바운딩 박스를 변환 (x_center, y_center, width, height) 형태로 변환
            x_center = (box[0] + box[2]) / 2  # 바운딩 박스의 중심 x 좌표 계산
            y_center = (box[1] + box[3]) / 2  # 바운딩 박스의 중심 y 좌표 계산
            width = box[2] - box[0]  # 바운딩 박스의 너비 계산
            height = box[3] - box[1]  # 바운딩 박스의 높이 계산
            
            # YOLO 형식에 맞춰 (클래스 ID, x_center, y_center, width, height)을 0-1 스케일로 저장
            label_file.write(f"{int(label)} {x_center} {y_center} {width} {height}\n")
    
    # 9. 바운딩 박스와 레이블이 그려진 결과 이미지 저장
    # 결과 이미지에 바운딩 박스와 레이블을 그려서 이미지 생성
    image_with_labels = results[0].plot()  # 바운딩 박스와 레이블이 그려진 이미지를 반환
    result_image_path = os.path.join(output_image_folder, f"{os.path.splitext(image_file)[0]}_labeled.jpg")  # 결과 이미지 파일 경로 설정
    cv2.imwrite(result_image_path, image_with_labels)  # 라벨링된 이미지를 파일로 저장

    # 10. 진행 상황 출력
    print(f"라벨링 완료: {image_file}")  # 현재 처리한 이미지 파일 이름을 출력
    print(f"결과 이미지 저장 경로: {result_image_path}")  # 결과 이미지가 저장된 경로를 출력

# 11. 모든 이미지에 대해 라벨링 완료
print("모든 이미지에 대해 자동 라벨링이 완료되었습니다.")  # 모든 이미지에 대한 라벨링이 끝났음을 알리는 메시지 출력
