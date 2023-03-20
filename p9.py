from matplotlib import pyplot as plt
import control

s = control.TransferFunction.s
# Write the value of G(s)H(s)
G = 1/((s+1)*(s+2)*(s+3))
rlist, klist = control.rlocus(G)
plt.show()
