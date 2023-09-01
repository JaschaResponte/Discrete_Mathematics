from matplotlib_venn import venn2
from matplotlib import pyplot as plt

set_A = {"2","3","4","5"}
set_B = {"2","4","6","8","10"} #limiting to 10 here for the sake of demonstration


venn = venn2([set_A,set_B], set_labels=('A', 'B'))
venn.get_label_by_id("10").set_text('\n'.join(set_A - set_B))
venn.get_label_by_id("11").set_text('\n'.join(set_A & set_B))
venn.get_label_by_id("01").set_text('\n'.join(set_B - set_A))

plt.title("Sets A and B")
plt.show()