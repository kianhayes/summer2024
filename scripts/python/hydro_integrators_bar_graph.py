import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('E:/School/reu2024/research/summer2024/athena/integrators_test/data.csv', header=None)
integrators = []
rt_times = []
implosion_times = []

for solver in data.iloc[1:, 0]:
    integrators.append(solver.upper())

for time in data.iloc[1:,1]:
    implosion_times.append(float(time))

for time in data.iloc[1:,2]:
    rt_times.append(float(time))

print(integrators)
print(rt_times)
print(implosion_times)

df1 = pd.DataFrame(
   dict(
      names=integrators,
      marks=rt_times
   )
)

df2 = pd.DataFrame(
   dict(
      names=integrators,
      marks=implosion_times
   )
)

df1_sorted = df1.sort_values('marks')
df2_sorted = df2.sort_values('marks')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

ax1.bar('names', 'marks', data=df1_sorted, color='#0D324D')
ax2.bar('names', 'marks', data=df2_sorted, color='#7F5A83')
ax1.set_title('Rayleigh-Taylor Instability', size=20)
ax2.set_title('Implosion', size=20)
ax1.set_xlabel('Solver', fontsize=15)
ax1.set_ylabel('Time (min)', fontsize=15)
ax2.set_xlabel('Integrator', fontsize=15)
ax1.tick_params(axis='both', which='major', labelsize=12)
ax2.tick_params(axis='both', which='major', labelsize=12)

fig.tight_layout()
fig.savefig('E:/School/reu2024/research/summer2024/paper/plots/hydro_integrators_bar_graph.png', bbox_inches='tight', dpi=250)
