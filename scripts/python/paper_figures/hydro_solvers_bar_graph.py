import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

implosion_data = pd.read_csv('E:/School/reu2024/research/summer2024/athena/solvers_test/implosion_solvers_data.csv', header=None)
rt_data = pd.read_csv('E:/School/reu2024/research/summer2024/athena/solvers_test/rt_solvers_data.txt', header=None)
solvers = []
rt_times = []
implosion_times = []

for solver in rt_data.iloc[0:,0]:
    solvers.append(solver.upper())

for time in implosion_data.iloc[:,2]:
    implosion_times.append(float(time))

for time in rt_data.iloc[:,1]:
    rt_times.append(float(time)/60)

print(rt_times)
print(implosion_times)

df1 = pd.DataFrame(
   dict(
      names=solvers,
      marks=rt_times
   )
)

df2 = pd.DataFrame(
   dict(
      names=solvers,
      marks=implosion_times
   )
)

df1_sorted = df1.sort_values('marks')
df2_sorted = df2.sort_values('marks')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

ax1.bar('names', 'marks', data=df1_sorted, color='#DE6449')
ax2.bar('names', 'marks', data=df2_sorted, color='#4F9D69')
ax1.set_title('Rayleigh-Taylor Instability', size=20)
ax2.set_title('Implosion', size=20)
ax1.set_xlabel('Solver', fontsize=15)
ax1.set_ylabel('Performance by Time (min)', fontsize=15)
ax2.set_xlabel('Solver', fontsize=15)
ax1.tick_params(axis='both', which='major', labelsize=12)
ax2.tick_params(axis='both', which='major', labelsize=12)

fig.tight_layout()
fig.savefig('E:/School/reu2024/research/summer2024/paper/plots/hydro_solvers_bar_graph.png', bbox_inches='tight', dpi=250)
