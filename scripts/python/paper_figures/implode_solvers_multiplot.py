import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import AxesGrid
import yt

solvers = ['hllc', 'lhllc', 'hlle', 'llf', 'roe']
test_dir = "/data/khyaes/solvers_test/lw_collapse"

fig = plt.figure()

grid = AxesGrid(
    fig,
    (0.05, 0.07, 6, 2), # Change this to get the dimensions and sizing of the subplots right. It is the padding for (left, bottom, width, height)
    nrows_ncols=(1, 5),
    axes_pad= 2, # Padding between the subplots
    label_mode='L',
    share_all=True,
    cbar_location="right",
    cbar_mode="single",
    cbar_size="3%",
    cbar_pad="0%")

variable=('gas', 'temperature')

for i, solver in enumerate(solvers):
    ds = yt.load(f'{test_dir}/{solver}/data/Implode.out2.00500.athdf')
    s = yt.SlicePlot(ds=ds, normal='z', fields=variable)
    s.set_cmap(variable, 'inferno')
    s.annotate_title(solver.upper())
    s.set_width(0.3)
    s.set_zlim(variable, zmax=1.4e-8, zmin=7e-9)
    s.set_colorbar_label(variable, 'Temperature (code)')
    s.set_font_size(58)
    s.set_colorbar_minorticks(variable, False)
    s.set_minorticks(variable, False)

    plot = s.plots[variable]
    plot.figure = fig
    plot.axes = grid[i].axes
    plot.cax = grid.cbar_axes[i]

    # Finally, this actually redraws the plot.
    s.render()

# 'bbox_inches='tight' here is very important for getting correct dimensions on subplots!!
plt.savefig("/data/khyaes/solvers_test/lw_collapse/implosion_solvers_multiplot.png", bbox_inches='tight', dpi=100) 

