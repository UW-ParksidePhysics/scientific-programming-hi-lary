import matplotlib as plt


def annotate_plot(annotations):
    # plt.text(x, y, s, fontdict=None, **kwargs)
    # x,y=floats, s=string, fontdict=None or dict, kwargs= other properties
    plt.text(annotations['positions'][0], annotations['positions'][1], annotations['string'], )