import matplotlib
matplotlib.use('TkAgg')  # GUI backend setting

import numpy as np
import matplotlib.pyplot as plt

# Frequency range (1 MHz - 10 GHz)
f = np.logspace(6, 10, 1000)

# Electrical conductivities (S/m)
sigma = np.array([
    5.8e7,  # Copper
    3.5e7,  # Aluminum
    1.0e7,  # Iron
    6.3e7,  # Silver
    1.3e7,  # Nickel
    4.1e7   # Gold
])

# Magnetic permeability (H/m)
mu = 4 * np.pi * 1e-7

# Skin depth calculation
delta = []
for s in sigma:
    delta.append(1 / np.sqrt(np.pi * mu * s * f))  # meters

# Convert to micrometers
delta = [d * 1e6 for d in delta]

# Material names
materials = ['Copper', 'Aluminum', 'Iron', 'Silver', 'Nickel', 'Gold']

# Plotting
plt.figure(figsize=(10, 6))
for i, material in enumerate(materials):
    plt.semilogx(f, delta[i], label=material, linewidth=1.5)

plt.title('Skin Depth vs Frequency', fontsize=13)
plt.xlabel('Frequency (Hz)')
plt.ylabel(r'Skin Depth  $\delta$  (µm)')
plt.grid(True, which='both', linestyle='--', linewidth=0.6)
plt.legend()
plt.tight_layout()
plt.show()
