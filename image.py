import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageOps
import json

def newtweett(msg):
  
    bg = 'white'
    text = 'black'

    # Load the profile picture and resize it to 50 x 50 pixels
    pp = Image.open("image.png")
    pp = pp.resize((50, 50))

    # Crop the image into a circle using ImageOps.fit()
    mask = Image.new("L", pp.size, 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0) + pp.size, fill=255)
    pp = ImageOps.fit(pp, mask.size, centering=(0.5, 0.5))
    pp.putalpha(mask)

    # Load the fonts for the tweet text and username
    text_font = ImageFont.truetype("NotoSans-Medium.ttf", 22)
    user_font = ImageFont.truetype("NotoSans-Medium.ttf", 18)
    tweet_font = ImageFont.truetype("NotoSans-Medium.ttf", 22)

    # Define the maximum width of a line in pixels
    max_width = 40

    # Wrap the tweet text into multiple lines
    # Split the user's input text into lines
    user_lines = msg.splitlines()

    # Create an empty list to store wrapped text for each line
    wrapped_lines = []

    # Wrap each line of text and store in the wrapped_lines list
    for line in user_lines:
        if line.strip() == '':
            # If the line is empty, add it as it is
            wrapped_lines.append('')
        else:
            wrapped_lines.extend(textwrap.wrap(line, width=max_width, break_long_words=True))

    # Calculate the height of the tweet text in pixels
    tweet_height = len(wrapped_lines) * 35

    # Create a new image with the size of 550 x (200 + tweet_height) pixels and fill it with the background color
    img = Image.new("RGB", (550,  200 + tweet_height), bg)

    # Create a drawing object to draw on the image
    draw = ImageDraw.Draw(img)

    # Draw the name and username on the top left corner of the image
    draw.text((100, 50),
              'Sourav Mishra',
              font=text_font,
              fill=text)

    draw.text((100, 80),
              '@souravvmishra_',
              font=user_font,
              fill='gray')

    # Paste the profile picture on the top left corner of the image
    img.paste(pp, (40, 55), pp)  # Use the alpha channel of pp as a mask

    # Draw each line of text on the image
    y = 120  # The initial y coordinate
    for line in wrapped_lines:
        draw.text((40, y), line, font=tweet_font, fill=text)
        y += 35  # Increase the y coordinate by 30 pixels for each line

    # Save the image as a png file
    img.save("fake_tweet_with_image.png")

    img = Image.open('fake_tweet_with_image.png')
    w, h = img.size
    sqr = Image.new("RGB", (max(w + 100, h + 100), max(w + 100, h + 100)), bg)
    draw = ImageDraw.Draw(img)

    # Calculate the coordinates of the upper left corner of the pasted image
    x = (sqr.width - img.width) // 2  # Center the image horizontally
    y = (sqr.height - img.height) // 2  # Center the image vertically
    box = (x, y)

    # Paste the saved image on the center of the new layer
    sqr.paste(img, box)

    # Save the image as a png file
    sqr.save("tweet.png")
