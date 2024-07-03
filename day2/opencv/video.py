import cv2 as cv

cap = cv.VideoCapture(0)
# cap 设备状态
while cap.isOpened():
    # ret 是否读取成功
    # frame一帧图片
    # 图像转换（被转换的图片，转换模式）
    ret, frame = cap.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    if not ret:
        print("can't open img")
        break
    # (窗口名称，图片)
    cv.imshow('img', frame)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
    # cv.waitkey(0)
    
