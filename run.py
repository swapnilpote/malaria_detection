import cv2
import json
import numpy as np
import requests

def prediction():
    img = cv2.imread("data/Parasitized/C33P1thinF_IMG_20150619_114756a_cell_179.png")
    img = cv2.resize(img, (110, 110))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = np.reshape(img, (1, 110, 110, 3))

    headers = {"Content-Type": "application/json"}
    payloads = {"signature_name": "serving_default", "inputs": {"input_1": img.tolist()}}
    tfserving_response = requests.post("http://localhost:8501/v1/models/malaria:predict", headers=headers, data=json.dumps(payloads))

    return tfserving_response.json()


if __name__ == "__main__":
    response = prediction()
    print(response)