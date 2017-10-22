from SimpleCV import *

hypeShirt = Image("/home/francisco/Desktop/pics/supreme.jpg")
whiteShirt = Image("/home/francisco/Desktop/pics/white.jpg")
bapeShirt = Image("/home/francisco/Desktop/pics/bape.jpg")

whiteCrop = whiteShirt.scale(800, 800)
hypeCrop = hypeShirt.scale(800, 800)
bapeCrop = bapeShirt.scale(800, 800)

logoCrop = hypeCrop.colorDistance(Color.RED)

sub = whiteCrop - bapeCrop

sub.show()
