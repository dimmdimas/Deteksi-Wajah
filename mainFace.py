import cv2, os

cam = cv2.VideoCapture(2)
cam.set(3, 640)
cam.set(4, 480)
faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faceID = input("Masukan Face ID yang akan direkam datanya: ")
print ('Tatap wajah anda ke dalam webcam')
ambilData = 1
wajahDir = 'datawajah'
while True:
    retV,frame = cam.read()
    abuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceDetector.detectMultiScale(abuAbu, 1.3, 5)
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 255), 2)

        namaFile = 'wajah.'+str(faceID)+'.'+str(ambilData)+'.jpg'
        cv2.imwrite(wajahDir+'/'+namaFile, frame)
        ambilData += 1
    # cv2.imshow('Web', frame)
    cv2.imshow('WebAbu', abuAbu)

    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break
    elif ambilData>40:
        break

print('Pengambilan selesai')
cam.release()
cv2.destroyAllWindows()