#imports ImageIO in version 3, writen short with iio
import imageio.v3 as iio
Filename = ["goku.jpg", "sev.png"]
images = []
for filename in Filename:
    images.append(iio.imread(filename))

iio.imwrite('Test.gif', images, duration = 1000, loop = 2)


