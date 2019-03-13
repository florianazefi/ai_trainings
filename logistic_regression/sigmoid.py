import numpy as np
import matplotlib.pyplot as plt

ing_colors = {
        "orange"     : '#FF6200',
        "indigo"     : '#525199',
        "light grey" : '#A8A8A8',
        "mid grey"   : '#767676',
        "sky"        : '#60A6DA',
        "fuchsia"    : '#AB0066',
        "lime"       : '#D0D93C',
        "leaf"       : '#349651',
        "text color" : '#333333',
        }

x = np.linspace(-5,5,200)

def sigmoid(x, b0=0, b1=1):
    return 1 / (1 + np.exp(-b0 -b1*x))

plt.figure(figsize=(5.0, 4.0))
# plt.title(r'$\beta_1 = 1$')
plt.plot(x, sigmoid(x, b0=-1, b1=1), label=r'$\beta_0 = -3$', color=ing_colors['orange'])
plt.plot(x, sigmoid(x, b0=0, b1=1), label=r'$\beta_0 = 0$', color=ing_colors['indigo'])
plt.plot(x, sigmoid(x, b0=1, b1=1), label=r'$\beta_0 = +3$', color=ing_colors['leaf'])
plt.ylim(*plt.ylim())
plt.plot([0.,0.], plt.ylim(), 'k--', linewidth=1, color='grey')
plt.xlabel("x")
plt.ylabel(r'$(1 + e^{-\beta_0 - x})^{-1}$')
plt.legend(loc="upper left")
plt.savefig("sigmoid_b0.png", dpi=300, bbox_inches='tight')
plt.close()

plt.figure(figsize=(5.0, 4.0))
# plt.title(r'$\beta_0 = 0$')
plt.plot(x, sigmoid(x, b0=-0, b1=0.5), label=r'$\beta_1 = 0.5$', color=ing_colors['orange'])
plt.plot(x, sigmoid(x, b0=0, b1=1), label=r'$\beta_1 = 1$', color=ing_colors['indigo'])
plt.plot(x, sigmoid(x, b0=0, b1=2), label=r'$\beta_1 = 2$', color=ing_colors['leaf'])
plt.ylim(*plt.ylim())
plt.plot([0.,0.], plt.ylim(), 'k--', linewidth=1, color='grey')
plt.xlabel("x")
plt.ylabel(r'$(1 + e^{- \beta_1x})^{-1}$')
plt.legend(loc="upper left")
plt.savefig("sigmoid_b1.png", dpi=300, bbox_inches='tight')
plt.close()
