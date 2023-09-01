from matplotlib_venn import venn3
from matplotlib import pyplot as plt

set_N = 65
set_T = 45
set_F = 42
set_NT = 20
set_NF = 25
set_TF = 15
set_NTF = 8

# Create the Venn diagram
venn = venn2(subsets=(set_N - set_NT - set_NF + set_NTF, set_T - set_NT - set_TF + set_NTF, set_NT - set_NTF,
                      set_F - set_NF - set_TF + set_NTF, set_NF - set_NTF, set_TF - set_NTF, set_NTF),
             set_labels=('Newsweek', 'Times', 'Fortune'))

plt.title("Magazines Survey")
plt.show()