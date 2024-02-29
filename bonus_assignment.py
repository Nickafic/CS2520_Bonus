# Authors: Benjamin Nguyen, Nick Nguyen
# Assignment:  Bonus Assignment
# Completed (or last revision): 02/29/2024

# Design Idea Statement
"""
We were inspired by ...

Team members: Benjamin Nguyen, Nick Nguyen
Benjamin Nguyen contribution: coded the source code
Nick Nguyen contribution: coded the source code
"""
# Source Code

from PIL import Image

BeachImage = Image.open('test.jpeg')
BoatImage = Image.open('boat.jpeg')
copy_image = BeachImage.copy()
position = ((copy_image.width - BoatImage.width), (copy_image.height - BoatImage.height))
copy_image.paste(BoatImage, position)
copy_image.save('pasted_image.jpeg')
copy_image.show()