import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import AxesGrid
import yt

solvers = ['hlld', 'lhlld', 'hlle', 'llf', 'roe']
test_dir = "/data/khyaes/solvers_test/kh_shear"

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

variable=('gas', 'plasma_beta')

for i, solver in enumerate(solvers):
    ds = yt.load(f'{test_dir}/{solver}/data/kh-shear-lecoanet.out2.00200.athdf')
    s = yt.SlicePlot(ds=ds, normal='z', fields=variable)
    s.set_cmap(variable, 'magma')
    s.annotate_title(solver.upper())
    s.set_zlim(variable, zmax=1e11, zmin=1e5)
    s.set_colorbar_label(variable, 'Plasma Beta')
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
plt.savefig("/data/khyaes/solvers_test/kh_shear/kh_solvers_multiplot.png", bbox_inches='tight', dpi=100) 

