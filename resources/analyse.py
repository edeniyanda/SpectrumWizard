import matplotlib.pyplot as plt
from colorthief import ColorThief



def plot_analyse(img_name, num_of_color:int):

    ct = ColorThief(img_name)
    dc = ct.get_palette(color_count = num_of_color)
    
    plt.imshow([[dc[i] for i in range(num_of_color-1)]])
    plt.show()
