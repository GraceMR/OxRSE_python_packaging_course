# tstools/__init__.py
from .moments import get_mean_and_var
from .vis import plot_histogram

import tstools

# instead of mean, var = tstools.moments.get_mean_and_var(...)
mean, var = tstools.get_mean_and_var(timeseries) 

# instead of fig, ax = tstools.vis.plot_histogram(...)
fig, ax = tstools.plot_histogram(timeseries, 4*np.sqrt(var)) 
