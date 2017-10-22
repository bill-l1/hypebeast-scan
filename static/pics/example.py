from SimpleCV import *

__author__ = 'yuva'
def main():
    img = Image("/home/francisco/Desktop/pics/group.jpg")
    print img.listHaarFeatures()
    # faces = img.findHaarFeatures("haarcascade_frontalface_alt.xml")
    faces = img.findHaarFeatures("face2.xml")
    #faces = img.findHaarFeatures("haarcascade_frontalface_default.xml")
    scalesize = 1
    size = 0
    if faces:
        for face in faces:
            print "I found a face at " + str(face.coordinates())
            print face.x , face.y,face.width() , face.height()
            print face.topLeftCorner()
            img.drawRectangle(face.topLeftCorner()[0],face.topLeftCorner()[1] , face.width() , face.height())
            img.drawCircle(face.coordinates(),face.width()/2 , color=(0,255,0) , thickness=2)

            img.save(filename='detected')
        print len(faces)


main()
