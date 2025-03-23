import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def plot_general_logs(df):
    fig, axes = plt.subplots(nrows=1, ncols=5, figsize=(10, 10), sharey=True)
    
    # Track 1: Caliper (CALI)
    axes[0].plot(df['CALI'], df['DEPTH'], color='black', lw=0.5)
    axes[0].set_xlabel('CALI (inch)')          
    axes[0].set_xlim(0, 20)
    axes[0].xaxis.set_ticks_position("top")
    axes[0].xaxis.set_label_position("top")
    axes[0].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[0].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[0].minorticks_on()
    axes[0].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    axes[0].invert_yaxis()
    
    # Track 2: Gamma Ray (GR)
    axes[1].plot(df['GR'], df['DEPTH'], color='black', lw=0.2)
    axes[1].set_xlabel('GR (API)')
    axes[1].set_xlim(0, 150) 
    axes[1].xaxis.set_ticks_position("top")
    axes[1].xaxis.set_label_position("top")
    Cutoff = 75
    axes[1].fill_betweenx(df['DEPTH'], df['GR'], Cutoff, where=df['GR'] > Cutoff, interpolate=True, color='lightgreen', label='shales')
    axes[1].fill_betweenx(df['DEPTH'], df['GR'], Cutoff, where=df['GR'] < Cutoff, interpolate=True, color='yellow', label='sands')
    axes[1].axvline(Cutoff, color='k', linewidth=1, linestyle='--')
    axes[1].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[1].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[1].minorticks_on() 
    axes[1].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    
    # Track 3: Resistivity (ILD, LL8, MSFL)
    axes[2].plot(df['LLD'], df['DEPTH'], color='blue', lw=0.5)
    axes[2].set_xlabel('LLD (ohm.m)')
    axes[2].set_xlim(0.1, 1000)
    axes[2].xaxis.set_ticks_position("top")
    axes[2].xaxis.set_label_position("top")
    axes[2].set_xscale('log')
    axes[2].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[2].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[2].minorticks_on()
    axes[2].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    
    # Track 4: P-Wave (DT)
    axes[3].plot(df['DT'], df['DEPTH'], color='red', lw=0.5)
    axes[3].set_xlabel('DT (us/ft)')
    axes[3].set_xlim(30, 500)
    axes[3].xaxis.set_ticks_position("top")
    axes[3].xaxis.set_label_position("top")
    axes[3].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[3].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[3].minorticks_on() 
    axes[3].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    
    # Track 5: Neutron Porosity (NPHI) Density (RHOB)
    axes[4].plot(df['RHOB'], df['DEPTH'], color='red', lw=0.3)
    axes[4].set_xlabel('RHOB (g/cc)')
    axes[4].set_xlim(1.75, 2.75)
    axes[4].spines['top'].set_edgecolor('red')
    axes[4].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[4].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[4].minorticks_on() 
    axes[4].xaxis.set_minor_locator(MaxNLocator(nbins=10))

    ax2 = axes[4].twiny()  
    ax2.plot(df['NPHI'], df['DEPTH'], color='blue', label='NPHI', lw=0.3)
    ax2.invert_xaxis() 
    ax2.set_xlim(0.6, 0)
    axes[4].xaxis.set_ticks_position("top")
    axes[4].xaxis.set_label_position("top")
    ax2.spines["top"].set_position(("axes", 1.08))
    ax2.spines['top'].set_edgecolor('blue')
    ax2.set_xlabel('NPHI (v/v)')

    x = np.array(axes[4].get_xlim())
    z = np.array(ax2.get_xlim())

    nz=((df['NPHI']-np.max(z))/(np.min(z)-np.max(z)))*(np.max(x)-np.min(x))+np.min(x)

    axes[4].fill_betweenx(df['DEPTH'], df['RHOB'], nz, where=df['RHOB']>=nz, interpolate=True, color='green')
    axes[4].fill_betweenx(df['DEPTH'], df['RHOB'], nz, where=df['RHOB']<=nz, interpolate=True, color='yellow')

    plt.tight_layout()
    plt.show()

