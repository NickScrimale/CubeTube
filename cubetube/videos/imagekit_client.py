import os
from imagekitio import ImageKit


def get_imagekit_client():
    return ImageKit()


def upload_video(file_data: bytes, file_name: str, folder: str = "videos") -> dict:
    public_key = os.environ.get("IMAGEKIT_PUBLIC_KEY")

    client = get_imagekit_client()

    response = client.files.upload(
        file_data=file_data,
        
    )