from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

x0 = 3.5
zmin = -0.2

x = np.linspace(-x0,x0,101)
y = np.linspace(-x0,x0,101)
X,Y = np.meshgrid(x,y)
Z = 1/np.pi * np.exp(-(X-1)**2 - (Y-0.5)**2)


fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')

plt.xticks(fontsize=0)
plt.yticks(fontsize=0)


surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, alpha=0.8, cmap=cm.coolwarm)
cset = ax.contourf(X, Y, Z, zdir='z', offset=zmin, cmap=cm.coolwarm)
cset = ax.contourf(X, Y, Z, zdir='x', alpha= 0.3, offset=-np.max(x), cmap=cm.coolwarm)
cset = ax.contourf(X, Y, Z, zdir='y', alpha= 0.3, offset=np.max(y), cmap=cm.coolwarm)


#ax.set_xlabel('q')
ax.set_xticks([])
ax.set_xlim(-x0, x0)
#ax.set_ylabel('p')
ax.set_yticks([])
ax.set_ylim(-x0, x0)
#ax.set_zlabel('z')
ax.set_zticks([])
ax.set_zlim(zmin,0.35)
#ax.set_title('3D surface with 2D contour plot projections')

#plt.axis('off')

plt.savefig('my_icon.png',format='png', dpi=300, bbox_inches='tight')
plt.show()
