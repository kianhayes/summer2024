import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('E:/School/reu2024/research/summer2024/athena/solvers_test/mhd_solvers_data.csv')
data2 = open('E:/School/reu2024/research/summer2024/athena/solvers_test', 'r')
solvers = []
blast = []
kh = []

for solver in data.iloc[:,0]:
    solvers.append(solver)

for time in data.iloc[:,2]:
    blast.append(float(time))

for time in data.iloc[:,4]:
    kh.append(float(time))

df1 = pd.DataFrame(
   dict(
      names=solvers,
      marks=blast
   )
)

df2 = pd.DataFrame(
   dict(
      names=solvers,
      marks=kh
   )
)

df1_sorted = df1.sort_values('marks')
df2_sorted = df2.sort_values('marks')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

ax1.bar('names', 'marks', data=df1_sorted, color='#555B6E')
ax2.bar('names', 'marks', data=df2_sorted, color='#90BEDE')
ax1.set_title('MHD Blast', size=20)
ax2.set_title('Leocant KH', size=20)
ax1.set_xlabel('Solver', fontsize=15)
ax1.set_ylabel('Performance by Time (min)', fontsize=15)
ax2.set_xlabel('Solver', fontsize=15)
ax1.tick_params(axis='both', which='major', labelsize=12)
ax2.tick_params(axis='both', which='major', labelsize=12)

fig.tight_layout()
fig.savefig('E:/School/reu2024/research/summer2024/paper/plots/mhd_solvers_bar_graph.png', bbox_inches='tight', dpi=100)