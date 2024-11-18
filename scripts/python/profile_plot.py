'''
Main function for making a slice plot present in other scripts that have more specific utility
'''

import yt

def SaveProfilePlot(variable, ds, plot_dir, norm, title, file_name, zmin='min', zmax='max'):
    s = yt.ProfilePlot(ds, norm, variable)
    #s.set_cmap(variable, 'inferno')
    s.annotate_title(title)
    #s.set_xlim(variable, xmin=zmin, xmax=zmax)
    s.save(f'{plot_dir}/{file_name}')

    return 