def plot_well_logs1(df):
    fig, axes = plt.subplots(nrows=1, ncols=8, figsize=(10, 10), sharey=True)
    
    # Track 1: Caliper (CALI)
    axes[0].plot(df['CALI'], df['DEPTH'], color='black', lw=0.5)
    axes[0].set_xlabel('CALI (inch)')          
    axes[0].set_xlim(0, 20)
    axes[0].xaxis.set_ticks_position("top")
    axes[0].xaxis.set_label_position("top")
    axes[0].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[0].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[0].minorticks_on()
    axes[0].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    axes[0].invert_yaxis()
    
    # Track 2: Gamma Ray (GR)
    axes[1].plot(df['GR'], df['DEPTH'], color='black', lw=0.2)
    axes[1].set_xlabel('GR (API)')
    axes[1].set_xlim(0, 150) 
    axes[1].xaxis.set_ticks_position("top")
    axes[1].xaxis.set_label_position("top")
    Cutoff = 75
    axes[1].fill_betweenx(df['DEPTH'], df['GR'], Cutoff, where=df['GR'] > Cutoff, interpolate=True, color='lightgreen', label='shales')
    axes[1].fill_betweenx(df['DEPTH'], df['GR'], Cutoff, where=df['GR'] < Cutoff, interpolate=True, color='yellow', label='sands')
    axes[1].axvline(Cutoff, color='k', linewidth=1, linestyle='--')
    axes[1].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[1].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[1].minorticks_on() 
    axes[1].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    
    # Track 3: Resistivity (ILD, LL8, MSFL)
    axes[2].plot(df['LLD'], df['DEPTH'], color='blue', lw=0.5)
    axes[2].set_xlabel('LLD (ohm.m)')
    axes[2].set_xlim(0.1, 1000)
    axes[2].xaxis.set_ticks_position("top")
    axes[2].xaxis.set_label_position("top")
    axes[2].set_xscale('log')
    axes[2].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[2].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[2].minorticks_on()
    axes[2].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    
    # Track 4: P-Wave (DT)
    axes[3].plot(df['DT'], df['DEPTH'], color='red', lw=0.5)
    axes[3].set_xlabel('DT (us/ft)')
    axes[3].set_xlim(30, 500)
    axes[3].xaxis.set_ticks_position("top")
    axes[3].xaxis.set_label_position("top")
    axes[3].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[3].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[3].minorticks_on() 
    axes[3].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    
    # Track 5: Neutron Porosity (NPHI) Density (RHOB)
    axes[4].plot(df['RHOB'], df['DEPTH'], color='red', lw=0.3)
    axes[4].set_xlabel('RHOB (g/cc)')
    axes[4].set_xlim(1.75, 2.75)
    axes[4].spines['top'].set_edgecolor('red')
    axes[4].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[4].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[4].minorticks_on() 
    axes[4].xaxis.set_minor_locator(MaxNLocator(nbins=10))

    ax2 = axes[4].twiny()  
    ax2.plot(df['NPHI'], df['DEPTH'], color='blue', label='NPHI', lw=0.3)
    ax2.invert_xaxis() 
    ax2.set_xlim(0.6, 0)
    axes[4].xaxis.set_ticks_position("top")
    axes[4].xaxis.set_label_position("top")
    ax2.spines["top"].set_position(("axes", 1.08))
    ax2.spines['top'].set_edgecolor('blue')
    ax2.set_xlabel('NPHI (v/v)')

    x = np.array(axes[4].get_xlim())
    z = np.array(ax2.get_xlim())

    nz=((df['NPHI']-np.max(z))/(np.min(z)-np.max(z)))*(np.max(x)-np.min(x))+np.min(x)

    axes[4].fill_betweenx(df['DEPTH'], df['RHOB'], nz, where=df['RHOB']>=nz, interpolate=True, color='green')
    axes[4].fill_betweenx(df['DEPTH'], df['RHOB'], nz, where=df['RHOB']<=nz, interpolate=True, color='yellow')

    # Track 6: P-Velociy (Vp)
    axes[5].plot(df['Vp'], df['DEPTH'], color='red', lw=0.5)
    axes[5].set_xlabel('Vp (m/s)')
    axes[5].set_xlim(4500, 29000)
    axes[5].xaxis.set_ticks_position("top")
    axes[5].xaxis.set_label_position("top")
    axes[5].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[5].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[5].minorticks_on() 
    axes[5].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    
    # Track 7: P-Velociy (Vp)
    axes[6].plot(df['AI'], df['DEPTH'], color='red', lw=0.5)
    axes[6].set_xlabel('AI (kg/(m²·s))')
    axes[6].set_xlim(6500, 65000)
    axes[6].xaxis.set_ticks_position("top")
    axes[6].xaxis.set_label_position("top")
    axes[6].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[6].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[6].minorticks_on() 
    axes[6].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    
    # Track 8: P-Velociy (Vp)
    axes[7].plot(df['RC'], df['DEPTH'], color='red', lw=0.5)
    axes[7].set_xlabel('Reff.Coefficient')
    axes[7].set_xlim(-1, 1)
    axes[7].xaxis.set_ticks_position("top")
    axes[7].xaxis.set_label_position("top")
    axes[7].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[7].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[7].minorticks_on() 
    axes[7].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    
    plt.tight_layout()
    plt.show()

