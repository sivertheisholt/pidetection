import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        if req_body:
            # Your code to process the POST data
            print(f"Received data: {req_body}")

            img_base64 = req_body['imgBase64']

            return func.HttpResponse(img_base64, mimetype="text/plain")
        else:
            return func.HttpResponse("No data received", status_code=400)
    except Exception as e:
        return func.HttpResponse(str(e), status_code=500)

    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse(
        "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
        status_code=200
    )
