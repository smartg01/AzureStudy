

E Series is high memory usage
B series is burstable series
L Family is storage optimised allowing higher disk throughput
F Family is compute optimised allowing for extra CPUs.


## CPU baseline

Each size VM has a “baseline” CPU amount, from 10% to 135%. Your VM will earn CPU credits any time that it is under the baseline CPU threshold, and spend CPU credits any time that it is over (up to a maximum). B series servers can idle along most of the time, and then boost up to 400% of the baseline performance – i.e. it can use up to 16 cores if needed, rather than just the allocated 4 cores. 

[source](https://www.onenet.co.nz/whitepapers/babbling-about-azure-b-series-burstable-vms)

