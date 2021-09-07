# std libs
import math


# funcs
def calc_entropy(p_dist):
    """Calculate the entropy of a probability distribution (list)."""
    # calculate
    return -(sum(p * math.log(p) if p != 0 else 0 for p in p_dist))


def gen_uniform_pdist(states):
    """Create a uniform probability distribution."""
    # create lists of state probabilities
    for _ in range(states):
        # gen probability of state
        yield 1 / states
        

def uniform_entropy(states):
    """A simpler way to calculate entropy if probablities of all states are equal."""    
    # calculate
    return -(math.log(1 / states))


def gen_entropy(states):
    """Wrap all entropy calculating funcs."""
    return calc_entropy(gen_p_dist(states))


def gen_pdist(states, step=1):
    """Generate all whole integer percentage probability distribution."""
    # get starting point
    pdist = [100] + ([0] * (states - 1))
    
    # indexes
    donating, event = 0, 1
    
    # begin loop
    while not pdist[-1] // 100:
        # go on and yield
        yield [event / 100 for event in pdist]
        
        # update event
        pdist[event] += step
                
        # update donating event
        pdist[donating] -= step
        
        # update donating index
        donating = donating + (pdist[donating] == 0)
        
        # get next event index
        event = event % (states - 1) + donating + 1
        
    # final yield
    yield [event / 100 for event in pdist]