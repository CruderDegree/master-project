import matplotlib.pyplot as plt

beta = [-20, -16, -15,-14,-10,-5,-2,-1,0,0.5,1 ,1.5,2,3,4,5,8,10,11 ,12.5 ,13.5,15 ,17.5 ,18.5 ,20 ]
F = [0.01,0.03,0.223,0.108,0.06,0.02,0.143,0.342,0.783,0.783,0.782,0.674,0.649,0.617,0.537,0.437,0.33,0.498,0.64,0.506,0.209,0.056,0.232,0.021,0.137
]

minb = -20
maxb = 20
plt.plot(beta,F, 'k-', linewidth=0.5)
plt.plot(beta,F, 'b.')
#plt.plot([2*minb, 2*maxb], [0.783, 0.783], 'r--')
plt.xlabel("β")
plt.ylabel("Fidelity at t=T")
plt.xlim(-22, 22)

filename = "beta"
plt.savefig(filename+".pdf")
plt.savefig(filename+".svg")
plt.savefig(filename+".png")

