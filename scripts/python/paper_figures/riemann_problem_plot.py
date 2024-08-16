import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'mathtext.default':  'regular' })
plt.rcParams["font.family"] = "Times New Roman"
plt.axhline(8, 0.2, 0.499, color='black')
plt.axhline(3, 0.5, 0.8, color='black')
plt.xlim(-11, 11)
plt.ylim(0.1, 12)
plt.box(False)
plt.xticks([-3.5, -0.008, 3.5], ['$x_i$', '$x_{i+1/2}$', '$x_{i+1}$'])
plt.yticks([])
plt.arrow(-10, 0.2, 20, 0, color='black', length_includes_head=True, head_width=0.1, head_length=0.15, head_starts_at_zero=True) # Horizontal
plt.arrow(0, 0.12, 0, 10, color='black', length_includes_head=True, head_width=0.1, head_length=0.15, head_starts_at_zero=True) # Vertical 
plt.text(0.3, 9.8, 'U', fontsize=8, fontname='Times New Roman')
plt.text(9.8, -0.5, 'x', fontsize=8, fontname='Times New Roman')
plt.text(-3.8, 7.3, '$U_L$', fontsize=10, fontname='Times New Roman')
plt.text(3.2, 2.3, '$U_R$', fontsize=10, fontname='Times New Roman')
plt.savefig('E:/School/reu2024/research/summer2024/paper/plots/riemann_problem.png', bbox_inches='tight', dpi=250)