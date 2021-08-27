# libs
import matplotlib.pyplot

# custom libs
from . import adjustText

# reusable bar graph plotter
def bar_graph(xs, ys, plot_labels, size=(8, 6), bar_labels=False):
    # set plot size
    matplotlib.pyplot.figure(figsize=size)

    # bars are by default width 0.8, so we'll add 0.1 to the left coordinates # so that each bar is centered
    x_bars = [i + 0.5 for i, _ in enumerate(xs)]

    # plot bars
    matplotlib.pyplot.bar(x_bars, ys, color='#ff4433')
    
    # get labels
    xlabel, ylabel, plot_title = plot_labels.split(':')

    # label axes and graph title
    matplotlib.pyplot.ylabel('{}'.format(ylabel, fontsize=12))
    matplotlib.pyplot.xlabel('{}'.format(xlabel, fontsize=12))
    matplotlib.pyplot.title('{}'.format(plot_title))
    
    # label x-axis with current major
    if bar_labels:
        matplotlib.pyplot.xticks([i + 0.5 for i, _ in enumerate(xs)], xs, rotation=90)

    # finally generate graph
    return matplotlib.pyplot
    

# reusable bar graph plotter
def horizontal_bar_graph(xs, ys, plot_labels, size=(8, 6), fig_caption=None):
    # get x-axis
    xaxis = list(reversed(xs))

    # get y-axis
    yaxis = list(reversed(ys))
    
    # get y positions
    ypos = [y for y in range(len(yaxis))]

    # set plot size
    matplotlib.pyplot.figure(figsize=size, dpi=200.00, linewidth=4)
    
    # get labels
    xlabel, plot_title = plot_labels.split(':')

    # label axes and graph title
    matplotlib.pyplot.xlabel('{}'.format(xlabel, fontsize=50))
    matplotlib.pyplot.title('{}'.format(plot_title, fontsize=50))
    
    # plot bars
    matplotlib.pyplot.barh(ypos, xaxis, color='#ff4433', align='center', tick_label=yaxis)
    
    # check for figure caption
    if fig_caption:
        # add caption below figure
        matplotlib.pyplot.figtext(0.5, -0.1, fig_caption, wrap=True, horizontalalignment='center', fontsize=14)
    
    # generate graph
    return matplotlib.pyplot


# for time series data
def line_graph(xs, ys, plot_labels, size=(8, 6)):
    
    # get labels for plot (not points)
    xlabel, ylabel, plot_title = plot_labels.split(':')

    # set plot size
    matplotlib.pyplot.figure(figsize=size)

    # create a line chart, years on x-axis, gdp on y-axis
    matplotlib.pyplot.plot(xs, ys, color='green', marker=None, linestyle='solid') # add a title
  
    # label axes and graph title
    matplotlib.pyplot.ylabel('{}'.format(ylabel, fontsize=12))
    matplotlib.pyplot.xlabel('{}'.format(xlabel, fontsize=12))
    matplotlib.pyplot.title('{}'.format(plot_title))
    
    # return plot
    return matplotlib.pyplot   
    
    
def scatter_graph(xs, ys, point_names, plot_labels, size=(8, 6), fig_caption=None):
    # set plot size
    matplotlib.pyplot.figure(figsize=size, dpi=200.00, linewidth=4)

    # plot bars
    matplotlib.pyplot.scatter(xs, ys, color='#005580', alpha=0.8)
    
    # get labels
    ylabel, xlabel, plot_title = plot_labels.split(':')

    # label axes and graph title
    matplotlib.pyplot.ylabel('{}'.format(ylabel, fontsize=12))
    matplotlib.pyplot.xlabel('{}'.format(xlabel, fontsize=12))
    matplotlib.pyplot.title('{}'.format(plot_title))

    # add text labels
    text = [matplotlib.pyplot.text(x, y, label) for x, y, label in zip(xs, ys, point_names)]
    
    # get points repel
    xrepel, yrepel = len(xs) / 5, len(ys) / 5
    
    # create text points
    xtxt, ytxt = [xrepel + 1 for x in xs], [yrepel + 0.5 for y in ys]
    
    # adjust
    adjustText.adjust_text(text, 
                           arrowprops=dict(
                               arrowstyle="simple, head_width=0.25, tail_width=0.05", 
                               color='#ff4433', 
                               lw=0.5, 
                               alpha=0.5
                           ),
                           force_points=(3.2, 8.0)
                          )
    
     # check for figure caption
    if fig_caption:
        # add caption below figure
        matplotlib.pyplot.figtext(0.5, -0.1, fig_caption, wrap=True, horizontalalignment='center', fontsize=14)
        
    # finally generate graph
    return matplotlib.pyplot