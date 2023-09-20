import os
from skimage import io, exposure


def colorizing(input_path, output_path):
        image = io.imread(input_path)

        gamma = 1.3 
        adjusted_image = exposure.adjust_gamma(image, gamma=gamma)

        io.imsave(output_path, adjusted_image)
