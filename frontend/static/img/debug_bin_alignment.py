"""
Script de debug pour identifier le décalage de bins
"""
import numpy as np
import matplotlib.pyplot as plt
from mcnptoolspro import Mctal, MctalTally, Ptrac

# Charger MCTAL
m = Mctal(r'C:\Users\qduca\OneDrive\Applications\DECIMA_v2\data\mctal_samples\poly_spherical_Cf_50cm_f8bnk_10bars_7e8_seq.m')
t8 = m.GetTally(8)
tfc = MctalTally.TFC

e_bins = np.array(t8.GetEBins())
vals = np.array([
    t8.GetValue(tfc, tfc, tfc, tfc, tfc, tfc, i, tfc)
    for i in range(len(e_bins) - 1)
])

NPS = 700000000
vals = vals * NPS

# Charger PTRAC - CODE IDENTIQUE À test_LB6411
ptrac_path = r"C:\Users\qduca\OneDrive\Applications\DECIMA_v2\data\ptrac_samples\poly_spherical_Cf_50cm_f8bnk_10bars_7e8_seq.p"
p = Ptrac(ptrac_path, Ptrac.ASC_PTRAC)

deposited_energies = []
hists = p.ReadHistories(10000)
while hists:
    for h in hists:
        energy_sum = 0.0
        for e in range(h.GetNumEvents()):
            event = h.GetEvent(e)
            if event.Type() in (Ptrac.SRC, Ptrac.BNK):
                particle_type = event.Get(Ptrac.PARTICLE)
                if particle_type in (9, 32):
                    energy_init = event.Get(Ptrac.ENERGY)
                    for next_event_index in range(e + 1, h.GetNumEvents()):
                        next_event = h.GetEvent(next_event_index)
                        if next_event.Type() == Ptrac.TER:
                            energy_final = next_event.Get(Ptrac.ENERGY)
                            deposited_energy = energy_init - energy_final
                            energy_sum += deposited_energy
                            break
        deposited_energies.append(energy_sum)
    hists = p.ReadHistories(10000)

# Créer l'histogramme PTRAC
hist_ptrac, bin_edges = np.histogram(deposited_energies, bins=e_bins)

print(f'=== DEBUG BINS ===')
print(f'MCTAL: len(e_bins)={len(e_bins)}, len(vals)={len(vals)}')
print(f'PTRAC: len(hist_ptrac)={len(hist_ptrac)}, len(bin_edges)={len(bin_edges)}')
print(f'\nVérification: bin_edges == e_bins? {np.array_equal(bin_edges, e_bins)}')

# Trouver le premier bin non-nul
idx_mctal_first = np.where(vals > 0)[0][0]
idx_ptrac_first = np.where(hist_ptrac > 0)[0][0]

print(f'\nPremier bin non-nul:')
print(f'MCTAL: idx={idx_mctal_first}, bin=[{e_bins[idx_mctal_first]:.6f}, {e_bins[idx_mctal_first+1]:.6f}), val={vals[idx_mctal_first]:.3e}')
print(f'PTRAC: idx={idx_ptrac_first}, bin=[{e_bins[idx_ptrac_first]:.6f}, {e_bins[idx_ptrac_first+1]:.6f}), val={hist_ptrac[idx_ptrac_first]:.3e}')

# Tracer un zoom sur la région du premier pic
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Test différentes méthodes de tracé
x_centers = (e_bins[:-1] + e_bins[1:]) / 2

# Méthode 1: step with e_bins[:-1], where='post'
ax = axes[0, 0]
ax.step(e_bins[:-1], vals, where='post', color='blue', label='MCTAL', linewidth=2)
ax.step(e_bins[:-1], hist_ptrac, where='post', color='red', linestyle='--', label='PTRAC', linewidth=2)
ax.set_title('Méthode 1: step(e_bins[:-1], where=post)')
ax.set_yscale('log')
ax.set_xlim(0.15, 0.25)
ax.legend()
ax.grid(True, alpha=0.3)

# Méthode 2: bar chart (vérité terrain)
ax = axes[0, 1]
width = np.diff(e_bins)
ax.bar(e_bins[:-1], vals, width=width, alpha=0.5, color='blue', label='MCTAL', align='edge')
ax.bar(e_bins[:-1], hist_ptrac, width=width, alpha=0.5, color='red', label='PTRAC', align='edge')
ax.set_title('Méthode 2: bar(align=edge) - VÉRITÉ TERRAIN')
ax.set_yscale('log')
ax.set_xlim(0.15, 0.25)
ax.legend()
ax.grid(True, alpha=0.3)

# Méthode 3: step avec centres, where='mid'
ax = axes[1, 0]
ax.step(x_centers, vals, where='mid', color='blue', label='MCTAL', linewidth=2)
ax.step(x_centers, hist_ptrac, where='mid', color='red', linestyle='--', label='PTRAC', linewidth=2)
ax.set_title('Méthode 3: step(centers, where=mid)')
ax.set_yscale('log')
ax.set_xlim(0.15, 0.25)
ax.legend()
ax.grid(True, alpha=0.3)

# Méthode 4: Affichage des valeurs numériques
ax = axes[1, 1]
zoom_start = 45
zoom_end = 55
indices = np.arange(zoom_start, zoom_end)
ax.plot(indices, vals[zoom_start:zoom_end], 'o-', label='MCTAL', markersize=8)
ax.plot(indices, hist_ptrac[zoom_start:zoom_end], 's--', label='PTRAC', markersize=6)
ax.set_title(f'Méthode 4: Valeurs numériques (bins {zoom_start}-{zoom_end})')
ax.set_xlabel('Index de bin')
ax.set_ylabel('Counts')
ax.legend()
ax.grid(True, alpha=0.3)

# Afficher les bins correspondants
for i in range(zoom_start, min(zoom_start+5, zoom_end)):
    print(f'Bin {i}: [{e_bins[i]:.6f}, {e_bins[i+1]:.6f}), MCTAL={vals[i]:.3e}, PTRAC={hist_ptrac[i]:.3e}')

plt.tight_layout()
plt.savefig('debug_bin_alignment.png', dpi=150)
print('\nGraphique sauvegardé: debug_bin_alignment.png')
plt.show()
