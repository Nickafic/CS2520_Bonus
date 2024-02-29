# Authors: Benjamin Nguyen, Nick Nguyen
# Assignment:  Bonus Assignment
# Completed (or last revision): 02/29/2024

# Design Idea Statement
"""
We like the ocean, so we decided to use that as our base of our artwork.
This our original design.
Team members: Benjamin Nguyen, Nick Nguyen
Benjamin Nguyen contribution: coded the whale image
Nick Nguyen contribution: coded the boat and balloon
"""
# Source Code

from PIL import Image

BeachImage = Image.open('test.jpeg')
BoatImage = Image.open('boat.jpeg')
whale_Image = Image.open('Humpback_whale.jpeg')
BalloonImage = Image.open('balloon.jpeg')
copy_image = BeachImage.copy()
position = (1000,1000)
position2 = ((copy_image.width - whale_Image.width - 1000), (copy_image.height - whale_Image.height))
copy_image.paste(whale_Image, position2)
copy_image.paste(BoatImage, position)
copy_image.paste(BalloonImage, (2000,200))
copy_image.save('pasted_image.jpeg')
copy_image.show()