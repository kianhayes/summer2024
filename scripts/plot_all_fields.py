'''
Plots all fields in a data file if the current working directory is where all the data is located.
'''

import yt
import os

def SaveSlicePlot(variable, ds, plot_dir, file_name):
    s = yt.SlicePlot(ds, 'z', variable)
    s.set_cmap(variable, 'inferno')
    s.annotate_title(variable)
    s.save(f'{plot_dir}/{file_name}')

    return 

data_file = input('Paste data file path: ')
data_dir = os.path.dirname(data_file)
plot_dir = f'{data_dir}/../all_fields_plots'

print(data_file)
print(data_dir)
print(plot_dir)

if os.path.exists(plot_dir): 
    plot_list = os.listdir(plot_dir)
    if len(plot_list) != 0:
        for file in plot_list:
            os.remove(f'{plot_dir}/{file}')
        os.rmdir(plot_dir)
    
    else:
        os.rmdir(plot_dir)
    
os.mkdir(plot_dir)

ds = yt.load(data_file, hint='athena')

for field in ds.derived_field_list:
    if 'gas' in field:
        SaveSlicePlot(variable=field, ds=ds, plot_dir=plot_dir, file_name=f'{field[1]}_plot.png')

    else:
        continue

