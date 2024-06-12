import yt
import os
import time

def SaveSlicePlot(variable, ds, plot_dir, file_name):
    s = yt.SlicePlot(ds, 'z', variable)
    s.set_cmap(variable, 'inferno')
    s.annotate_title(variable)
    s.set_zlim(variable, zmax=5e-7, zmin=1e-10)
    s.save(f'{plot_dir}/{file_name}.png')

    return 

data_dir = input('Copy directory containing the data: ')
plot_dir = f'{data_dir}/../plots'
os.chdir(data_dir)
all_ds = yt.load(f'{data_dir}/*.athdf', hint='athena')
temperature_variable = ('gas', 'temperature')
i = 0

if temperature_variable in all_ds[0].derived_field_list:
    for ds in all_ds:
        SaveSlicePlot(variable=temperature_variable, ds=ds, plot_dir=plot_dir, file_name=i)
        i = i + 1

else:
    print(all_ds[0].derived_field_list)
    desired_field = input('Temperature variable not in this data. Copy desired field from Derived Field List: ')
    for ds in all_ds: 
        SaveSlicePlot(variable=desired_field, ds=ds, plot_dir=plot_dir, file_name=i)
        i = i + 1
        
        

