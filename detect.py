from ultralytics import YOLO

# 载入训练好的模型
model = YOLO("best.pt")

# 对影片进行侦测(把 demo.mp4 换成你的影片档名)
# 侦测结果(画好框的影片)会存到 runs/detect/predict/
model.predict(source="demo.mp4", save=True, conf=0.4)

# 若要使用即时摄影机侦测,改用下面这行:
# model.predict(source=0, show=True, conf=0.4)
