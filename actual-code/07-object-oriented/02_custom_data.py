camera_1 = {
  "iso": 1250,
  "f-stop": 5.0,
  "aspect_ratio": "16:9",
  "location": "birmingham_studio_one",
  "zoom_level": 1
}

def zoom_in(camera):
  camera["zoom_level"] = camera.get("zoom_level", 0) + 1

zoom_in(camera_1)
print(camera_1)

camera_2 = {
  "zom_level": 1,
  "iso": 1250
}

zoom_in(camera_2)

# object -> __init__()
class Camera:
  def __init__(self, zoom, location):
    self.zoom_level = zoom
    self.location = location

  def zoom_in(self):
    self.zoom_level += 1.1
    return self.zoom_level

  def __str__(self):
    return f"Camera in {self.location}, currently at zoom level {self.zoom_level}"




# creating an new object, instantiating, "newing-up"
camera_3 = Camera(zoom=1, location="glasgow_studio_4")  # safer data types  


camera_3.zoom_in()
camera_3.zoom_in()

print(camera_3.zoom_level)
print(camera_3.location)

# print -> __str__
print(camera_3)




