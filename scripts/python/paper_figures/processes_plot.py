import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({'text.usetex': True, 'font.family': 'serif', 'font.serif': 'Computer Modern'})


#data1 = pd.read_csv('/home/khayes/summer2024/athena/processes_test/processes_data1.txt', sep='\t', header=None)
data3 = open('/data/khyaes/processes_test/test4/data/all_data.txt', 'r')
data1 = open('/data/khyaes/processes_test/test2/data/all_data.txt', 'r')
data2 = open('/data/khyaes/processes_test/test3/data/all_data.txt', 'r')
time1 = []
time2 = []
time3 = []

for num in data1:
    if num != '\n':
        print(num)
        num = float(num)
        minutes = num / 60
        time1.append(minutes)

for num in data2:
    if num != '\n':
        num = float(num)
        minutes = num / 60
        time2.append(minutes)

for num in data3:
    if num != '\n':
        num = float(num)
        minutes = num / 60
        time3.append(minutes)

plt.plot(range(len(time1)), time1, marker='s', color='r', markersize=3)
plt.plot(range(len(time1)), time2, marker='s', color='b', markersize=3)
plt.plot(range(len(time1)), time3, marker='s', color='g', markersize=3)
plt.title('Performance by Time')
plt.xlim(-1, 33)
plt.ylim(0, 250)
plt.legend(['Test 1', 'Test 2', 'Test 3'])
plt.xlabel('Number of Processes')
plt.ylabel('Time (min)')
plt.savefig('/home/khayes/summer2024/paper/plots/processes_test.png', bbox_inches='tight', dpi=250)