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
print(f'\n{args}')
print(f'\nData Directory: {args.data_directory}' 
      f'\nPlot Directory: {args.plot_directory}' 
      f'\nMax color bar value {args.zmax}' 
      f'\nMin color bar value: {args.zmin}' 
      f'\nVariable to plot: {args.variable}' 
      f'\nPlot title: {args.title}'
      f'\nNormal vector of plot: {args.normal}')

ds = yt.load(args.data_directory, hint='athena')

if ('gas', args.variable) in ds.derived_field_list:
    SaveSlicePlot(variable=('gas', args.variable), ds=ds, plot_dir=args.plot_directory, norm=args.normal, title=args.title, zmin=args.zmin, zmax=args.zmax, file_name=f'{args.variable}_plot.png')
