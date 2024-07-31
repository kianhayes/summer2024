'''
Plots all fields in a data file if the current working directory is where all the data is located.
'''

import yt
import argparse
import os
from slice_plot import SaveSlicePlot

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--data_directory", default='./', help="Directory of data file to plot", required=True)
parser.add_argument("-p", "--plot_directory", help="Specifies a directory to put plots", required=True)
parser.add_argument("-norm", "--normal", default='z', help='Normal vector of the plot')

args = parser.parse_args()

data_file = args.data_directory
data_dir = os.path.dirname(data_file)
plot_dir = args.plot_directory

ds = yt.load(data_file, hint='athena')

for field in ds.derived_field_list:
    print(field)

for field in ds.derived_field_list:
    if 'gas' in field:
        SaveSlicePlot(variable=field, ds=ds, norm=args.normal, plot_dir=plot_dir, title=field[1], file_name=f'{field[1]}_{args.normal}.png')

    else:
        continue


