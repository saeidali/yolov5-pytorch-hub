import torch
from cv2 import cv2

model = torch.hub.load('yolov5', 'yolov5s', pretrained=True,source='local')
img = 'zidane.jpg'
frame = cv2.imread(img)
detections = model(frame[..., ::-1])
results = detections.pandas().xyxy[0].to_dict(orient="records")
for result in results:
                con = result['confidence']
                cs = result['class']
                x1 = int(result['xmin'])
                y1 = int(result['ymin'])
                x2 = int(result['xmax'])
                y2 = int(result['ymax'])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255,0,0), 2)
cv2.imshow("winname", frame)
k = cv2.waitKey(6000)