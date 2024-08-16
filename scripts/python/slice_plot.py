'''
Main function for making a slice plot present in other scripts that have more specific utility
'''

import yt

def SaveSlicePlot(variable, ds, plot_dir, norm, title, file_name, zmin='min', zmax='max'):
    s = yt.SlicePlot(ds, norm, variable)
    s.set_cmap(variable, 'inferno')
    s.annotate_title(title)
    s.set_zlim(variable, zmin=zmin, zmax=zmax)
    s.save(f'{plot_dir}/{file_name}')

    return 
