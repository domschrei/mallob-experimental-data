
# mallob-experimental-data

This repository serves as a documentation for the experiments described in our SAT 2021 publication "Scalable SAT Solving in the Cloud".

For more details on our experiments, please consult the supplementary material PDF in this directory.

We also invite you to take a look at [Animallob](https://dominikschreiber.de/animallob), an interactive visualization of selected load balancing experiments.

## Used Software

The softwares we evaluate are located here:

* Mallob: https://github.com/domschrei/mallob
* Hordesat (updated): https://github.com/domschrei/hordesat
* Lingeling: https://github.com/arminbiere/lingeling
* Kissat: https://github.com/arminbiere/kissat

## Content

* `experiments/`: Contains the gathered experimental data. **Note:** As our system produced many Gigabytes of logging output, we only provide condensed runtime and performance information for each (set of) experiments. Please let us know if you wish to access some full logs or if you are missing some relevant data about an experiment.
* `figures/`: Some figures and plots we produced from the data in `experiments/` which may be useful or interesting (some of which are included in the main paper or in the supplementary material).
* `instances/`: The raw data and the result of our careful benchmark selection process.
