#  Saturnian System Orbital Habitat: Radiation Shielding Optimization Simulation

This repository contains the mathematical frameworks, Python source code, and performance optimization models for the hull architecture of our **National Space Society (NSS) Gerard K. O'Neill Space Settlement Contest** submission. 

The simulation utilizes deep-space nuclear attenuation physics to validate a multi-layered hull design targeting long-term habitability within Saturn's harsh orbital radiation environment.

---

##  Multilayer Hull Architecture Design

The engineered shielding stack is specifically designed to handle primary Galactic Cosmic Rays (GCR), secondary neutron cascade fragmentation, and orbital ring hypervelocity debris. 

### Layer Configuration (Outermost to Innermost)
1. **Whipple Sacrificial Debris Bumper**: 5mm Carbon-Fiber Reinforced Polymer (CFRP) to fracture micro-meteoroid elements.
2. **Vacuum Standoff Gap**: 150mm spatial void to allow the expansion and dispersion of shockwave kinetic debris clouds.
3. **Kinetic Energy Catcher Blanket**: 12mm integrated Nextel and Kevlar multi-ply fabrics.
4. **Neutron Thermalization Buffer**: 100mm (10cm) 5% Boron-loaded High-Density Polyethylene (HDPE) to moderate and capture secondary neutrons.
5. **Bulk GCR Core Mass Shield**: 2,000mm (200cm) In-Situ Resource Utilization (ISRU) Titan Ice-Regolith Composite matrix.
6. **Inner Pressure Air-Hull**: 45mm Structural Aluminum-Lithium alloy containing a sea-level 1 atm life-support atmosphere.

---

## Optimization & Physics Methodology

The core software model implements the **Beer-Lambert Exponential Attenuation Law** across custom physical material properties to calculate cumulative **Mass Thickness (\(X\))** in \(\text{g/cm}^2\):

\[X = \sum (\text{Thickness}_i \times \text{Density}_i)\]

The resulting dose attenuation equation evaluates total deep-space protection:

\[I = I_0 \cdot e^{-\frac{X}{\lambda}}\]

### Simulation Metrics & Inputs:
* **Ambient GCR Background (\(I_0\))**: \(600 \text{ mSv/year}\) (Solar Minimum baseline environment).
* **Low-Z Mean Free Attenuation Path (\(\lambda\))**: \(65 \text{ g/cm}^2\).
* **Polyethylene Shield Density**: \(0.95 \text{ g/cm}^3\).
* **Titan Ice-Regolith Core Density**: \(1.20 \text{ g/cm}^3\).
* **Target Safety Parameter**: \(\leq 20 \text{ mSv/year}\) (Modern NASA Astronaut Career Boundary).

---

## Execution Guide
(you can also download the executable if a release is available)

### Prerequisites
Ensure your local machine has a Python 3 framework with standard data handling and visualization dependencies installed:

```bash
pip install numpy matplotlib
```

### Running the Optimizer Simulation
1. Clone or download this repository file structure to your workstation workspace.
2. Run the optimization engine script via terminal shell or IDE environments:

```bash
python RadiationSimulation.py
```

Note: This ReadMe was created with the use of AI. Meanwhile, all the code is written by me.
