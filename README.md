# MooresNeighborhood
Python implementation of a 2d 100x100 grid Moore neighborhood cellular automa model

![download](https://user-images.githubusercontent.com/77468658/190838603-135556c2-d8dc-4ae0-af9b-518b31b97019.png)

i. How do these ratios change as the contagion progresses?

These ratios begin to converge as the process continues because T+1/T becomes
smaller and T/T+1 becomes bigger each timestep.

ii. To what values will the ratios converge if the simulation was to continue indefinitely?

The ratios will both converge to 1 , This happens because the difference between the
2 values T and T+1 will stay the same at 8 but the numbers T and T+1 will continue to
get bigger making the constant 8 smaller in comparison to the continuously growing
number of newly infected since the ratio will be 8(t)/(8(t-1)) when it is a higher number
like 20 steps it will be 160/152 which is 1.05 vs 2 steps 16/8 is 2.

iii. How does this particular contagion model differ from a model that allows cells to interact and
infect each other globally (i.e., across the entire grid)?

This contagion model doesn't have as many options of people to interact with and
since this model has a set number of people which it can interact with it will have a
steady linear rate of increase vs a rate that will depend on where each person infected
will go since they can move wherever you can't predict exactly which cell and when it will
get infected. In conclusion this model has way less variance than a model that can
globally interact.
