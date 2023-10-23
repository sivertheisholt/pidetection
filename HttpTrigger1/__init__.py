import logging

import azure.functions as func
from HttpTrigger1.tblite_detection_img import detect_image

import requests


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        url = "https://raw.githubusercontent.com/protocolbuffers/protobuf/main/python/google/protobuf/internal/builder.py"
        local_path = "/azure-functions-host/workers/python/3.9/LINUX/X64/google/protobuf/internal"

        response = requests.get(url)

        if response.status_code == 200:
            with open(local_path, 'wb') as file:
                file.write(response.content)
            print(f"File downloaded and saved to {local_path}")
        else:
            print(
                f"Failed to download the file. Status code: {response.status_code}")

        req_body = req.get_json()
        if req_body:
            # Your code to process the POST data
            print(f"Received data")

            img_base64 = req_body['imgBase64']

            res = detect_image(img_base64)

            return func.HttpResponse(res, mimetype="text/plain")
        else:
            return func.HttpResponse("No data received", status_code=400)
    except Exception as e:
        return func.HttpResponse(str(e), status_code=500)
