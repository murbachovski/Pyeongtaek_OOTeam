import threading
from data_yolo import capture_image

def async_capture(im0):
    thread = threading.Thread(
        target=capture_image,
        args=(im0,))
    thread.daemon = True
    thread.start()
    