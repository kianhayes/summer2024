#!/bin/bash

### This script was for the automatic running of Athena++ with different solvers and equations of state AND outputs data AND creates the plots/videos for each

declare -a eos=('adiabatic isothermal')
declare -a solvers=('hlle hllc lhllc hlld lhlld roe llf')

PRECURSOR='[BASH SCRIPT]: '
i=1
TEST_DIR=/data/khyaes/solvers_test
export OMP_NUM_THREADS=16
ALL_DATA_DIR=${TEST_DIR}/test2

for eos in $eos
do
    for solver in $solvers
        do
            SOLVER_EOS_DIR=${ALL_DATA_DIR}/${eos}_${solver}
            DATA_DIR=$SOLVER_EOS_DIR/data
            PLOTS_DIR=$SOLVER_EOS_DIR/plots
            
            echo
            echo $PRECURSOR Changing solver and/or EOS
            echo $PRECURSOR Running simulation with $solver solver and $eos EOS 
            echo $PRECURSOR Configuring Athena...
            echo

            cd ~/athena
            python configure.py --prob blast -b -omp -hdf5 --flux=$solver --eos=$eos --hdf5_path=$HDF5_DIR --include=/usr/include/openmpi-x86_64/ > ${ALL_DATA_DIR}/${eos}_${solver}_configuration_output.txt

            if [ $? != 0 ]; then 
                echo
                echo $PRECURSOR The $solver solver and $eos EOS are not compatible 
                echo $PRECURSOR Moving to next solver and EOS...

                ## TODO have the configuration output file removed when this error occurs
                
                continue
            
            else
                mkdir $SOLVER_EOS_DIR
                mkdir $DATA_DIR
                mkdir $PLOTS_DIR

                make clean > /dev/null
                make -j 16 > ${SOLVER_EOS_DIR}/make_output.txt
                
            fi
            
            echo
            echo $PRECURSOR Finished configuring Athena
            echo $PRECURSOR Changing to data directory...

            cd $DATA_DIR

            echo
            echo $PRECURSOR Running simulation with $solver solver and $eos EOS in $PWD...

            ~/athena/bin/athena -i /data/khyaes/solvers_test/athinput.blast > ${SOLVER_EOS_DIR}/simulation_output.txt

            echo
            echo $PRECURSOR Finished running simulation and printing results

            echo
            echo $PRECURSOR Making plot images for data and rendering video...

            python /home/khayes/summer2024/scripts/plot_all.py > ${SOLVER_EOS_DIR}/plot_output.txt

            ffmpeg -r 10 -i ${PLOTS_DIR}/%1d.png ../video.mp4 > ${SOLVER_EOS_DIR}/ffmpeg_output.txt
            
            echo
            echo $PRECURSOR Done with all processes for $solver solver and $eos EOS

            i=$((i + 1))
        done
        
    i=$((i + 1))
done

echo $PRECURSOR ALL DONE