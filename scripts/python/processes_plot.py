import matplotlib.pyplot as plt
import pandas as pd

data1 = pd.read_csv('/home/khayes/summer2024/athena/processes_test/processes_data1.txt', sep='\t', header=None)
data2 = open('/data/khyaes/processes_test/test2/data/all_data.txt', 'r')
time1 = []
time2 = []

for num in data1.iloc[1:, 2]:
    time1.append(float(num))

for num in data2:
    if num != '\n':
        num = float(num)
        minutes = num / 60
        time2.append(minutes)

plt.plot(range(1, 33), time1, marker='s', color='r', markersize=3)
plt.plot(range(1, 33), time2, marker='s', color='b', markersize=3)
plt.title('Performance by Time')
plt.xlim(0, 33)
plt.ylim(0, 150)
plt.legend(['Test 1', 'Test 2'])
plt.xlabel('Number of Processes')
plt.ylabel('Time (min)')
plt.savefig('/home/khayes/summer2024/paper/plots/processes_test.png', bbox_inches='tight', dpi=250)
