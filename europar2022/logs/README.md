
# logs/

Each directory corresponds to one certain run of Mallob. In each directory, you can find the following files and directories:

* `slurm-*.out`: The log file generated by SLURM, the job scheduler employed at the used supercomputer.
* `*/`: Each directory `i` contains all log files created by MPI rank `i`. Due to space limitations, we only provide these directories for rank zero as well as for each rank which we configured to introduce jobs to the system.