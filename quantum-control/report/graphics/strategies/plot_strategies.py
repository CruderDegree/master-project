from numpy.lib.function_base import disp
from strategies import generate_control, term_structures, ampl_strats, displacement_strats
import numpy as np
import matplotlib.pyplot as plt

# Generate controls
t_steps = 101
t = np.linspace(0,1,t_steps)
max_terms = 6
n_plots = 25 # Number of controls plotted on 1 fig

fig, ax = plt.subplots()
for term_struct in term_structures:
    for amplification in ampl_strats:
        for displacement_strat in displacement_strats:
            for n_terms in range(3, max_terms+1):
                for i in range(n_plots):
                    u = generate_control(t, n_terms, term_struct, amplification, displacement_strat)
                    ax.plot(t, u, alpha=0.25)
                ax.set_xlabel(r"$t$")
                ax.set_ylabel(r"$u(t)$")
                ax.set_title(term_struct + " - " + str(n_terms) + " terms, amplification : " + amplification + " displacement:"+displacement_strat)
                filename = "./seeding_strats_controls/" + term_struct + "-amplification-"+ amplification+"-displacement-"+displacement_strat+"-" + str(n_terms) + "-terms"
                fig.savefig(filename+".pdf")
                fig.savefig(filename+".png")
                ax.clear()
