import numpy as np
import matplotlib.pyplot as plt



polyThick = float(input("Enter the thickness of Polyethylene-Boron Mass \n>>> ")) #cm
iceThick = float(input("Enter the thickness of Ice-Regolith Core Mass \n>>> ")) #cm

polyDensity = 0.95 #Borated HDPE
iceDensity = 1.20 #Titan Ice-regolith

I0 = 600 #Ambient GCR dose
lambdaGCR = 65.0 # attenuation lenght for low-Z materials
nasaLimit = 20.0

polyMassThickness = polyThick * polyDensity
iceMassThickness = iceThick * iceDensity
totalMassThickness = polyMassThickness + iceMassThickness

dose = I0 * np.exp(-totalMassThickness / lambdaGCR)

def main():
    print('='*90)
    print("RADIATION PROTECTION SIM")
    print('='*90)
    print(f'Polyethylene-Boron Mass Thickness: {polyMassThickness} g/cm^2')
    print(f"Ice-Regolith Core Mass Thickness:  {iceMassThickness}  g/cm^2")
    print(f"Total Shield Mass Thickness (Radiation protection) : {totalMassThickness} g/cm^2")
    print("="*90)
    print(f"Ambient Space Radiation: {I0:>6.1f} mSv/year")
    print(f"Cabin Radiation Dose: {dose:>6.1f} mSv/year")
    print(f"NASA safety limity for one year: {20.0:>6.1f} mSv/year")
    print("="*90)
    
    if dose <= 20.0:
        print("Conclusion\nPass (Shielding valuses are sufficient)")
    else:
        print("Conclusion\nFail (Shielding too thin)")

def Visualize():
    thRange = np.linspace(0, iceThick, 200)
    simMassThickness = polyMassThickness + (thRange * iceDensity)
    simDose = I0 * np.exp(-simMassThickness / lambdaGCR)
    
    plt.figure(figsize=(7, 4.5))
    plt.plot(thRange, simDose, color='#1f77b4', linewidth=2.5, label='Internal Cabin Radiation')
    plt.axhline(y=20.0, color="crimson", linestyle="--", linewidth=1.5, label='NASA Safe Limit')
    
    plt.scatter(iceThick, dose, color='darkorange', s=100, zorder=5, label='Design Point')
    plt.text(iceThick - 25, dose + 25, f"{dose:.1f} mSv/yr", weight='bold', color='darkorange')
    
    plt.title('Shield Performance: Radiation Attenuation vs. Core Thickness', fontsize=12, pad=15)
    plt.xlabel('Annual Ice-Regolith Shield Thickness (cm)', fontsize=10)
    plt.ylabel('Annual Dose Equivalent (mSv/year)', fontsize=10)
    plt.xlim(0, iceThick + 10)
    plt.ylim(0, I0 + 50)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(loc='upper right')
    plt.tight_layout()

    plt.show()

main()
Visualize()