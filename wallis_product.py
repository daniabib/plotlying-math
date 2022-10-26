import plotly.graph_objects as go
import numpy as np
from math import pi


def f(n):
    return (2*n)**2/((2*n - 1)*(2*n + 1))

assert f(1) == 4/3
assert f(2) == 16/15
assert f(3) == 36/35

def wallis_prod(n):
    return np.prod([f(x) for x in range(1, n+1)])

def plot_wallis_line(n: int = 26):
    ns = np.arange(1, n+1)
    # x = np.arange(1, n+1, .1)
    y = [wallis_prod(n) for n in range(1, n+1)]
    fig = go.Figure(data=go.Scatter(x=ns, y=y, name="Wallis Product"))
    fig.add_trace(go.Scatter(x=ns, y=[pi/2 for _ in ns], name="$$\pi/2$$"))
    fig.show()

def plot_wallis_scatter(n: int = 26):
    ns = np.arange(1, n+1)
    # x = np.arange(1, n+1, .1)
    sn = [wallis_prod(n) for n in range(1, n+1)]
    fig = go.Figure(data=go.Scatter(x=sn, y=ns, name="Wallis Product", mode='lines+markers'))
    # fig.add_trace(go.Scatter(x=ns, y=[pi/2 for _ in ns], name="$$\pi/2$$"))
    fig.show()


# plot_wallis_line(1000)
plot_wallis_scatter()