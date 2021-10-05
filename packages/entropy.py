# std libs
import math
from typing import Iterator


# funcs
def info_content(p: float) -> float:
    """Calculate information content (aka surpisal) of a event with probability P."""
    return -(math.log(p))


def calc_entropy(p_dist: list[float]) -> Iterator[float]:
    """Calculate the entropy of a probability distribution (list)."""
    # calculate
    return (sum(p * info_content(p) if p != 0 else 0 for p in p_dist))


def gen_uniform_pdist(states: int) -> float:
    """Create a uniform probability distribution."""
    # create lists of state probabilities
    for _ in range(states):
        # gen probability of state
        yield 1 / states
        

def uniform_entropy(states: int) -> float:
    """A simpler way to calculate entropy if probablities of all states are equal."""    
    # calculate
    return -(math.log(1 / states))


def gen_entropy(states: int) -> Iterator[float]:
    """Wrap all entropy calculating funcs."""
    return calc_entropy(gen_p_dist(states))


def gen_pdist(states: int, step: int = 1) -> Iterator[list]:
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
    
    
def gen_se_prob(start: int = 1, 
                stop: int = 100, 
                step: int = 1) -> Iterator[float]:
    """Generate single event probabilities."""
    # loop
    for event in range(start, stop, step):
        yield event/(stop)