import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#plt.style.use('/home/khayes/summer2024/scripts/python/paper_figures/paper.mplstyle')

data = pd.read_csv('/home/khayes/summer2024/athena/solvers_test/rt_solvers_error_data.txt', sep=',')
ts = []
errors = []
num_solvers = ['llf', 'hlle', 'lhllc', 'roe']

for num_solver in num_solvers:
    plt.plot(data['time'], data[num_solver])
    
plt.legend(['LLF', 'HLLE', 'LHLLC', 'Roe'])
plt.xlabel('Simulation Time (sec)')
plt.ylabel('Error sigma_num')

plt.savefig('/home/khayes/summer2024/athena/solvers_test/solvers_error_plot.png', dpi=300)