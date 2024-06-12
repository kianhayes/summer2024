import yt
import os
import time

def SaveSlicePlot(variable, ds, plot_dir, file_name):
    s = yt.SlicePlot(ds, 'z', variable)
    s.set_cmap(variable, 'inferno')
    s.annotate_title(variable[1])
    s.set_zlim(variable, zmin=0, zmax=5e-9)
    s.save(f'{plot_dir}/{file_name}.png')

    return 

data_dir = input('Copy directory containing the data: ')
plot_dir = f'{data_dir}/../plots'
os.chdir(data_dir)
ds = yt.load(f'{data_dir}/*.athdf', hint='athena')
temperature_variable = ('gas', 'temperature')
i = 0

if temperature_variable in ds[0].derived_field_list:
    SaveSlicePlot(variable=temperature_variable, ds=ds[-1], plot_dir=plot_dir, file_name=i)

else:
    print(ds[0].derived_field_list)
    desired_field = input('Temperature variable not in this data. Copy desired field from Derived Field List: ')
    SaveSlicePlot(variable=desired_field, ds=ds[len(ds)/2], plot_dir=plot_dir, file_name=i)
        
        