def plot_well_logs2(df, df2):
    fig, axes = plt.subplots(nrows=1, ncols=8, figsize=(10, 10), sharey=True)
    
    # Track 1: Caliper (CALI)
    axes[0].plot(df['CALI'], df['DEPTH'], color='black', lw=0.5)
    axes[0].set_xlabel('CALI (inch)')          
    axes[0].set_xlim(0, 20)
    axes[0].xaxis.set_ticks_position("top")
    axes[0].xaxis.set_label_position("top")
    axes[0].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[0].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[0].minorticks_on()
    axes[0].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    axes[0].invert_yaxis()
    
    # Track 2: Gamma Ray (GR)
    axes[1].plot(df['GR'], df['DEPTH'], color='black', lw=0.2)
    axes[1].set_xlabel('GR (API)')
    axes[1].set_xlim(0, 150) 
    axes[1].xaxis.set_ticks_position("top")
    axes[1].xaxis.set_label_position("top")
    Cutoff = 75
    axes[1].fill_betweenx(df['DEPTH'], df['GR'], Cutoff, where=df['GR'] > Cutoff, interpolate=True, color='lightgreen', label='shales')
    axes[1].fill_betweenx(df['DEPTH'], df['GR'], Cutoff, where=df['GR'] < Cutoff, interpolate=True, color='yellow', label='sands')
    axes[1].axvline(Cutoff, color='k', linewidth=1, linestyle='--')
    axes[1].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[1].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[1].minorticks_on() 
    axes[1].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    
    # Track 3: Resistivity (ILD, LL8, MSFL)
    axes[2].plot(df['LLD'], df['DEPTH'], color='blue', lw=0.5)
    axes[2].set_xlabel('LLD (ohm.m)')
    axes[2].set_xlim(0.1, 1000)
    axes[2].xaxis.set_ticks_position("top")
    axes[2].xaxis.set_label_position("top")
    axes[2].set_xscale('log')
    axes[2].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[2].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[2].minorticks_on()
    axes[2].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    
    # Track 4: P-Wave (DT)
    axes[3].plot(df['DT'], df['DEPTH'], color='red', lw=0.5)
    axes[3].set_xlabel('DT (us/ft)')
    axes[3].set_xlim(30, 250)
    axes[3].xaxis.set_ticks_position("top")
    axes[3].xaxis.set_label_position("top")
    axes[3].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[3].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[3].minorticks_on() 
    axes[3].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    
    # Track 5: Neutron Porosity (NPHI) Density (RHOB)
    axes[4].plot(df['RHOB'], df['DEPTH'], color='red', lw=0.3)
    axes[4].set_xlabel('RHOB (g/cc)')
    axes[4].set_xlim(1.75, 2.75)
    axes[4].spines['top'].set_edgecolor('red')
    axes[4].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[4].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[4].minorticks_on() 
    axes[4].xaxis.set_minor_locator(MaxNLocator(nbins=10))

    ax2 = axes[4].twiny()  
    ax2.plot(df['NPHI'], df['DEPTH'], color='blue', label='NPHI', lw=0.3)
    ax2.invert_xaxis() 
    ax2.set_xlim(0.6, 0)
    axes[4].xaxis.set_ticks_position("top")
    axes[4].xaxis.set_label_position("top")
    ax2.spines["top"].set_position(("axes", 1.08))
    ax2.spines['top'].set_edgecolor('blue')
    ax2.set_xlabel('NPHI (v/v)')

    x = np.array(axes[4].get_xlim())
    z = np.array(ax2.get_xlim())

    nz=((df['NPHI']-np.max(z))/(np.min(z)-np.max(z)))*(np.max(x)-np.min(x))+np.min(x)

    axes[4].fill_betweenx(df['DEPTH'], df['RHOB'], nz, where=df['RHOB']>=nz, interpolate=True, color='green')
    axes[4].fill_betweenx(df['DEPTH'], df['RHOB'], nz, where=df['RHOB']<=nz, interpolate=True, color='yellow')

    # Track 6: P-Velociy (Vp)
    axes[5].plot(df['Vp'], df['DEPTH'], color='red', lw=0.5)
    axes[5].set_xlabel('Vp (m/s)')
    axes[5].set_xlim(4500, 29000)
    axes[5].xaxis.set_ticks_position("top")
    axes[5].xaxis.set_label_position("top")
    axes[5].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[5].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[5].minorticks_on() 
    axes[5].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    
    # Track 7: P-Velociy (Vp)
    axes[6].plot(df['AI'], df['DEPTH'], color='red', lw=0.5)
    axes[6].set_xlabel('AI (kg/(m²·s))')
    axes[6].set_xlim(6500, 65000)
    axes[6].xaxis.set_ticks_position("top")
    axes[6].xaxis.set_label_position("top")
    axes[6].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[6].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[6].minorticks_on() 
    axes[6].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    
    # Track 8: P-Velociy (Vp)
    axes[7].plot(df['RC'], df['DEPTH'], color='red', lw=0.5)
    axes[7].set_xlabel('Reff.Coefficient')
    axes[7].set_xlim(-1, 1)
    axes[7].xaxis.set_ticks_position("top")
    axes[7].xaxis.set_label_position("top")
    axes[7].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[7].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[7].minorticks_on() 
    axes[7].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    
    # Function to plot tops
    def plot_tops(ax):
        for _, row in df2.iterrows():
            ax.axhline(row['Top'], color='red', linestyle='--', linewidth=1)
            ax.text(ax.get_xlim()[0], row['Top'], row['Fm'], verticalalignment='bottom', color='black', fontsize=8)
            
    for i in range(0, 8):
        plot_tops(axes[i]) 
    
    plt.tight_layout()
    plt.show()


