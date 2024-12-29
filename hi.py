from PIL import Image
import requests # type: ignore
from io import BytesIO

url = "https://media.giphy.com/media/OccMlQrNO0YU4zFchY/giphy.gif"
response = requests.get(url)
img = Image.open(BytesIO(response.content))

img.show()
