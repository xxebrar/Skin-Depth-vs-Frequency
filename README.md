# Skin Depth vs Frequency

This project calculates and visualizes the **skin depth (δ)** of several conductive materials as a function of frequency.

Skin depth is defined as:

\[
\delta = \frac{1}{\sqrt{\pi f \mu \sigma}}
\]

Where:
- **f** → Frequency (Hz)
- **μ** → Magnetic permeability (H/m)
- **σ** → Electrical conductivity (S/m)

The script computes the skin depth for:
- Copper  
- Aluminum  
- Iron  
- Silver  
- Nickel  
- Gold  

The resulting skin depth curves are plotted using a **semilogarithmic frequency axis** in **micrometers (µm)**.

---

## Requirements

Install necessary packages:

```bash
pip install numpy matplotlib
