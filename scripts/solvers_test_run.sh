#!/bin/bash

declare -a eos=('adiabatic isothermal')
declare -a solvers=('hlle hllc lhllc hlld lhlld roe llf')

PRECURSOR='[BASH SCRIPT]: '
i=1

for eos in $eos
do
    for solver in $solvers
        do
            echo
            echo $PRECURSOR Changing solver and/or EOS
            echo $PRECURSOR Running simulation with $solver solver and $eos EOS 
            echo $PRECURSOR Configuring Athena...
            echo

            cd ~/athena
            python configure.py --prob blast --flux $solver --eos $eos -b -mpi -hdf5 --hdf5_path=$HDF5_DIR --mpiccmd=/usr/lib64/mpich/bin/mpicxx

            if [ $? != 0 ]; then 
                echo
                echo $PRECURSOR The $solver solver and $eos EOS are not compatible 
                echo $PRECURSOR Moving to next solver and EOS...
                continue
            
            else
                make clean
                make -j 10
            
            fi
            
            echo
            echo $PRECURSOR Finished configuring Athena
            echo $PRECURSOR Changing to data directory...

            cd /data/khyaes/solvers_test

            echo
            echo $PRECURSOR Running simulation with $solver solver and $eos EOS...

            mpiexec -np 16 ~/athena/bin/athena -i /data/khyaes/solvers_test/athinput.blast > /data/khyaes/solvers_test/${i}_${solver}_${eos}.txt

            echo
            echo $PRECURSOR Finished running simulation and printing results

            i=$((i + 1))
        done
        
    i=$((i + 1))
done

echo $PRECURSOR DONE