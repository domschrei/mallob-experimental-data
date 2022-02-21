
# Experiments 

Every sub-sub-directory features a certain subset of the following files:

* `avg_comm_volumes`: The average number of integers sent around during clause exchange per round.
* `conflicts`: The total number of conflicts of all involved solver backends.
* `cdf_donetimes`: In scheduling experiments, this is like `cdf_runtimes` but with the _total_ run time of the entire system until an instance is resolved, i.e., it is a CDF over the response times of jobs (supposing that every job enters at t=0).
* `cdf_runtimes`: Contains two columns: The runtime `t` so far and the number of instances solved within `t` seconds (_per instance_).
* `cores_per_job`: Contains two columns: The runtime `t` so far and the average number of cores each job has access to.
* `donetimes`: List of qualified response times (see `cdf_donetimes` and `runtimes`).
* `jobs`: Contains two columns: The runtime `t` so far and the number of active jobs in the system.
* `load`: Contains two columns: The runtime `t` so far and the ratio of busy non-client PEs in the system.
* `par2score`: Average of individual runtimes, penalizing timeouts with twice the time limit. 
* `program_options`: The options the parallel solver was called with.
* `props`: The total number of propagations of all involved solver backends.
* `runtimes`: List of qualified runtimes. Contains three columns: Instance ID, delimiter, run time.
* `scheduled_jobs`: Contains two columns: The runtime `t` so far and the number of jobs scheduled so far.
* `scheduling_times`: Contains two columns: The instance ID and the elapsed time between it becoming ready to be scheduled and actually being scheduled.
* `solved_{sat,unsat}`: Number of solved SAT/UNSAT instances.
* `speedups_{lingeling,kissat}`: Per-instance speedups of a parallel solver over the sequential solver. Contains five columns: Instance ID, delimiter, speedup, sequential run time, parallel run time.
