import numpy
import matplotlib.pyplot as plt

if __name__ == "__main__" :
    x = []
    y = []
    with open("recorder", 'r') as f:
        for line in f.readlines():
            splitted = line.split(':')
            print(splitted)
            x.append(int(splitted[0]))
            y.append(float(splitted[1][:-1]))
    plt.plot(x, y)
    plt.show()
