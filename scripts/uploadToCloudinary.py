import cloudinary

from cloudinary.uploader import upload

from credentials import cloudinary as cld

cloudinary.config(
  cloud_name = cld['name'],
  api_key = cld['key'],
  api_secret = cld['secret'],
  secure = True
)


def UploadPhoto(path):
    x = upload(path)
    print('Photo Uploaded',path)
    # return "thiw will bw url"
    return x['url']