import cv2 as cv

cap = cv.VideoCapture(0)

frame_list = []
full_list = []

width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
 
forward = cv.VideoWriter('forward.mp4', cv.VideoWriter_fourcc(*'mp4v'),20,(width,height))
backward = cv.VideoWriter("backward.mp4", cv.VideoWriter_fourcc(*'mp4v'), 20, (width, height))
full = cv.VideoWriter("full.mp4", cv.VideoWriter_fourcc(*'mp4v'), 20, (width, height))

while True:
    ret, frame = cap.read()
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    forward.write(frame)
    cv.imshow('frame', frame)
cap.release()
forward.release()
    
cap1 = cv.VideoCapture("forward.mp4")
check, vid = cap1.read()

while (check == True):
    check, vid = cap1.read()
    frame_list.append(vid)
    full_list.append(vid)
frame_list.pop()
frame_list.reverse()

for frame1 in frame_list:
    backward.write(frame1)
    full_list.append(frame1)
    
for frame2 in full_list:
    full.write(frame2)  

cap1.release()
backward.release()
full.release()
cv.destroyAllWindows()
