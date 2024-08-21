import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
plt.rcParams['text.usetex'] = True

def lines(x):
    y1 = x
    y2 = -x
    y3 = 0.5*x

    return y1, y2, y3

x = np.linspace(0, 10, 100)
y1, y2, y3= lines(x)

plt.plot(y1, x, color='black')
plt.plot(y2, x, color='black')
plt.plot(y3, x, color='black')
plt.xlim(-11, 11)
plt.ylim(-1, 12)
plt.box(False)
plt.xticks([])
plt.yticks([])
plt.arrow(-10, 0, 20, 0, color='black', length_includes_head=True, head_width=0.1, head_length=0.15, head_starts_at_zero=True) # Horizontal
plt.arrow(0, 0, 0, 10, color='black', length_includes_head=True, head_width=0.1, head_length=0.15, head_starts_at_zero=True) # Vertical 
a1 = patches.FancyArrowPatch((-6.1, 6), (3.1, 6), connectionstyle="arc3,rad=-0.2")
a2 = patches.FancyArrowPatch((2.9, 6), (6.1, 6), connectionstyle="arc3,rad=-0.2")
plt.gca().add_patch(a1)
plt.gca().add_patch(a2)
plt.rcParams.update({'mathtext.default':  'regular' })
plt.text(0.3, 9.8, 't', fontsize=8, fontname='Times New Roman')
plt.text(9.8, -0.5, 'x', fontsize=8, fontname='Times New Roman')
plt.text(-11, 10.5, '$S_L$', fontsize=12, fontname='Times New Roman')
plt.text(10.5, 10.5, '$S_R$', fontsize=12, fontname='Times New Roman')
plt.text(4.8, 10.5, '$S^*$', fontsize=12, fontname='Times New Roman')
plt.text(-2.3, 7.1, '$U_{L*}$', fontsize=12, fontname='Times New Roman')
plt.text(4.5, 6.6, '$U_{R*}$', fontsize=12, fontname='Times New Roman')
plt.text(-8.7, 1, '$U_L$', fontsize=12, fontname='Times New Roman')
plt.text(8, 1, '$U_R$', fontsize=12, fontname='Times New Roman')

plt.savefig('E:/School/reu2024/research/summer2024/paper/plots/star_region_plot.png', bbox_inches='tight', dpi=250)