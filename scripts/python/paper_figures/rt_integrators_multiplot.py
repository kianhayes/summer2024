import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import AxesGrid
import yt

integrators = ['rk2', 'rk3', 'rk4', 'vl2', '5_4']
test_dir = "/data/khyaes/integrator_test/rt"

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

for i, integrator in enumerate(integrators):
    ds = yt.load(f'{test_dir}/{integrator}/data/rt.out2.00208.athdf')
    s = yt.SlicePlot(ds=ds, normal='z', fields=variable)
    s.set_cmap(variable, 'inferno')
    if integrator == '5_4':
        s.annotate_title('SSPRK5_4')
    else:
        s.annotate_title(integrator.upper())
        
    s.set_zlim(variable, zmax=5.3e-9, zmin=2e-9)
    s.set_log(variable, False)
    s.set_colorbar_label(variable, 'Temperature')
    s.set_minorticks(variable, False)
    s.set_colorbar_minorticks(variable, True)
    s.set_font_size(58)

    plot = s.plots[variable]
    plot.figure = fig
    plot.axes = grid[i].axes
    plot.cax = grid.cbar_axes[i]

    # Finally, this actually redraws the plot.
    s.render()

# 'bbox_inches='tight' here is very important for getting correct dimensions on subplots!!
plt.savefig("/data/khyaes/integrator_test/rt/rt_integrator_multiplot.png", bbox_inches='tight', dpi=100) 

