# YOLO 모델과 OpenCV 라이브러리, os 라이브러리 임포트
from ultralytics import YOLO  
import cv2  
import os  

# 1. YOLO 모델 로드
model = YOLO("yolo11x.pt")

# 2. 이미지 폴더와 결과 저장 폴더 설정
image_folder = "captured_images"  
output_image_folder = "results_images"  
output_folder = "results_labels"  

# 3. 결과 저장 폴더 생성
os.makedirs(output_folder, exist_ok=True)  
os.makedirs(output_image_folder, exist_ok=True)  

# 4. 이미지 파일 목록 가져오기
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

# 5. 각 이미지에 대해 라벨링 수행
for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)  

    # OpenCV로 이미지 로드 후 크기 확인
    image = cv2.imread(image_path)
    img_height, img_width = image.shape[:2]  # 이미지 높이, 너비 가져오기

    # 6. 모델로 예측 수행
    results = model(image_path, classes=0)  
    
    # 7. 바운딩 박스, 레이블, 확신도 가져오기
    boxes = results[0].boxes.xyxy  # 바운딩 박스 좌표 (x1, y1, x2, y2)
    labels = results[0].boxes.cls  
    confidences = results[0].boxes.conf  

    # 8. 정규화된 좌표를 저장할 텍스트 파일 생성
    label_file_path = os.path.join(output_folder, f"{os.path.splitext(image_file)[0]}.txt")
    with open(label_file_path, "w") as label_file:  
        for box, label, confidence in zip(boxes, labels, confidences):
            # 바운딩 박스 좌표
            x_center = (box[0] + box[2]) / 2 / img_width  # 정규화된 중심 x 좌표
            y_center = (box[1] + box[3]) / 2 / img_height  # 정규화된 중심 y 좌표
            width = (box[2] - box[0]) / img_width  # 정규화된 너비
            height = (box[3] - box[1]) / img_height  # 정규화된 높이
            
            # YOLO 형식으로 저장 (클래스 ID, x_center, y_center, width, height)
            label_file.write(f"{int(label)} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")
    
    # 9. 바운딩 박스와 레이블이 그려진 결과 이미지 저장
    image_with_labels = results[0].plot()  
    result_image_path = os.path.join(output_image_folder, f"{os.path.splitext(image_file)[0]}.jpg")  
    cv2.imwrite(result_image_path, image_with_labels)  

    # 10. 진행 상황 출력
    print(f"라벨링 완료: {image_file}")  
    print(f"결과 이미지 저장 경로: {result_image_path}")  

# 11. 모든 이미지 라벨링 완료
print("모든 이미지에 대한 자동 라벨링이 완료되었습니다.")  
