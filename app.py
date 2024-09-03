from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource
from bokeh.layouts import column

# Prepare the data
x = [1, 2, 3, 4, 5]
y1 = [6, 7, 2, 4, 5]
y2 = [2, 3, 4, 5, 6]
y3 = [4, 5, 5, 7, 2]

# Create a new plot
p = figure(title="Example of Multiple Layers Displayed", x_axis_label="x", y_axis_label="y")

# Add multiple layers of visualization
p.vbar(x=x, top=y2, legend_label="Bars", width=0.5, bottom=0, color="red")  # Vertical bars
p.line(x, y1, legend_label="Lines", color="blue", line_width=2)             # Line plot
p.circle(x, y3, legend_label="Circles", size=12, fill_color="red", fill_alpha=0.5, line_color="blue")  # Circle plot

# Add the plot to the current document
curdoc().add_root(p)
