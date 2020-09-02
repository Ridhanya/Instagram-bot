from PIL import Image, ImageDraw, ImageFont
from random import randint
import pandas
import random
#create image object from the input image path
def text_wrap(text, font, max_width):
        """Wrap text base on specified width. 
        This is to enable text of width more than the image width to be display
        nicely.
        @params:
            text: str
                text to wrap
            font: obj
                font of the text
            max_width: int
                width to split the text with
        @return
            lines: list[str]
                list of sub-strings
        """
        lines = []
        
        # If the text width is smaller than the image width, then no need to split
        # just add it to the line list and return
        if font.getsize(text)[0]  <= max_width:
            lines.append(text)
        else:
            #split the line by spaces to get words
            words = text.split(' ')
            i = 0
            # append every word to a line while its width is shorter than the image width
            while i < len(words):
                line = ''
                while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
                    line = line + words[i]+ " "
                    i += 1
                if not line:
                    line = words[i]
                    i += 1
                lines.append(line)
        return lines





try:
	n=random.randint(1,7)
	image = Image.open("D:\\INSTA\\space_images\\space"+str(n)+".jfif")   
except IOError as e:
    print(e)

# Resize the image 
df=pandas.read_csv("D:\\INSTA\\scrap\\two.csv")
li=[]
for row in df["Headline"]:
	li.append(row)
width = 500
img_w = image.size[0]
img_h = image.size[1]
wpercent = (width/float(img_w))
hsize = int((float(img_h)*float(wpercent)))
rmg = image.resize((width,hsize), Image.ANTIALIAS)

# Set x boundry
# Take 10% to the left for min and 50% to the left for max
x_min = (rmg.size[0] * 8) // 100
x_max = (rmg.size[0] * 50) // 100
# Randomly select x-axis
ran_x = randint(x_min, x_max)
# Create font object with the font file and specify desired size
# Font style is `arial` and font size is 20
font_path = 'font/arialbd.ttf'
font = ImageFont.truetype(font=font_path, size=40)
text = str(li[0])
lines = text_wrap(text, font, rmg.size[0]-ran_x)
line_height = font.getsize('hg')[1]

y_min = (rmg.size[1] * 4) // 100   # 4% from the top
y_max = (rmg.size[1] * 90) //100   # 90% to the bottom
y_max -= (len(lines)*line_height)  # Adjust
ran_y = randint(y_min, y_max)      # Generate random point

#Create draw object
draw = ImageDraw.Draw(rmg)
#Draw text on image
color = 'rgb(110,150,240)'  # Red color
x = ran_x
y = ran_y
for line in lines:
    draw.text((x,y), line, fill=color, font=font)
    
    y = y + line_height    # update y-axis for new line
# Redefine x and y-axis to insert author's name

y += 5                       # Add some line space
x += 20   

rmg=rmg.resize((1080,1080))                   # Indent it a bit to the right

rmg.save("output.jpg")



