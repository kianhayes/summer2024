'''
This plots all data files in a directory if the current working directory is where all the data is located. Various plot properties can be changed with command-line arguments such as
the directory where the plots are placed, the bounds of the color bar, the title, and the plotted variable.
'''

import yt
import argparse
from slice_plot import SaveSlicePlot

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--data_directory", default='./', help="Directory of data file to plot", required=True)
parser.add_argument("-p", "--plot_directory", help="Specifies a directory to put plots")
parser.add_argument("-zmax", help="Max value of color bar", type=float)
parser.add_argument("-zmin", help="Min value of color bar", type=float)
parser.add_argument("-v", "--variable", default='temperature', help="Variable to plot, this fills the second item in the required tuple for this argument in yt, default being ('gas', 'temperature')")
parser.add_argument("-t", "--title", help="Plot title")
parser.add_argument("-norm", "--normal", default='z', help='Normal vector of the plot')

args = parser.parse_args()

if args.plot_directory == None:
    plot_dir = f'{args.data_directory}/../plots'
else:
    plot_dir = args.plot_directory
    
all_ds = yt.load(f'{args.data_directory}/*.athdf', hint='athena')
i = 0

if ('gas', args.variable) not in all_ds[0].derived_field_list:
    print(f"\n('gas', '{args.variable}') is not a variable in this data. Retry with one from this list")
    for field in all_ds[0].derived_field_list:
        if 'gas' in field:
            print(f'{field}')

else:
    for ds in all_ds:
        SaveSlicePlot(
            variable=('gas', args.variable), 
            ds=ds, 
            plot_dir=plot_dir, 
            norm=args.normal, 
            title=f'{args.title} at t={round(float(ds.current_time), 3)}', 
            zmin=args.zmin, 
            zmax=args.zmax, 
            file_name=f'{i}.png')

        i = i + 1   


