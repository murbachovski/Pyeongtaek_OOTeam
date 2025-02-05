<p align="center">
  <img src="https://github.com/user-attachments/assets/3a89f014-558f-4191-ba25-583971a1c034" width="300">
  <img src="https://github.com/user-attachments/assets/c2d4d830-6141-4da8-9952-28e750ab1c43" width="300">
</p>

## 평택대학교 프로젝트
```
인파 밀집 시스템 개발
```

## 팀 현황
1. [Pyeongtaek_AI_YOLO_Team](https://github.com/rivermin01/Pyeongtaek_AI_YOLO_Team/tree/Develop)<br>
2. [pyeongtaek_A](https://github.com/dksengh/pyeongtaek_A/tree/main)<br>
3. [PTU-VISION](https://github.com/PTU-hehyj/PTU-VISION/tree/Develope)<br>

## 구성원(예시
```
팀장: 김대진
팀원: 김대진, 김대진
```

## 설명(예시
```
YOLO를 활용한...
```

## 환경 셋팅(예시
The code requires python>=3.7 and we use torch==1.10.2 and torchvision==0.11.3. To visualize the results, matplotlib>=3.5.1 is also required.
```
python 3.7
pytorch == 1.10.2
torchvision == 0.11.3
matplotlib==3.5.1
```

## 환경 설치(예시
```
pip install -r requirements.txt
```

## 실행(예시
```
cd team_project
python3 app.py
```

## CCTV 접근
1. [카카오맵](https://map.kakao.com/?nil_profile=title&nil_src=local)
<p align="center">
  <img width="1081" alt="Image" src="https://github.com/user-attachments/assets/2be59a8d-c2cc-4867-9db1-d255f4de3303" width="300">
</p>

### 접근 방법
```
카카오맵 CCTV 접근 => 소스코드(F12) 확인 => 비디오 링크 복사 => cv2.CaptureVideo() 적용 => 영상 스트리밍
```
### 예시 링크
```
cap = cv2.VideoCapture("https://cctvsec.ktict.co.kr/6246/cCCtjN+N+EnDEdCu9wHS00X5iOMXIc41FwpwasljdCsrysX/jGzlP6b54WADcjaY")
```

## 면적 측정

1. [구글맵](https://www.google.co.kr/maps/?entry=ttu&g_ep=EgoyMDI1MDIwMi4wIKXMDSoASAFQAw%3D%3D)
<p align="center">
  <img src="https://github.com/user-attachments/assets/46a67170-4d6c-4a3b-9f64-1d9f5f8c2a98" width="300">
</p>

2. [네이버지도](https://map.naver.com/p?c=15.00,0,0,0,dh)
<p align="center">
  <img src="https://github.com/user-attachments/assets/02d5db1d-1d19-4c20-b180-25c9655469a7" width="300">
</p>

3. [카카오맵](https://map.kakao.com/?nil_profile=title&nil_src=local)
<p align="center">
  <img src="https://github.com/user-attachments/assets/5aa664df-7d71-4a70-88a1-1ea83d45786f" width="300">
</p>

### 설명
```
각 웹에서 거리 및 면적 측정 가능
```

## ~~OC_SORT 모델 활용~~
```
https://github.com/noahcao/OC_SORT/tree/master
```

## YOLO custom_datasets 경로 셋팅
```
coco8.yaml => path : coco8 폴더 경로, train : train 폴더 경로, val : val 폴더 경로
model.train(data='coco8.yaml 파일 경로')
```

## Background images
<img src="https://github.com/user-attachments/assets/052d795a-8361-4905-b325-8124e7ba729d" width="600">

```
FP => 거짓 탐지 => 오탐을 줄일 수 있다.
```
## Data Augmentation
<p align="center">
  <img src="https://github.com/user-attachments/assets/81c866a3-c39d-4cb4-89d6-a7bc818e7a65" width="600">
</p>

## 파이썬 경고음 넣기
[더미 경고음 사이트](https://pixabay.com/ko/sound-effects/search/%EA%B2%BD%EA%B3%A0%EC%9D%8C/)

```
# MAC
import os
os.system(afplay ./alarm.mp3)

# MAC(비동기)
import subprocess
subprocess.Popen(["afplay", "./alarm.mp3"])

# Winodws
pip install playsound
from playsound import playsound
playsound('./alarm.mp3')
```
