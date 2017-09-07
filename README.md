# Patient-Queuing-System
Single Server Queuing System which handles relapse cases

The model builds a queuing system for a single server for the given arrival rate of 20 per 100 hrs and service time of 3 hrs.
Every patient has 30% chances to relapse.
The model uses poisson distribution to generate arrival time and binomial distribution for 10 relpase cases.
Follows FIFO discipline. Every relapse is treated as a new arrival.
