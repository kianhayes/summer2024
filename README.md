# Kian Hayes Summer 2024 Benedictine College Research #
This repository serves the purpose of documenting my research conducted during the summer of 2024 at Benedictine College. I'm currently in the process of writing a paper for this independent research project in which a draft for can be seen in the /plots directory.

The research entails testing the performance of Athena++. Specifically, the performance of Riemann solvers and integrators included in the code along with its parallelization capabilities. 

A draft of the paper produced from this research can be found here:
[Paper Draft.pdf](https://github.com/user-attachments/files/17722670/draft3.pdf)

Abstract of paper:
The performance of several popular Riemann solvers and time integrators in the hydrodynamics simulation code Athena++ is studied. The results of which show that the Local-Lax-Friedrich’s (LLF) solver has the fastest time to completion but prominent dissipation due to the nature of this solver and its exclusion of solutions to the Riemann problem that feature shocks and other discontinuities. For integrators, we find that the VL2 integrator performs best with the lowest time to completion for all test problems. We confirm as proposed in Stone et al. (2020) that the HLLD and HLLC solvers and VL2 integrator are most suitable for general simulations involving shocks and other discontinuities in MHD and hydrodynamic problems respectively. Lastly, the parallelization capabilities of Athena++ are also tested in which we find an exponential decaying relation between the number of processes and run time of the simulation.

Below I detail the various directories in this repository:

## /athena ##
Contains various animations or plots from simulations and spreadsheets that I used to track data. 

#### Animation of the MHD Blast Problem ####
https://github.com/kianhayes/summer2024/assets/107010861/4fe7b556-7a0d-4230-9471-3a71c59400bb

### /athena/integrators_test ###
Files and data associated with the tests conducted to study the performance of various integrators that come with Athena++. 

![rt_integrator_multiplot](https://github.com/user-attachments/assets/dc34780d-996e-425c-9df6-343d13e087dc)
Plot showing the simulation results between the five integrators ran on the same test problem. 

![hydro_integrators_bar_graph](https://github.com/user-attachments/assets/f0b46caa-57f6-41f2-998b-f86f307a5f7a)
Bar graph showing the performance of different integrators based on their time to complete the Implosion and Rayleigh-Taylor instability simulations.

### /athena/solvers_eos_test ###
This contains files related to a test conducted to explore the performance of different Riemann solvers included in Athena++. The test included the use of both hydrodynamic and MHD test problems. 

![kh_solvers_multiplot](https://github.com/user-attachments/assets/03314536-6f50-462e-8e61-9f0b022c7463)
![implosion_solvers_multiplot](https://github.com/user-attachments/assets/8eecde8e-9114-42bb-8e1d-342840510222)

Plot showing the simulation results of various Riemann solvers. 

![mhd_solvers_bar_graph](https://github.com/user-attachments/assets/b61486db-6425-4f57-8edc-a2a376f4783e)
Bar graph showing the time to completion for the different Riemann solvers on two MHD test problems, the MHD blast and Leocant Kelvin-Helmholtz instability.

### /athena/processes_test ###
This contains the data and animations associated with the test conducted exploring the performance of running a different amount of parallelized processes for a simulation. The test compares running a simulation at 1 process all the way to 32 processes.

![processes_test](https://github.com/user-attachments/assets/86b3e4d1-0090-4b74-879e-19a9ed9adc6f)
Plot showing the results of 3 different tests studying the parallelization capabilities of Athena++, with the y-axis being time to completion and x-axis being the number of processes used to run the simulation. The 3 tests have varying computational costs. 

### Animation of the Rayleigh-Taylor Instability Problem ###
https://github.com/kianhayes/summer2024/assets/107010861/645ae73a-f704-4c2a-9e4e-89751f9d8556

## /paper ##
Contains plots used in the paper I'm writing for the research I conducted over the summer. A draft of the paper is also included in this directory. 

## /scripts ##
Contains Python and Bash scripts that I used to streamline data processing and data collection. This is anywhere from plotting data output by Athena++ or automating iterative processes during tests.



