'''
This plots all data files in a directory if the current working directory is where all the data is located. If the temperature field is not found
then the variable plotted is density.
'''

import yt
import os

def SaveSlicePlot(variable, ds, plot_dir, file_name):
    s = yt.SlicePlot(ds, 'z', variable)
    s.set_cmap(variable, 'inferno')
    s.annotate_title(variable)
    s.set_zlim(variable, zmax=5e-7, zmin=1e-10)
    s.save(f'{plot_dir}/{file_name}.png')

    return 

plot_dir = '../plots'
all_ds = yt.load(f'./*.athdf', hint='athena')
temperature_variable = ('gas', 'temperature')
i = 0

if temperature_variable in all_ds[0].derived_field_list:
    for ds in all_ds:
        SaveSlicePlot(variable=temperature_variable, ds=ds, plot_dir=plot_dir, file_name=i)
        i = i + 1

else:
    density_variable = ('gas', 'density')
    for ds in all_ds: 
        SaveSlicePlot(variable=density_variable, ds=ds, plot_dir=plot_dir, file_name=i)
        i = i + 1
        
        

