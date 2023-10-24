import logging

import azure.functions as func
from TfLiteDetectionTrigger.tflite_detection_img import detect_image


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        if req_body:
            # Your code to process the POST data
            print(f"Received data")

            img_base64 = req_body['imgBase64']

            res = detect_image(img_base64)

            return func.HttpResponse("Data processed successfully", status_code=200)
        else:
            return func.HttpResponse("No data received", status_code=400)
    except Exception as e:
        return func.HttpResponse(str(e), status_code=500)
