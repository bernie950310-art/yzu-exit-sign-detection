# YZU 校園緊急出口標誌偵測系統

本專題以元智大學校園中的緊急出口標誌(綠底白色奔跑人形之逃生指示標誌)為偵測目標,使用 YOLO11 物件偵測模型,透過自行收集與標註的校園資料集訓練而成。

## 專題資訊
- 課程:EEB215A 電腦視覺與影像處理概論
- 姓名 / 學號:李柏鋒 / s1130426

## 系統效能
| 指標 | 數值 |
|---|---|
| mAP50 | 0.975 |
| mAP50-95 | 0.791 |
| Precision | 1.0 |
| Recall | 0.977 |

## 資料集
- 自行於元智大學校園各棟建築拍攝並標註,共 230 張影像,單一類別 `exit_sign`。
- 使用 Roboflow 標註,匯出為 YOLOv11 格式。

## 環境需求
- Python 3.10+
- 安裝套件:`pip install ultralytics`

## 如何執行偵測
1. 下載本 repo 的 `best.pt`。
2. 準備一段要偵測的影片,命名為 `demo.mp4`,放在同一資料夾。
3. 執行:`python detect.py`
4. 偵測結果(畫好框的影片)會輸出到 `runs/detect/predict/` 資料夾。

## 展示影片
https://youtube.com/shorts/SUfJC06D2Hk?feature=share

## 使用工具與參考
- Ultralytics YOLO11:https://docs.ultralytics.com
- Roboflow(資料標註):https://roboflow.com
