import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import AxesGrid
import yt

integrators = ['rk2', 'rk3', 'rk4', 'vl2', '5_4']
test_dir = "/data/khyaes/integrator_test/implode"

fig = plt.figure()

grid = AxesGrid(
    fig,
    (0.5, 0.07, 5, 3), # Change this to get the dimensions and sizing of the subplots right. It is the padding for (left, bottom, width, height)
    nrows_ncols=(1, 5),
    axes_pad= 1, # Padding between the subplots
    label_mode='L',
    share_all=True,
    cbar_location="right",
    cbar_mode="single",
    cbar_size="3%",
    cbar_pad="0%")

variable=('gas', 'temperature')

for i, integrator in enumerate(integrators):
    ds = yt.load(f'{test_dir}/{integrator}/data/Implode.out2.00500.athdf')
    s = yt.SlicePlot(ds=ds, normal='z', fields=variable)
    s.set_cmap(variable, 'inferno')
    if integrator == '5_4':
        s.annotate_title('RK54')
    else:
        s.annotate_title(integrator.upper())
    s.set_zlim(variable, zmax=1.4e-8, zmin=7e-9)
    s.set_log(variable, False)
    s.set_colorbar_label(variable, 'Temperature')
    s.set_font_size(100)
    s.set_colorbar_minorticks(variable, False)
    s.set_minorticks(variable, False)

    plot = s.plots[variable]
    plot.figure = fig
    plot.axes = grid[i].axes
    plot.cax = grid.cbar_axes[i]

    # Finally, this actually redraws the plot.
    s.render()

# 'bbox_inches='tight' here is very important for getting correct dimensions on subplots!!
#plt.savefig("/home/khayes/summer2024/paper/plots/implode_integrator_multiplot.png", bbox_inches='tight', dpi=100) 

