from flask import Flask, Response
import cv2
from region_yolo import create_region_counter, count_objects
from alarm_yolo import create_security_alarm, monitor_security
from data_yolo import capture_image
from async_yolo import async_capture

app = Flask(__name__)

# 비디오 캡처 설정
cap = cv2.VideoCapture("rtsp://210.99.70.120:1935/live/cctv027.stream")

# 비디오의 너비, 높이 값 가져오기
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 영역 설정
region_points = {
    "region-01": [(102, 117), (56, 367), (5, 400), (18, 473), (167, 439), (209, 354), (142, 111)]
}

# 모델 및 이메일 설정
model_path = "yolo11n.pt"
from_email = "ai.murbachovski@gmail.com"
password = "hqsu venx bbba zokx"
to_email = "ai.murbachovski@gmail.com"

# 변수 설정
classes = 0

# 객체 카운터 및 보안 감지 시스템 초기화
region_counter = create_region_counter(region_points, model_path, classes=classes)
security_alarm = create_security_alarm(model_path, from_email, password, to_email)

# 비디오 프레임 생성 함수
def generate_frames():
    while cap.isOpened():
        success, im0 = cap.read()
        if not success:
            print("⚠️ 비디오 스트림을 읽을 수 없습니다. 재시도 중...")
            cap.set(cv2.CAP_PROP_POS_FRAMES, "rtsp://210.99.70.120:1935/live/cctv027.stream")  # 스트림을 다시 시도
            continue
        
        # 데이터 수집 (비동기 이미지 저장)
        async_capture(im0)
        
        # 객체 감지
        process_video_frame(im0)
        
        # 프레임을 JPEG로 인코딩
        ret, buffer = cv2.imencode('.jpg', im0)
        if not ret:
            continue
        
        frame = buffer.tobytes()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# 프레임 처리 및 객체 감지, 보안 알람 실행 함수
def process_video_frame(im0):
    # 객체 감지 및 보안 감지 적용
    im0, rc = count_objects(region_counter, im0)

    if im0 is None:
        print("⚠️ 객체 감지 과정에서 오류 발생. 원본 프레임을 유지합니다.")
        return

    print(f"현재 구역에서 탐지된 사람의 수 : {rc} 명 입니다.")

    # 영상에 탐지된 사람 수 표시
    text = f"Detected: {rc} persons"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (0, 255, 0)  # 초록색
    thickness = 2
    position = (50, 50)  # 왼쪽 상단
    cv2.putText(im0, text, position, font, font_scale, font_color, thickness, cv2.LINE_AA)

    # 특정 조건 시 보안 감지 실행
    if rc is not None and rc >= 1:
        im0 = monitor_security(security_alarm, im0)
        print(f"🔔 알람을 보냈습니다.{security_alarm}")

# Flask 라우트 정의: 실시간 비디오 스트리밍을 위한 엔드포인트
@app.route('/')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# 애플리케이션 실행
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
