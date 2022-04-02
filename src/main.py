from fastapi import FastAPI, UploadFile, File, HTTPException, status, Header

from handler import handle_file, handle_url
from predict import predict_model

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/predict_url")
async def predict_url(url: str):
    model_input = handle_url(url)
    model_output = predict_model(model_input)
    return model_output


def validate_image_content(content_type: str = Header(...)):
    """Require request MIME-type to be application/vnd.api+json"""

    content_main_type = content_type.split("/")[0]
    if content_main_type != "image":
        raise HTTPException(
            status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            f"Unsupported media type: {content_type}."
            " It must be image/",
        )


@app.post("/predict_file")
async def predict_file(upload_file: UploadFile = File(...)):
    validate_image_content(upload_file.content_type)
    model_input = handle_file(await upload_file.read())
    model_output = predict_model(model_input)
    return model_output
