import cv2

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 5)
    for (x, y, w, h) in faces:
        print(x, y, w, h)
        ri_cinza = gray[y:y+h, x:x+w]
        img_item = "teste.png"
        cv2.imwrite(img_item, ri_cinza)
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()