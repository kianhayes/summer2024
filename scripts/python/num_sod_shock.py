import yt
import pandas as pd
import numpy as np

Nx = 100
X = 1
dx = X/(Nx-1)
xs = np.linspace(0,X,Nx)
x0 = Nx//2
dt = 0.01
tmax = 0.5
ts = np.linspace(0, tmax, int(tmax/dt))

# Riemann Solvers
labels = ['HLLE', 'HLLC', 'LHLLC', 'LLF', 'Roe']
field = ('gas', 'density')
i = 0


for i in range(len(ts)):
    num_data_df = pd.DataFrame({'x': xs}, index=xs)

    for solver in labels:
        ds = yt.load(f'/data/khyaes/solvers_test/sod_shock/{solver.lower()}/data/Sod.out1.{str(i).zfill(5)}.athdf')
        yt_dens_array = ds.r['gas', 'density'].v
        yt_vel_array = ds.r['gas', 'velocity_x'].v
        yt_pres_array = ds.r['gas', 'pressure'].v

        num_data_df[f'{solver.lower()}_density'] = yt_dens_array
        num_data_df[f'{solver.lower()}_velocity'] = yt_vel_array
        num_data_df[f'{solver.lower()}_pressure'] = yt_pres_array

    num_data_df.to_csv(f'/data/khyaes/solvers_test/sod_shock/num_data/num_sod_{i}.txt')