lithology_colour = {
    'Sandstone' : 'yellow',
    'Shale'     : 'green',
    'Carbonate' : 'skyblue',
    'Coal'      : 'black'
}

fluid_colour = {
    'Unknown': 'white',
    'Water': 'skyblue',
    'Gas': 'orange',
    'Oil': 'red'
}


def plot_well_logs3(df):
    fig, axes = plt.subplots(nrows=1, ncols=7, figsize=(10, 10), sharey=True)
    
    # Track 1: Caliper (CALI)
    axes[0].plot(df['CALI'], df['DEPTH'], color='black', lw=0.5)
    axes[0].set_xlabel('CALI (inch)')          
    axes[0].set_xlim(0, 20)
    axes[0].xaxis.set_ticks_position("top")
    axes[0].xaxis.set_label_position("top")
    axes[0].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[0].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[0].minorticks_on()
    axes[0].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    axes[0].invert_yaxis()
    
    # Track 2: Gamma Ray (GR)
    axes[1].plot(df['GR'], df['DEPTH'], color='black', lw=0.2)
    axes[1].set_xlabel('GR (API)')
    axes[1].set_xlim(0, 150) 
    axes[1].xaxis.set_ticks_position("top")
    axes[1].xaxis.set_label_position("top")
    Cutoff = 75
    axes[1].fill_betweenx(df['DEPTH'], df['GR'], Cutoff, where=df['GR'] > Cutoff, interpolate=True, color='lightgreen', label='shales')
    axes[1].fill_betweenx(df['DEPTH'], df['GR'], Cutoff, where=df['GR'] < Cutoff, interpolate=True, color='yellow', label='sands')
    axes[1].axvline(Cutoff, color='k', linewidth=1, linestyle='--')
    axes[1].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[1].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[1].minorticks_on() 
    axes[1].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    
    # Track 3: Resistivity (ILD, LL8, MSFL)
    axes[2].plot(df['LLD'], df['DEPTH'], color='blue', lw=0.5)
    axes[2].set_xlabel('LLD (ohm.m)')
    axes[2].set_xlim(0.1, 1000)
    axes[2].xaxis.set_ticks_position("top")
    axes[2].xaxis.set_label_position("top")
    axes[2].set_xscale('log')
    axes[2].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[2].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[2].minorticks_on()
    axes[2].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    
    # Track 4: P-Wave (DT)
    axes[3].plot(df['DT'], df['DEPTH'], color='red', lw=0.5)
    axes[3].set_xlabel('DT (us/ft)')
    axes[3].set_xlim(30, 500)
    axes[3].xaxis.set_ticks_position("top")
    axes[3].xaxis.set_label_position("top")
    axes[3].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[3].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[3].minorticks_on() 
    axes[3].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    
    # Track 5: Neutron Porosity (NPHI) Density (RHOB)
    axes[4].plot(df['RHOB'], df['DEPTH'], color='red', lw=0.3)
    axes[4].set_xlabel('RHOB (g/cc)')
    axes[4].set_xlim(1.75, 2.75)
    axes[4].spines['top'].set_edgecolor('red')
    axes[4].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[4].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[4].minorticks_on() 
    axes[4].xaxis.set_minor_locator(MaxNLocator(nbins=10))

    ax2 = axes[4].twiny()  
    ax2.plot(df['NPHI'], df['DEPTH'], color='blue', label='NPHI', lw=0.3)
    ax2.invert_xaxis() 
    ax2.set_xlim(0.6, 0)
    axes[4].xaxis.set_ticks_position("top")
    axes[4].xaxis.set_label_position("top")
    ax2.spines["top"].set_position(("axes", 1.08))
    ax2.spines['top'].set_edgecolor('blue')
    ax2.set_xlabel('NPHI (v/v)')

    x = np.array(axes[4].get_xlim())
    z = np.array(ax2.get_xlim())

    nz=((df['NPHI']-np.max(z))/(np.min(z)-np.max(z)))*(np.max(x)-np.min(x))+np.min(x)

    axes[4].fill_betweenx(df['DEPTH'], df['RHOB'], nz, where=df['RHOB']>=nz, interpolate=True, color='green')
    axes[4].fill_betweenx(df['DEPTH'], df['RHOB'], nz, where=df['RHOB']<=nz, interpolate=True, color='yellow')

    # Track 6: Lithology Track 
    axes[5].set_xlim(0, 1)  # Dummy x-axis
    for i in range(len(df)-1):
        litho = df.iloc[i]['Lithology']
        color_lith = lithology_colour.get(litho, 'black')  
        axes[5].fill_betweenx([df.iloc[i]['DEPTH'], df.iloc[i+1]['DEPTH']], 0, 1, color=color_lith)
    
    axes[5].set_xlabel('Lithology')
    axes[5].xaxis.set_label_position("top")
    axes[5].set_xticks([])
    
    # Track 7: Fluid Track
    axes[6].set_xlim(0, 1)  # Dummy x-axis
    for i in range(len(df)-1):
        fluid = df.iloc[i]['Fluid']
        color_fluid = fluid_colour.get(fluid, 'black')  
        axes[6].fill_betweenx([df.iloc[i]['DEPTH'], df.iloc[i+1]['DEPTH']], 0, 1, color=color_fluid)
    
    axes[6].set_xlabel('Fluid')
    axes[6].xaxis.set_label_position("top")
    axes[6].set_xticks([])

    plt.tight_layout()
    plt.show()


