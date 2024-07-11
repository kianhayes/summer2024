import yt
import os

def SaveSlicePlot(variable, ds, plot_dir, file_name):
    s = yt.SlicePlot(ds, 'z', variable)
    s.set_cmap(variable, 'inferno')
    s.annotate_title(variable[1])
    #s.set_zlim(variable, zmin=0, zmax=5e10)
    s.save(f'{plot_dir}/{file_name}.png')

    return 

data_dir = input('Copy directory containing the data: ')
plot_dir = f'{data_dir}/../plots'
os.chdir(data_dir)
ds = yt.load(f'{data_dir}/*.athdf', hint='athena')
temperature_variable = ('gas', 'temperature')
i = 0

if temperature_variable in ds[0].derived_field_list:
    SaveSlicePlot(variable=temperature_variable, ds=ds[-1], plot_dir=plot_dir, file_name='temp_plot')

else:
    density_variable = ('gas', 'density')
    SaveSlicePlot(variable=density_variable, ds=ds[10], plot_dir=plot_dir, file_name='density_plot')
        
        

