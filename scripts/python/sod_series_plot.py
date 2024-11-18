import numpy as np
from scipy.optimize import newton
import matplotlib.pyplot as plt
import yt
import pandas as pd

Nx = 100
X = 1
dx = X/(Nx-1)
xs = np.linspace(0,X,Nx)
x0 = Nx//2
dt = 0.01
tmax = 0.5
ts = np.linspace(0, tmax, int(tmax/dt))
lw = 0.75
fields = ['density', 'velocity', 'pressure']
labels = ['HLLE', 'HLLC', 'LHLLC', 'LLF', 'Roe']

for j, t in enumerate(ts):
    analytic = pd.read_csv(f'/data/khyaes/solvers_test/sod_shock/analytic_data/analytic_sod_{j}.txt')
    num_data = pd.read_csv(f'/data/khyaes/solvers_test/sod_shock/num_data/num_sod_{j}.txt')

    fig, axs = plt.subplots(1,3,figsize=(8,2))
    axs[0].set_title("Density")
    axs[0].plot(xs, analytic['Density'], lw=lw)
    axs[1].set_title("Velocity")
    axs[1].plot(xs, analytic['Velocity'], lw=lw)
    axs[1].set_yticks([0.,.2,.4,.6,.8,1.],['','','','','',''])
    axs[2].set_title("Pressure")
    axs[2].plot(xs, analytic['Pressure'], lw=lw)
    axs[2].set_yticks([0.,.2,.4,.6,.8,1.],['','','','','',''])
    fig.suptitle(f'Sod Shock at t={round(t, 3)}')

    for i in range(3):
        axs[i].set_xlim([0.,1.])
        axs[i].set_ylim([-.05,1.05])

    # Riemann Solvers
    for solver in labels:
        dens_array = num_data[f'{solver.lower()}_density']
        vel_array = num_data[f'{solver.lower()}_velocity']
        pres_array = num_data[f'{solver.lower()}_pressure']

        axs[0].plot(xs, dens_array, lw=lw)
        axs[1].plot(xs, vel_array, lw=lw)
        axs[2].plot(xs, pres_array, lw=lw)

    fig.tight_layout()
    plt.savefig(f'/data/khyaes/solvers_test/sod_shock/plots/sod{j}.png', dpi=300)