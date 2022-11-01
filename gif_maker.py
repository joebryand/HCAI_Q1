import imageio
images = []

filenames = range(20,1001,20)

filenames = [str(s) for s in filenames]
filenames = [s + '.png' for s in filenames]

for filename in filenames:
    images.append(imageio.imread(filename))
#imageio.mimsave('Plots/animated_gif_2.gif', images, fps=2)