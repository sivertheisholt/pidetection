# Pidetection

An Azure Function designed to perform object detection using a pre-trained machine learning model. The function accepts a base64-encoded image via a POST request trigger, processes the image to detect objects, and then forwards the results to a web application for display or further action.

The image is sent to the function in a POST request, where it's decoded and passed to the model for inference. The model identifies objects within the image, returning information such as object labels, bounding boxes, and confidence scores.

Once the detection is complete, the results are packaged and sent to the web application, which could display the detected objects visually or integrate the data into other workflows. The entire process is serverless, allowing for scalable and efficient object detection without the need to manage underlying infrastructure.


