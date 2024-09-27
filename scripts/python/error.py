import numpy as np
import yt
import os
import pandas as pd

"""
1. Get the directory list of every solver and remove unwanted file paths
2. Put every value for primitive variables in an array
3. Do the error calculation for every solver I want to compare to HLLC solver.
4. Append that error to text file
"""

ref_solver = 'hllc'
num_solvers = ['llf', 'hlle', 'lhllc', 'roe']

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

def remove_xdmf(directory_list):
    '''
    Removes the .xdmf files from a directory list in order to loop through the proper data files in a time series
    '''

    for file in directory_list:
        if '.xdmf' in file:
            directory_list.remove(file)

    return directory_list

ref_data_dir = '/data/khyaes/solvers_test/rt/hllc/data'
ref_dir_list = remove_xdmf(os.listdir('/data/khyaes/solvers_test/rt/hllc/data'))
ts = []
all_ref_data = []
all_data = pd.DataFrame()
time_limit = 0.1

# Loop through reference solver directory, get the simulation time and puts the data for density into an array that contains
# all the data at each time step for the reference solver.
for hdf5_file in ref_dir_list:
    current_ref_data = []
    ref_ds = yt.load(f'/data/khyaes/solvers_test/rt/{ref_solver}/data/{hdf5_file}')
    t = round(float(ref_ds.current_time), 3)
    ts.append(t)

    ref_density_data = ref_ds.r['gas', 'density'].v
    all_ref_data.append(ref_density_data)

    

print(f'All Ref Data: {all_ref_data}')
all_data.insert(loc=0, column='time', value=ts)

# Now that we have an array of an array for each time step in the reference data, need an array of arrays for each time step for numerical solver
# Loops through every numerical solver directory
for i, num_solver in enumerate(num_solvers):
    num_data_dir = f'/data/khyaes/solvers_test/rt/{num_solver}/data'
    num_dir_list = remove_xdmf(os.listdir('/data/khyaes/solvers_test/rt/hllc/data'))
    error_data = []
    all_num_data = []

    # Loop through every file in the current numerical solver data directory and gets the data at that time step and puts it into 'all_num_data' array, 
    # At the end of this loop the array of arrays for each time step will be created
    for hdf5_file in num_dir_list:
        num_ds = yt.load(f'{num_data_dir}/{hdf5_file}')

        num_density_data = num_ds.r['gas', 'density'].v
        all_num_data.append(num_density_data)

    print(f'All Num Data for {num_solver}: {all_num_data}')
    # Now that we have the array of arrays, want to do the error calculation all_num - all_ref
    for j, num_data in enumerate(all_num_data):
        error_value = calculate_error(all_ref_data[j], num_data)
        error_data.append(error_value)
    
    print(f'All error data for {num_solver}: {error_data}')
    print(f'Pandas DF: {all_data}')
    # Now that we have the errors at every time step compared against the current solver, want to insert the error data into the Pandas DataFrame
    all_data.insert(loc=i+1, column=num_solver, value=error_data)

error_data_file = open("/home/khayes/summer2024/athena/solvers_test/rt_solvers_error_data.txt", "a")
all_data.to_csv("/home/khayes/summer2024/athena/solvers_test/rt_solvers_error_data.txt", sep=',')