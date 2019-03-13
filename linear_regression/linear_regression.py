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

xx = np.linspace(-20,60,200)

def f(x):
    return 5 + x/5.

x = np.random.uniform(-20, 60, 100)
y = f(x) + np.random.normal(0., 2.0, x.shape)

plt.figure(figsize=(5.0, 4.0))
plt.scatter(x, y, s=8, c=ing_colors["sky"])
plt.plot(xx, f(xx), color=ing_colors["orange"])
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("linear_regression.png", dpi=300)
plt.close()
