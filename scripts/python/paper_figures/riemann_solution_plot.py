import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

plt.rcParams.update({'mathtext.default':  'regular' })
plt.rcParams['text.usetex'] = True

def lines(x):
    y1 = x
    y2 = -x

    return y1, y2

x = np.linspace(0, 10, 100)
y1, y2 = lines(x)

plt.plot(y1, x, color='black')
plt.plot(y2, x, color='black')
plt.xlim(-11, 11)
plt.ylim(-1, 12)
plt.box(False)
plt.xticks([])
plt.yticks([])
plt.arrow(-10, 0, 20, 0, color='black', length_includes_head=True, head_width=0.1, head_length=0.15, head_starts_at_zero=True) # Horizontal
plt.arrow(0, 0, 0, 10, color='black', length_includes_head=True, head_width=0.1, head_length=0.15, head_starts_at_zero=True) # Vertical 
a = patches.FancyArrowPatch((-6.1, 6), (6.1, 6), connectionstyle="arc3,rad=-0.2")
plt.gca().add_patch(a)
plt.text(0.3, 9.8, 't', fontsize=8)
plt.text(9.8, -0.5, 'x', fontsize=8)
plt.text(3, 7, '$U^{HLL}$', fontsize=12)
plt.text(-11, 10.5, '$S_L$', fontsize=12)
plt.text(10.5, 10.5, '$S_R$', fontsize=12)
plt.text(-8.7, 1, '$U_L$', fontsize=12)
plt.text(8, 1, '$U_R$', fontsize=12)

plt.savefig('E:/School/reu2024/research/summer2024/paper/plots/riemann_solution.png', bbox_inches='tight', dpi=250)