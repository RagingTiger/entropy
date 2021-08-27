# std libs
import math


# funcs
def calc_entropy(p_dist):
    """Calculate the entropy of a probability distribution (list)."""
    # calculate
    return -(sum(p * math.log(p) for p in p_dist))


def gen_p_dist(states):
    """Create a uniform probability distribution."""
    # create lists of state probabilities
    for _ in range(states):
        # gen probability of state
        yield 1 / states
        

def shortcut_entropy(states):
    """A simpler way to calculate entropy if probablities of all states are equal."""
    # get probability of one state
    p = 1 / states
    
    # now get entropy
    return -(p * math.log(p) * states)


def gen_entropy(states):
    """Wrap all entropy calculating funcs."""
    return calc_entropy(gen_p_dist(states))  