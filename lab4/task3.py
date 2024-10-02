import cv2

video_file_path = '../lab4/Videos/Video.mp4'

cap = cv2.VideoCapture(video_file_path)
video_file_name = video_file_path.split('/')[-1]
fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)
cv2.namedWindow('Video', cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()

    if ret:
        cv2.putText(frame, f'File: {video_file_name}', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.putText(frame, f'FPS: {fps:.2f}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.imshow('Video', frame)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
