#!/bin/bash

### This script was for the automatic running of Athena++ with different solvers and equations of state AND outputs 
### data AND creates the plots/videos for each

declare -a solvers=('hlle hllc lhllc hlld lhlld roe llf')

PRECURSOR='[BASH SCRIPT]: '
TEST_DIR=/data/khyaes/solvers_test
export OMP_NUM_THREADS=16
ALL_DATA_DIR=${TEST_DIR}/lw_collapse

for solver in $solvers
    do
        SOLVER_DIR=${ALL_DATA_DIR}/${solver}
        DATA_DIR=$SOLVER_DIR/data
        PLOTS_DIR=$SOLVER_DIR/plots
        
        echo
        echo $PRECURSOR Changing solver
        echo $PRECURSOR Running simulation with $solver solver
        echo $PRECURSOR Configuring Athena...
        echo

        cd ~/athena
        python configure.py --prob=lw_implode -omp -hdf5 --flux=$solver --hdf5_path=$HDF5_DIR --include=/usr/include/openmpi-x86_64/ > ${ALL_DATA_DIR}/${solver}_configuration_output.txt

        if [ $? != 0 ]; then 
            echo
            echo $PRECURSOR The $solver solver and adiabatic EOS are not compatible 
            echo $PRECURSOR Moving to next solver...
            rm ${ALL_DATA_DIR}/${solver}_configuration_output.txt
            continue
        
        else
            mkdir $SOLVER_DIR
            mkdir $DATA_DIR
            mkdir $PLOTS_DIR
            make clean > /dev/null
            make -j 16 > ${SOLVER_DIR}/${solver}_make_output.txt
        fi
        
        echo
        echo $PRECURSOR Finished configuring Athena
        echo $PRECURSOR Changing to data directory...

        cd $DATA_DIR

        echo
        echo $PRECURSOR Running simulation with $solver solver in $PWD...

        ~/athena/bin/athena -i /data/khyaes/solvers_test/athinput.lw_implode > ${SOLVER_DIR}/${solver}_simulation_output.txt

        echo
        echo $PRECURSOR Finished running simulation and printing results

        echo
        echo $PRECURSOR Making plot images for data and rendering video...

        python /home/khayes/summer2024/scripts/plot_all.py > ${SOLVER_DIR}/${solver}_plot_output.txt 2>&1

        ffmpeg -r 25 -i ${PLOTS_DIR}/%1d.png ../video.mp4 > ${SOLVER_DIR}/${solver}_ffmpeg_output.txt 2>&1
        
        echo
        echo $PRECURSOR Done with all processes for $solver solver

    done

echo $PRECURSOR ALL DONE