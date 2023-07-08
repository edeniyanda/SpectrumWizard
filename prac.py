import matplotlib.pyplot as plt
from colorthief import ColorThief


ct = ColorThief("test.jpg")
dominant_color = ct.get_color(quality=1)


plt.imshow([[dominant_color]])

plt.show()

dc = ct.get_palette(color_count=7)


# plt.imshow([[dc[i] for i in range(5)]])

# plt.show()


print(dc)
