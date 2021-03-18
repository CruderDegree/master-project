import numpy as np
import matplotlib.pyplot as plt
import json
import time

# Open Json file and return dict of contents
def readJson(filename: str) -> dict:
    f = open(filename, "r")
    dataDict = json.load(f)
    f.close()
    return dataDict

# Check whether control u is unique compared to list of unique ctrls by calculating euclidian norm
def isUniqueControl(u: list, uniqueControls: list, eps=1e-16) -> bool:
    for v in uniqueControls:
        euclidNorm = 0
        for t in range(len(v)):
            euclidNorm += (u[t] - v[t]) * (u[t] - v[t])
        if np.sqrt(euclidNorm) < eps:
            return False
        else:
            return True
    return True


if __name__ == "__main__":
    then = time.time()
    print_stuff = True # "Debug mode"

    filename = "landscape.json"
    data = readJson(filename)

    durations = data["durations"]
    n_iterations = int(data["noise_iter"])
    max_stepsize = 1
    min_fidelity = 0.1 # Minimum fidelity for solution to be analyzed
    min_optimizer_iterations = 101 # Minimum number of optimizations
    dx = (2 - -2) / (256-1) # Method as in qengine

    fig, ax = plt.subplots()

    InF_mean = np.zeros(len(durations) ) # Mean of infidelities
    InF_var = np.zeros( len(durations) )    # Variance of infidelities
    stepSize = np.zeros( len( durations ) )
    n_unique_controls = np.zeros( len( durations ), dtype=int)
    hessian_diag = np.zeros( len( durations ) )

    for idx,duration in enumerate(durations):
        uniqueControls = []
        InF_temp = np.zeros(n_iterations)
        stepSize_sum = 0
        hessian_diag_sum = 0
        iterations = 0
        for i in range(n_iterations):
            try:
                F = data["fidelity_grape_"+str(duration)][i]
                optimizer_iterations = int( data["iterations_"+str( duration ) + "_grape"][ i ] )
                stepsizes = data["stepsizes_" + str( duration ) + "_" + str( i )]
                control = data["ctrl_" + str( duration ) + "_grape"][ "data" ][i][ 0 ]
                hessian = data["hessianDiag_" + str( duration ) + "_" + str( i )]
            except KeyError:
                F = data["fidelity_grape_"+str( int(duration) )][i]
                optimizer_iterations = int( data["iterations_"+str( int(duration) ) + "_grape"][ i ] ) 
                stepsizes = data["stepsizes_" + str( int( duration ) ) + "_" + str( i )]
                control = data["ctrl_" + str ( int ( duration ) ) + "_grape"][ "data" ][ i ][ 0 ]
                hessian = data["hessianDiag_" + str( int( duration ) ) + "_" + str( i )]
            if F < min_fidelity or len(stepsizes) < min_optimizer_iterations: # Filter out bad runs w. no solution
                continue
            iterations += 1
            InF_temp[i] = 1-F 
            stepSize_sum += np.mean(stepsizes)
            if isUniqueControl(control, uniqueControls): # Check if ctrl is unique
                uniqueControls.append( control )
            if np.max(hessian) < 100:
                hessian_diag_sum += np.mean(hessian) # / dx / dx

        InF_mean[idx] = np.mean(InF_temp)
        InF_var[idx] = np.var(InF_temp)      
        stepSize[idx] = stepSize_sum / iterations
        n_unique_controls[idx] = len(uniqueControls)
        hessian_diag[idx] = hessian_diag_sum / iterations

    ax.plot([durations[0], durations[-1]], [0,0], 'k--', linewidth=0.7) # Line to guide eye
    ax.plot([duration for duration in durations] , InF_mean, 's-', label="Mean infidelity") # Mean infidelity
    ax.plot([duration for duration in durations] , InF_var, 'o-', label="Var infidelity") # Std of infidelity
    ax.plot([duration for duration in durations] , stepSize/max_stepsize, 'd-', label="Mean step size") # AVg step size
    ax.plot([duration for duration in durations] ,  n_unique_controls/max(n_unique_controls), 'v-', 
                                                    label="Unique controls / "+str(int( max(n_unique_controls) ))) 
                                                    # No. of unique controls / max unique controls
    ax.plot([duration for duration in durations] , hessian_diag / np.sum(hessian_diag), '^-', label="Normalized mean Hessian diag.") # Mean of hessian diagonal 
    ax.set( xlabel='Control duration [sim]',
            ylabel='Value')
    fig.legend(bbox_to_anchor=(0.6,1), framealpha=0.95)

    figurename = "Landscape"
    fig.savefig(figurename+".pdf")
    fig.savefig(figurename+".png")

    now = time.time()
    if print_stuff:
        print("Done! Time elapsed:",now-then,"s")
        print("Unique Controls:")
        print(n_unique_controls)
        print("Hessian diagonal")
        print(hessian_diag)


