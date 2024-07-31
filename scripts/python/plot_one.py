import yt
import os
import argparse
from slice_plot import SaveSlicePlot

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--data_directory", help="Directory of data file to plot", required=True)
parser.add_argument("-p", "--plot_directory", help="Directory of plot", required=True)
parser.add_argument("-zmax", help="Max value of color bar", type=float)
parser.add_argument("-zmin", help="Min value of color bar", type=float)
parser.add_argument("-v", "--variable", default='temperature', help="Variable to plot, this fills the second item in the required tuple for this argument in yt, default being ('gas', 'temperature')")
parser.add_argument("-t", "--title", help="Plot title")
parser.add_argument("-norm", "--normal", default='z', help='Normal vector of the plot')

args = parser.parse_args()

ds = yt.load(args.data_directory, hint='athena')

if args.title == None:
    plot_title = f'{args.variable.upper()} at t={round(float(ds.current_time), 3)}'
else:
    plot_title = args.title

if ('gas', args.variable) in ds.derived_field_list:
    SaveSlicePlot(variable=('gas', args.variable), ds=ds, plot_dir=args.plot_directory, norm=args.normal, title=plot_title, zmin=args.zmin, zmax=args.zmax, file_name=f'{args.variable}_plot.png')

else:
    print('The chosen variable is not in the field list')
    for field in ds.derived_field_list:
        if 'gas' in field:
            print(field[1])