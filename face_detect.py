import cv2

SAVEDIR = ""

def face_detect(filename):

    faceCascade = cv2.CascadeClassifier('./opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')

    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    faces = faceCascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255,0,0), 2)
    
    cv2.imwrite('detected_face.jpg', image)
    
    if len(faces) == 0:
        is_detected = False
    else:
        is_detected = True
    
    return SAVEDIR + '/detected_face.jpg', is_detected

'''
test code
if __name__ == '__main__':
    print(face_detect('face.jpg')[1])
'''