from matplotlib import pyplot as plt
from matplotlib_venn import venn3_circles, venn3_unweighted
from matplotlib_venn import _common, _venn3
from matplotlib.patches import Circle

# Set of values.
subsets=(6316, 21369, 3104, 1098048, 2843, 3791, 1052)

# Adding venn diagram.
v = venn3_unweighted(subsets, set_labels = ('Strelka_0.3', 'VarScan_0.3', 'Truth_Data'), set_colors=('red', 'orange', 'skyblue'))
areas = (1, 1, 1, 1, 1, 1, 1)
centers, radii = _venn3.solve_venn3_circles(areas)

# Saving the values.
plt.title("Positions")
plt.show()
plt.savefig('Tumor_Purity_0.3_Positions_Plot.pdf')
