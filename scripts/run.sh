#!/bin/sh
#!/bin/bash

for n in {1..32}; 
do
    echo Running simulation with $n processes...
    mpiexec -n $n ~/athena/bin/athena -i /data/khyaes/processes_test/athinput.rt2d > /data/khyaes/processes_test/${n}_processes.txt 
    echo Done running simulation with $n processes
    echo ''
done