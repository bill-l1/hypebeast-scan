import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

def scanImg(fileURL):

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "1edd0d88ad8d.json"
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    brandFile = open("brands.txt", "r")
    brands = brandFile.read().lower().split('\n')
    brands = brands[:-1]
    #print brands
    brandFile.close()

    tags = ["hypebeast", "streetwear", "japan street fashion"]

    webBrands = {}
    entities = []
    tagScores = {}
    brandScores = {}
    score = 0;
    
    if os.path.isfile('static/pics/' + fileURL):
        # The name of the image file to annotate
        file_name = os.path.join(
            os.path.dirname(__file__),
            'static/pics/' + fileURL)

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
                tagScores[tag] = 500
                score += 500

        print " "

        if len(webBrands) > 0:
            print "Brands Detected:"
        else:
            print "No hypebeast brands detected..."
            
        for brand in webBrands:
            print "Brand:", brand, "    Score: ", webBrands[brand], "[+400]"
            brandScores[brand] = 400
            score += 400

        print " "
        print "Final Hypebeast Score:", score
        
        title = "foobar"

        if score <= 0:
            title = "not even close"
        elif score < 500:
            title = "junior hypeman"
        elif score < 900:
            title = "hypey"
        elif score < 1300:
            title = "certified hypebeast"
        else:
            title = "hype god"
        
        return [tagScores, brandScores, score, title]

    else:

        return None