def plot_well_logs4(df, df2):
    fig, axes = plt.subplots(nrows=1, ncols=7, figsize=(10, 10), sharey=True)
    
    # Track 1: Caliper (CALI)
    axes[0].plot(df['CALI'], df['DEPTH'], color='black', lw=0.5)
    axes[0].set_xlabel('CALI (inch)')          
    axes[0].set_xlim(0, 20)
    axes[0].xaxis.set_ticks_position("top")
    axes[0].xaxis.set_label_position("top")
    axes[0].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[0].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[0].minorticks_on()
    axes[0].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    axes[0].invert_yaxis()
    
    # Track 2: Gamma Ray (GR)
    axes[1].plot(df['GR'], df['DEPTH'], color='black', lw=0.2)
    axes[1].set_xlabel('GR (API)')
    axes[1].set_xlim(0, 150) 
    axes[1].xaxis.set_ticks_position("top")
    axes[1].xaxis.set_label_position("top")
    Cutoff = 75
    axes[1].fill_betweenx(df['DEPTH'], df['GR'], Cutoff, where=df['GR'] > Cutoff, interpolate=True, color='lightgreen', label='shales')
    axes[1].fill_betweenx(df['DEPTH'], df['GR'], Cutoff, where=df['GR'] < Cutoff, interpolate=True, color='yellow', label='sands')
    axes[1].axvline(Cutoff, color='k', linewidth=1, linestyle='--')
    axes[1].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[1].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[1].minorticks_on() 
    axes[1].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    
    # Track 3: Resistivity (ILD, LL8, MSFL)
    axes[2].plot(df['LLD'], df['DEPTH'], color='blue', lw=0.5)
    axes[2].set_xlabel('LLD (ohm.m)')
    axes[2].set_xlim(0.1, 1000)
    axes[2].xaxis.set_ticks_position("top")
    axes[2].xaxis.set_label_position("top")
    axes[2].set_xscale('log')
    axes[2].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[2].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[2].minorticks_on()
    axes[2].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    
    # Track 4: P-Wave (DT)
    axes[3].plot(df['DT'], df['DEPTH'], color='red', lw=0.5)
    axes[3].set_xlabel('DT (us/ft)')
    axes[3].set_xlim(30, 500)
    axes[3].xaxis.set_ticks_position("top")
    axes[3].xaxis.set_label_position("top")
    axes[3].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[3].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[3].minorticks_on() 
    axes[3].xaxis.set_minor_locator(MaxNLocator(nbins=7))
    
    # Track 5: Neutron Porosity (NPHI) Density (RHOB)
    axes[4].plot(df['RHOB'], df['DEPTH'], color='red', lw=0.3)
    axes[4].set_xlabel('RHOB (g/cc)')
    axes[4].set_xlim(1.75, 2.75)
    axes[4].spines['top'].set_edgecolor('red')
    axes[4].grid(which='major', color='black', linestyle='-', linewidth=0.5)
    axes[4].grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
    axes[4].minorticks_on() 
    axes[4].xaxis.set_minor_locator(MaxNLocator(nbins=10))

    ax2 = axes[4].twiny()  
    ax2.plot(df['NPHI'], df['DEPTH'], color='blue', label='NPHI', lw=0.3)
    ax2.invert_xaxis() 
    ax2.set_xlim(0.6, 0)
    axes[4].xaxis.set_ticks_position("top")
    axes[4].xaxis.set_label_position("top")
    ax2.spines["top"].set_position(("axes", 1.08))
    ax2.spines['top'].set_edgecolor('blue')
    ax2.set_xlabel('NPHI (v/v)')

    x = np.array(axes[4].get_xlim())
    z = np.array(ax2.get_xlim())

    nz=((df['NPHI']-np.max(z))/(np.min(z)-np.max(z)))*(np.max(x)-np.min(x))+np.min(x)

    axes[4].fill_betweenx(df['DEPTH'], df['RHOB'], nz, where=df['RHOB']>=nz, interpolate=True, color='green')
    axes[4].fill_betweenx(df['DEPTH'], df['RHOB'], nz, where=df['RHOB']<=nz, interpolate=True, color='yellow')

    # Track 6: Lithology Track 
    axes[5].set_xlim(0, 1)  
    for i in range(len(df)-1):
        litho = df.iloc[i]['Lithology']
        color_lith = lithology_colour.get(litho, 'black')  
        axes[5].fill_betweenx([df.iloc[i]['DEPTH'], df.iloc[i+1]['DEPTH']], 0, 1, color=color_lith)
    
    axes[5].set_xlabel('Lithology')
    axes[5].xaxis.set_label_position("top")
    axes[5].set_xticks([])
    
    # Track 7: Fluid Track
    axes[6].set_xlim(0, 1) 
    for i in range(len(df)-1):
        fluid = df.iloc[i]['Fluid']
        color_fluid = fluid_colour.get(fluid, 'black')  
        axes[6].fill_betweenx([df.iloc[i]['DEPTH'], df.iloc[i+1]['DEPTH']], 0, 1, color=color_fluid)
    
    axes[6].set_xlabel('Fluid')
    axes[6].xaxis.set_label_position("top")
    axes[6].set_xticks([])

    # Function to plot tops
    def plot_tops(ax):
        for _, row in df2.iterrows():
            ax.axhline(row['Top'], color='red', linestyle='--', linewidth=1)
            ax.text(ax.get_xlim()[0], row['Top'], row['Fm'], verticalalignment='bottom', color='black', fontsize=8)
            
    for i in range(6, 7):
        plot_tops(axes[i]) 
        
    plt.tight_layout()
    plt.show()