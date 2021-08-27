# std libs
import math
import random


# funcs
def calc_entropy(p_dist):
    """Calculate the entropy of a probability distribution (list)."""
    # calculate
    return -(sum(p * math.log(p) for p in p_dist))


def gen_p_dist(states):
    """Create a random probability distribution."""
    # create lists of random state population
    state_pops = [random.randint(1, states) for _ in range(states)]
    
    # get total sum of randints
    total_value = sum(state_pops)
    
    # finally generate probability distribution
    for population in state_pops:
        # generate
        yield population / total_value
        

def gen_entropy(states):
    """Wrap all entropy calculating funcs."""
    return calc_entropy(gen_p_dist(states))


    