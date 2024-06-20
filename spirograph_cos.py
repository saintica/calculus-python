import math
import numpy as np
import matplotlib.pyplot as plt

    
N = 15
M = 15
fig, axs = plt.subplots(nrows=N, ncols=M, figsize=(12,12))
fig.set_facecolor("#f4f0e8")
n_points = 10000

for n in range(N):
    for m in range(M):
        k = (m+1)*math.gcd(m+1, n+1)
        theta = np.linspace(0., 2*np.pi*k, n_points)
        r = np.sin((n+1)/(m+1)*theta)
        axs[n,m].plot(r*np.sin(theta), r*np.cos(theta), color="#383b3e", linewidth=0.5)
        axs[n,m].tick_params(bottom=False, top=False, left=False, right=False, labelbottom=False, labeltop=False, labelleft=False, labelright=False) 
        axs[n,m].set_aspect('equal', 'box')
        axs[n,m].set_facecolor("#f4f0e8")
        axs[n,m].set_xlim([-1.1, 1.1])
        axs[n,m].set_ylim([-1.1, 1.1])
        for spine in ['top','bottom','left','right']:
            axs[n,m].spines[spine].set_visible(False)
for ax, row in zip(axs[:,0], [f"{n+1}" for n in range(N)]):
    ax.set_ylabel(row, rotation=0, size='large', labelpad=8)
for ax, col in zip(axs[-1], [f"{m+1}" for m in range(M)]):
    ax.set_xlabel(col,size='large')
fig.supxlabel('m', fontsize=20, y=0.05)
fig.supylabel('n', fontsize=20, rotation=0, x=0.07)
fig.suptitle(r"$r  =  \sin\left(\frac{n}{m} \theta\right)$", fontsize=20)
plt.show()
