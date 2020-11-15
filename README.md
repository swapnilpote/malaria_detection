# malaria_detection
Malaria detection using convolutional neural network

#### build docker container using --mount type=bind
docker run -d -p 8501:8501 --mount type=bind,source="/mnt/c/Users/Scooby Doo/Projects/malaria_detection/tf_serving",target=/models/malaria -e MODEL_NAME=malaria -t tensorflow/serving

### restful call way
import requests, json, cv2

img = cv2.imread(filepath)
img = cv2.resize(img, (110, 110))
img = img.reshape((1, 110, 110, 3))

headers = {"Content-Type": "application/json"}
payload = {"signature_name": "serving_default", "inputs": {"input_1":img.tolist()}}
url = "http://localhost:8501/v1/models/malaria:predict"

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
response.content