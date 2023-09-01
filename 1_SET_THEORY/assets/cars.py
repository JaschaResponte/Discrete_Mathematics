from matplotlib_venn import venn3
from matplotlib import pyplot as plt

set_A = 15
set_R = 12
set_W = 11
set_AW = 5
set_AR = 9
set_RW = 4
set_ARW = 3

venn = venn3(subsets=(set_A - set_AW - set_AR + set_ARW, set_R - set_AR - set_RW + set_ARW, set_AR - set_ARW,
                      set_W - set_AW - set_RW + set_ARW, set_RW - set_ARW, set_AW - set_ARW, set_ARW),
             set_labels=('A', 'R', 'W'))

plt.title("Cars Survey")
plt.show()