""" 
Write down any strategies that come to mind 
Import this module in other scripts to centralize strategies
"""

import numpy as np

term_structures = ["sin", "cos", "both", "alt_sin", "alt_cos"] # term structures that 'generate controls' recognizes
ampl_strats = ["none", "endpoints", "middle"]
displacement_strats = ["both", "none", "frequency", "cosine"]

def r():
    """ Random number betw. -1 and 1"""
    return (np.random.rand() - 0.5) * 2

def generate_control(t : np.array, n_terms : int, structure : str, amplify : str, displacement : str, rescale=True) -> np.array:
    """ 
    Structure can be any of sin, cos, both, alt_sin or alt_cos
    amplify determines which portions of the control should be amplified compared to others. This can be either 'endpoints', 'middle' or 'none'
    Displacement accounts for correcting y-axis displacements away from 0. These can arise both from frequencies and cosine terms. 
    arguments can be "both", "none", "cosine", "frequency"
    Whole periods ensures that all periods are multiple of k*pi
    Displace y displaces y to ensure starting at u(0) = 0
    rescale rescales the control by dividing by the number of terms
    """
    u = np.zeros_like(t)
    terms = 0
    for k in range(1, n_terms + 1):
        if structure in ["sin", "both"] or (structure is "alt_sin" and k%2 ==1) or (structure is "alt_cos" and k%2 == 0):
            p = r() if displacement not in ["both", "frequency"] else 1
            u += r() * np.sin(p * k * np.pi * t)
            terms += 1
        if structure in ["cos", "both"] or (structure is "alt_cos" and k%2 ==1) or (structure is "alt_sin" and k%2 == 0):
            p = 2*r() if displacement not in ["both", "frequency"] else 2
            q = r()
            u += q * np.cos(p * k * np.pi * t)
            terms += 1
            if displacement in ["both", "cosine"]:
                u -= q if p>0 else -q

    if amplify == "endpoints":
        u *= (np.cos(2 * np.pi * t) + 2) # Scales endpoints by up to 3
    elif amplify == "middle":
        u *= (2 * np.sin(np.pi * t) + 1) # Scales middle points by up to 3

    if rescale:
        u /= terms
    return u

if __name__ == "__main__":
    print("Test random numbers")
    print([r() for i in range(10)])
