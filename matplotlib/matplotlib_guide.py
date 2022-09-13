import matplotlib.pyplot as plt
import numpy as np
###############################################
print(80*'-')
print('Starting Basic Plotting')
print(80*'-')
###############################################
a = np.linspace(0,10,11)
b = a**4
x = np.arange(0,10)
y = 2*x

# Basic function to plot is plt.plot() - just basic x against y here
plt.plot(x,y)

# Add a title
plt.title("Eoin's Plot")
# x and y axes named
plt.xlabel("X AXIS")
plt.ylabel("Y AXIS")
# limit what the x and y axis show. Graphs can still go beyond this but might com in useful
plt.xlim(0,6)
plt.ylim(0,15)
# In a python script we need to use plt.show for plots similar to how print works
# ie just something to have it shown to us
# Must do axes, titles etc before calling this
plt.show()
# We can save the image created down as a png or jpeg or whatever type we want
plt.savefig("myplot.png")

# This is a jupyter specific command that makes sure plots appear in output panes
#%matplotlib inline

###############################################
print(80*'-')
print('Starting Figure Object')
print(80*'-')
###############################################
# using the figure object is the object oriented programming approach
# Use plt.figure to create a blank figure object, ie a completely blank canvas
# we will call the methods and attributes of the figure object to build the plot we want
#fig = plt.figure()
#fig = plt.figure(figsize=(10,10)) # get figsize in inches, gives us a 720x720 plot

# Add the axes we're gonna plot on. Can add as many axes as we want using the add_axes method call
#axes = fig.add_axes([0,0,1,1])

# Need to bear in mind that figure =! plot.
# ie our figure and our plot that goes on it are different things. The figure is the blank canvas
# and the plot is placed inside of that
# Can think of figure as easel and plot as the painting that goes on it,might not necessarily fill it all
# so add_axes is saying where on the figure our plot should be located
# add_axes([0,0,1,1])-> bottom left point of plot goes on (0,0) of figure, and (1,1) means use all of the
# remaining space on x and y axis. (so push diagram right out to fill up to right hand side upper corner)
#add_axes([0.5,0.5,1,1])
# -----------------* (1,1)
# |                |
# |        *       |
# |    (0.5,0.5)   |
# ------------------
# best to think these as ratios, ie (0,0)(1,1) means we're using 100% of the figure canvas

# Using this we can also embed multiple plots on one figure. So could have a big plot filling the
# whole figure, and a subplot with axes as (0.5,0.5,1,1) which is also there.
# the two figure will of course be overlaid, but it's POSSIBLE - so becomes the basis for subplots
# plt.subplots handles that for us


###############################################
print(80*'-')
print('Starting Figure Object and axes with data')
print(80*'-')
###############################################


fig = plt.figure()
# Add the big axes that fills whole canvas
axes_big = fig.add_axes([0,0,1,1]) # so exact same size as canvas
axes_big.plot(a,b)

# instead of directly setting labels, use the axis.set_abc() methods instead
axes_big.set_xlim(0,8)
axes_big.set_ylim(0,8000)
axes_big.set_xlabel('A')
axes_big.set_ylabel('B')
axes_big.set_title('Power of 4')


# Smaller axes that is within canvas but not filling it
axes_small = fig.add_axes([0.25,0.25,0.5,0.5]) # 0.5 ratio means we use 50% of x and y axis available
                                            # after starting at (0.25,0.25)
axes_small.plot(a,b)

# With this overlay method, we could for example, create a zoomed in section of a chart
axes_small.set_xlim(1,2)
axes_small.set_ylim(0,50)
axes_small.set_xlabel('A')
axes_small.set_ylabel('B')
axes_small.set_title('Zoomed in Power of 4')

print(type(fig))
print(type(axes_big))
plt.show()

# we can edit some attributes of the figure we've generated
# dpi is dots per inch, basically is the quality of the graph drawn. more dots is more visible line
# but go crazy and it starts taking up a lot of RAM
# figsize is just the size of canvas in inches, can make it huge if want
fig_new = plt.figure(dpi=200, figsize=(2,2)) #(1,8) makes a really tall skinny canvas,if ever wanted that
axes_new = fig_new.add_axes([0,0,1,1])

axes_new.plot(a,b)

# Save the thing as normal, add the bbox_inches because sometimes the axes don't print correctly when
# saving down
fig_new.savefig("new_figure.png",bbox_inches= "tight")


###############################################
print(80*'-')
print('Starting Subplots')
print(80*'-')
###############################################

# plt.subplots returns a tuple (figure,axes)
# a figure object, ie our canvas
# a nparray holding axes objects. The axes have been carved up into nice shapes for us, so we don't
    # have to place them on the figure ourselves
sub_fig, sub_axes = plt.subplots(nrows=2, ncols=2)

# The axes values is what we use to designate our plots.
# ie get a canvas and n subplots, call each axes object with a plot to have it drawn onto canvas
print(type(sub_axes)) # np array
print(sub_axes.shape) # has 2 cos of our ncols
print(sub_axes) # nparray holding the axes type objects
print(sub_axes[0]) # can access the individual axes objects from the array and use them to plot subplots
                    # if we want to do it that way its just another axes object like the ones above,
                    # but theres a list of them generated now. They plot onto the figure canvas
sub_axes[0][0].plot(x,y) # plot in top left slot of subplot figure
sub_axes[1][0].plot(a,b) # plot in bottom left of subplot figure

# Useful way to make the plot neat, makes printout try to not overlap or axes labesl block each other
#plt.tight_layout

# Another way to manually adjust the spacing between plots on the figure
# the value is the multiple of the axis, ie 0.9 times x axis used as spacing for wspace
sub_fig.subplots_adjust(wspace=0.9, hspace=0.2)

# changing attributes works the same way
sub_axes[0][0].set_xlabel("X LABEL AGAIN")
sub_axes[0][1].set_ylabel("X LABEL AGAIN")

# Can set a supertitle on the figure level as well
sub_fig.suptitle("SUPER TITLE")

# Save it down
sub_fig.savefig("my_new_subplot.png", bbox_inches="tight")
plt.show() # makes these show


###############################################
print(80*'-')
print('Starting Styling & legends')
print(80*'-')
###############################################

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

x = np.linspace(0,10,11)

# plot two lines on the same plot, just use same ax twice
# associate a label with each plot that will be utilised when making a legend
ax.plot(x,x, label="X vs X")
ax.plot(x, x**2, label= "X vs X^2")

# invoke the legend just by calling the legend method
ax.legend()
#ax.legend(loc="center left") # could tell specifically where we want the legend
#ax.legend(loc=(1.1,0.5)) give a point corresponding to add_axes arg ([1.1,0.5,m,n])

plt.show()

# Lastly we can amend the styling of our plots
last_fig = plt.figure()
last_ax = last_fig.add_axes([0,0,1,1])

# We can add a variety of args on plotting function to jazz it up
last_ax.plot(x,x,
         color='cyan',
         label="X vs X",
         lw=1.2, # line width, it's a ratio so 1.2 = x1.2 the regular thickness
         #linewidth same as lw
         ls="--", # linestyle, can make the line be a dashed line or use dots etc
         #linestyle=".-" same as ls
         marker="o", # if want to see individual points as dots on plot, as well as line eg if wanted
                    # a dashed line and dots on individual points, could do marker="o" and change
                    # ls="--". type of marker is on documentation
         ms=5, # marker size, how big the marker is, also works as markersize
         markerfacecolor="purple", # settings for the markers themselves, change the colors and effects
         markeredgewidth=8,
         markeredgecolor="red"
         )

plt.show()
































