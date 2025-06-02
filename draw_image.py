"""
Copyright 2021 Rob Weber

This file is part of omni-epd

omni-epd is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
import sys
from PIL import Image
from IT8951.display import AutoEPDDisplay
from omni_epd import displayfactory, EPDNotFoundError


DISPLAY_TYPE = "waveshare_epd.it8951"
VCOM = -2.27  # Specific VCOM value for your hardware

# load your particular display using the displayfactory, driver specified in INI file
print('Loading display')
try:
    # display = AutoEPDDisplay(vcom=-2.27)
    # epd = display.epd
    try:
    epd = displayfactory.load_display_driver(DISPLAY_TYPE)
except EPDNotFoundError:
    print(e)
    print(f"Couldn't find {DISPLAY_TYPE}")
    sys.exit()

except Exception as e:
# if now load an image file using the Pillow lib
print('Loading image')
image = Image.open('PIA03519_small.jpg')

# resize for your display
image = image.resize((epd.width, epd.height))

# prepare the epd, write the image, and close
print('Writing to display')
print("Rotating image 180 degrees, adjusting sharpness and contrast")
epd.prepare()

epd.display(image)

epd.close()
