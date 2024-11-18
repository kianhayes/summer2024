import numpy as np
import yt
import os
import pandas as pd
from matplotlib import pyplot as plt
plt.style.use("/home/khayes/summer2024/scripts/python/paper_figures/paper.mplstyle")

"""
1. Get the directory list of every solver and remove unwanted file paths
2. Put every value for primitive variables in an array
3. Do the error calculation for every solver I want to compare to HLLC solver.
4. Append that error to text file
"""

solvers = [('llf', 'blue'), ('hlle', 'red'), ('lhllc', 'yellow'), ('roe', 'green'), ('hllc', 'purple')]
fields = ['density', 'velocity', 'pressure']

def calculate_error(ref_data, num_data):
    '''
    Outputs the error between reference data and numerical data by summing the error between each grid cell in the simulation and normalizing it to N cells
    '''  

    error = 0
    for i in range(len(num_data)):
        dif = abs(num_data[i] - ref_data[i])
        error += dif

    error = (1/len(num_data))*error
    
    return error

def column_to_list(column):
    list = []

    for value in column:
        list.append(value)
    
    return list

Nx = 100
X = 1
dx = X/(Nx-1)
xs = np.linspace(0,X,Nx)
x0 = Nx//2
dt = 0.01
tmax = 0.5
ts = np.linspace(0, tmax, int(tmax/dt))
error_df = pd.DataFrame({'t': ts})
fig, axs = plt.subplots(1, 3, figsize=(16,9))

for solver in solvers:
    dens_error_array = []
    vel_error_array = []
    pres_error_array = []

    for i in range(len(ts)):
    
        analytic_data = pd.read_csv(f'/data/khyaes/solvers_test/sod_shock/analytic_data/analytic_sod_{i}.txt')
        num_data = pd.read_csv(f'/data/khyaes/solvers_test/sod_shock/num_data/num_sod_{i}.txt')

        dens_array = column_to_list(num_data[f'{solver[0].lower()}_density'])
        vel_array = column_to_list(num_data[f'{solver[0].lower()}_velocity'])
        pres_array = column_to_list(num_data[f'{solver[0].lower()}_pressure'])

        dens_error = calculate_error(column_to_list(analytic_data['Density']), dens_array) # A single float value
        vel_error = calculate_error(column_to_list(analytic_data['Velocity']), vel_array) # Single float
        pres_error = calculate_error(column_to_list(analytic_data['Pressure']), pres_array) # Single float

        dens_error_array.append(dens_error)
        vel_error_array.append(vel_error)
        pres_error_array.append(pres_error)

    axs[0].plot(ts, dens_error_array,'o', label=solver[0].upper(), color=solver[1])
    axs[1].plot(ts, vel_error_array, 'o', label=solver[0].upper(), color=solver[1])
    axs[2].plot(ts, pres_error_array, 'o', label=solver[0].upper(), color=solver[1])

for i in range(3):
    if i == 1:
        axs[i].set_xlim([0.,0.2])
        axs[i].set_ylim([0,0.03])
    else:
        axs[i].set_xlim([0.,0.2])
        axs[i].set_ylim([0,0.01])

axs[0].set_title('Density Error', size=12)
axs[1].set_title('Velocity Error', size=12)
axs[2].set_title('Pressure Error', size=12)
axs[2].legend(loc='center left', bbox_to_anchor=(1, 0.5))
fig.tight_layout()
plt.savefig(f'/home/khayes/summer2024/paper/sod_error_plot.png', dpi=300)
