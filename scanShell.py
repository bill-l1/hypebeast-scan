import io
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "1edd0d88ad8d.json"

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

##from SimpleCV import *
##
##prompt = raw_input("Are you taking a photo? (y/n)")
##
##if prompt == "y":
##    print "left click to take photo"
##    cam = Camera()
##    disp = Display()
##
##    while disp.isNotDone():
##        img = cam.getImage()
##        if disp.mouseLeft:
##            break
##        img.save("/home/francisco/Desktop/pics/itjustworks.jpg")
##        fileInput = "itjustworks.jpg"
##
##else:

fileInput = raw_input("Enter file name: ")

# Instantiates a client
client = vision.ImageAnnotatorClient()

brandFile = open("brands.txt", "r")
brands = brandFile.read().lower().split('\n')
brands = brands[:-1]
#print brands
brandFile.close()

tags = ["hypebeast", "streetwear"]

webBrands = {}
entities = []
hypeScore = 0

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'static/pics/' + fileInput)

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.web_detection(image=image)
notes = response.web_detection

print " "

for entity in notes.web_entities:
    if entity.description.lower() in brands:
        webBrands[entity.description] = entity.score
    print entity.description
    entities.append(entity.description.lower())

print " "



for tag in tags:
    if tag in entities:
        print "'" + tag +"'" + " tag detected [+500]"
        hypeScore += 500

print " "

if len(webBrands) > 0:
    print "Brands Detected:"
else:
    print "No hypebeast brands detected..."
    
for brand in webBrands:
    hypeScore += 400
    print "Brand:", brand, "    Score: ", webBrands[brand], "[+400]"

print " "
print "Final Hypebeast Score:", hypeScore

#print "\n\n"
#print webBrands

