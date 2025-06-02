import sys
from PIL import Image
from IT8951.display import AutoEPDDisplay
from omni_epd import displayfactory, EPDNotFoundError

DISPLAY_TYPE = "waveshare_epd.it8951"
VCOM = -2.27  # Specific VCOM value for your hardware

print('Loading display')
try:
    # Optionally use AutoEPDDisplay if not using displayfactory
    # display = AutoEPDDisplay(vcom=VCOM)
    # epd = display.epd

    epd = displayfactory.load_display_driver(DISPLAY_TYPE)
except EPDNotFoundError as e:
    print(e)
    print(f"Couldn't find {DISPLAY_TYPE}")
    sys.exit(1)
except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)

try:
    print('Loading image')
    image = Image.open('PIA03519_small.jpg')

    # Resize image to fit the display
    image = image.resize((epd.width, epd.height))

    print('Writing to display')
    print("Rotating image 180 degrees, adjusting sharpness and contrast")
    image = image.rotate(180)

    epd.prepare()
    epd.display(image)
    epd.close()

except Exception as e:
    print(f"Error processing image or displaying: {e}")
    sys.exit(1)
