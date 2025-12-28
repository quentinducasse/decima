"""
COMPLETE AmBe ANISOTROPY ANALYSIS
- W distribution overlays (ISO vs ANI_CORRECTED)
- Anisotropy factor F(theta) comparison with certificate
- Detailed statistical analysis

Usage: python analyze_ambe_complete.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'python'))

import mcnptoolspro as m
import matplotlib.pyplot as plt
import numpy as np

# ============================================================================
# CONFIGURATION
# ============================================================================

# MCNP Event types
EVENT_TYPE_SRC = 1000
EVENT_TYPE_BNK = 2000
EVENT_TYPE_SUR = 3000
EVENT_TYPE_COL = 4000
EVENT_TYPE_TER = 5000

# Safety limits
MAX_BATCHES = 10000
MAX_HISTORIES = 1000000

# PTRAC files to compare
PTRAC_FILES = [
    ('ISO', str(Path(__file__).parent / 'test_data' / 'LB6411_cezaneRealiste_ambeiso_Wsource_SRC-TER_SC_150_seq.ip')),
    ('ANI_CORRECTED', str(Path(__file__).parent / 'test_data' / 'LB6411_cezaneRealiste_ambeisoani_WsourceClaude_SRC-TER_SC_150_seq.ip')),
]

# Certificate data (IRSN LB6411 horizontal anisotropy factor)
CERT_THETA = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90,
                       100, 110, 120, 130, 140, 150, 160, 170, 180])
CERT_F = np.array([0.569, 0.691, 0.831, 0.909, 0.962, 0.993, 1.024, 1.028, 1.038, 1.036,
                   1.036, 1.037, 1.019, 1.008, 1.000, 0.978, 0.985, 0.990, 0.991])
CERT_UNC = np.array([0.005, 0.006, 0.007, 0.007, 0.008, 0.008, 0.008, 0.008, 0.008, 0.008,
                     0.008, 0.008, 0.008, 0.008, 0.008, 0.008, 0.008, 0.008, 0.008])

# Binning
THETA_BINS = np.arange(0, 181, 10)
BIN_CENTERS = THETA_BINS[:-1] + 5

# Custom W bins (from SI4)
W_BINS = np.array([
    -1.000, -0.985, -0.940, -0.866, -0.766, -0.643, -0.500, -0.342, -0.174, 0.000,
     0.174,  0.342,  0.500,  0.643,  0.766,  0.866,  0.940,  0.985,  1.000
])

# ============================================================================
# DATA PROCESSING
# ============================================================================

def read_ptrac_uvw(ptrac_path, max_batches=MAX_BATCHES, max_histories=MAX_HISTORIES):
    """Read U, V, W direction cosines from PTRAC file (SOURCE events only)"""
    print(f"Reading: {ptrac_path}")

    if not Path(ptrac_path).exists():
        print(f"  [ERROR] File does not exist!")
        return {'u': [], 'v': [], 'w': []}

    p = m.Ptrac(ptrac_path, m.Ptrac.ASC_PTRAC)
    u_values, v_values, w_values = [], [], []
    total_histories = 0
    batch_num = 0

    hists = p.ReadHistories(100)
    while hists and batch_num < max_batches and total_histories < max_histories:
        batch_num += 1
        for h in hists:
            total_histories += 1
            for e in range(h.GetNumEvents()):
                event = h.GetEvent(e)
                if event.Type() == EVENT_TYPE_SRC:
                    if event.Has(m.Ptrac.U):
                        u_values.append(event.Get(m.Ptrac.U))
                    if event.Has(m.Ptrac.V):
                        v_values.append(event.Get(m.Ptrac.V))
                    if event.Has(m.Ptrac.W):
                        w_values.append(event.Get(m.Ptrac.W))

        if batch_num % 100 == 0:
            print(f"  Batch {batch_num}: {total_histories} histories, {len(w_values)} SOURCE events")

        if total_histories < max_histories:
            hists = p.ReadHistories(100)
        else:
            break

    print(f"  TOTAL: {len(w_values)} SOURCE particles")
    return {
        'u': np.array(u_values),
        'v': np.array(v_values),
        'w': np.array(w_values)
    }

# ============================================================================
# MAIN ANALYSIS
# ============================================================================

print("="*80)
print("COMPLETE AmBe SOURCE ANISOTROPY ANALYSIS")
print("="*80)

# Read all files
results = {}
for name, ptrac_path in PTRAC_FILES:
    print(f"\n{'='*80}")
    print(f"Processing: {name}")
    print('='*80)
    uvw = read_ptrac_uvw(ptrac_path)

    if len(uvw['w']) > 0:
        theta_values = np.degrees(np.arccos(np.clip(uvw['w'], -1, 1)))
        counts_theta, _ = np.histogram(theta_values, bins=THETA_BINS)
        results[name] = {
            'u': uvw['u'],
            'v': uvw['v'],
            'w': uvw['w'],
            'theta': theta_values,
            'counts_theta': counts_theta,
            'n_events': len(uvw['w'])
        }

# Calculate anisotropy factor with proper normalization
n_iso = results['ISO']['n_events']
n_corrected = results['ANI_CORRECTED']['n_events']

print(f"\n{'='*80}")
print("EVENT COUNTS")
print('='*80)
print(f"  ISO events:       {n_iso:,}")
print(f"  CORRECTED events: {n_corrected:,}")
print(f"  Ratio:            {n_corrected/n_iso:.2f}x")

# Normalize counts by total events to get probability distributions
counts_iso = results['ISO']['counts_theta']
counts_corrected = results['ANI_CORRECTED']['counts_theta']

# Normalize to probability (density per bin)
prob_iso = counts_iso / n_iso
prob_corrected = counts_corrected / n_corrected

# Calculate anisotropy factor F(theta) = P_ani(theta) / P_iso(theta)
F_corrected = np.divide(prob_corrected, prob_iso,
                        out=np.ones_like(prob_iso, dtype=float), where=prob_iso > 0)

# Normalize to mean = 1 for comparison with certificate
mean_F_corrected = np.mean(F_corrected)
F_corrected_norm = F_corrected / mean_F_corrected

print(f"\n{'='*80}")
print("ANISOTROPY FACTOR RESULTS")
print('='*80)
print(f"\nCORRECTED SDEF (with sin jacobian):")
print(f"  Mean F (raw):        {mean_F_corrected:.4f}")
print(f"  Mean F (normalized): 1.0000 (by definition)")
print(f"  Range (normalized):  [{np.min(F_corrected_norm):.3f}, {np.max(F_corrected_norm):.3f}]")

# ============================================================================
# PLOTTING: 6 PANELS (3 rows x 3 cols)
# ============================================================================

fig = plt.figure(figsize=(18, 16))
gs = fig.add_gridspec(4, 3, hspace=0.35, wspace=0.3)

# ============ ROW 1: U, V, W OVERLAYS - RAW FREQUENCY ============
colors_overlay = {'ISO': 'blue', 'ANI_CORRECTED': 'orange'}
directions = [('U', 'X-axis'), ('V', 'Y-axis'), ('W', 'Z-axis')]

for idx, (dir_key, dir_name) in enumerate(directions):
    ax = fig.add_subplot(gs[0, idx])

    for file_name in ['ISO', 'ANI_CORRECTED']:
        if file_name in results:
            values = results[file_name][dir_key.lower()]
            n_events = results[file_name]['n_events']
            if len(values) > 0:
                # Normalized frequency (probability per bin, not per unit)
                counts, bins = np.histogram(values, bins=W_BINS)
                prob = counts / n_events

                # Use bar chart for cleaner visualization
                bin_centers = 0.5 * (bins[:-1] + bins[1:])
                bin_widths = np.diff(bins)
                ax.bar(bin_centers, prob, width=bin_widths, alpha=0.5,
                       color=colors_overlay[file_name], edgecolor=colors_overlay[file_name],
                       linewidth=1.5, label=f'{file_name} (n={n_events:,})')

                mean_val = np.mean(values)
                ax.axvline(mean_val, color=colors_overlay[file_name], linestyle='--',
                          linewidth=2, alpha=0.8)

    ax.set_title(f'{dir_key} Distribution - Normalized Frequency\n({dir_name} Direction Cosine)',
                fontsize=10, fontweight='bold')
    ax.set_xlabel(f'{dir_key}', fontsize=9)
    ax.set_ylabel('Probability per bin', fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=7)
    ax.set_xlim(-1.05, 1.05)

# ============ ROW 2: U, V, W OVERLAYS - NORMALIZED DENSITY ============
for idx, (dir_key, dir_name) in enumerate(directions):
    ax = fig.add_subplot(gs[1, idx])

    for file_name in ['ISO', 'ANI_CORRECTED']:
        if file_name in results:
            values = results[file_name][dir_key.lower()]
            n_events = results[file_name]['n_events']
            if len(values) > 0:
                # Normalized density for proper comparison
                ax.hist(values, bins=W_BINS, alpha=0.7, color=colors_overlay[file_name],
                       edgecolor=colors_overlay[file_name], linewidth=2, histtype='step',
                       label=f'{file_name} (n={n_events:,})', fill=False, density=True)

                mean_val = np.mean(values)
                ax.axvline(mean_val, color=colors_overlay[file_name], linestyle='--',
                          linewidth=2, alpha=0.8)

    ax.set_title(f'{dir_key} Distribution - Normalized\n({dir_name} Direction Cosine)',
                fontsize=10, fontweight='bold')
    ax.set_xlabel(f'{dir_key}', fontsize=9)
    ax.set_ylabel('Probability Density', fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=7)
    ax.set_xlim(-1.05, 1.05)

# ============ ROW 3: F(theta) NORMALIZED COMPARISON (left 2 cols) ============
ax = fig.add_subplot(gs[2, :2])

ax.errorbar(CERT_THETA, CERT_F, yerr=CERT_UNC,
           fmt='s', color='black', markersize=5, capsize=3,
           label='Certificate (IRSN)', linewidth=1.5, alpha=0.8)
ax.plot(BIN_CENTERS, F_corrected_norm, 'o-', color='green', markersize=5,
       linewidth=2, label='MCNP (Corrected)', alpha=0.7)
ax.axhline(1.0, color='gray', linestyle='--', linewidth=1, alpha=0.5)
ax.set_title('Anisotropy Factor F(theta) - Normalized Comparison',
            fontsize=11, fontweight='bold')
ax.set_xlabel('Angle (degrees)', fontsize=10)
ax.set_ylabel('F(theta) normalized', fontsize=10)
ax.grid(True, alpha=0.3)
ax.legend(fontsize=9)
ax.set_xlim(-5, 185)
ax.set_ylim(0.4, 1.4)

# ============ ROW 3: DEVIATION FROM CERTIFICATE (right col) ============
ax = fig.add_subplot(gs[2, 2])

cert_F_at_bins = np.array([CERT_F[np.argmin(np.abs(CERT_THETA - bc))] for bc in BIN_CENTERS])
diff_corrected = F_corrected_norm - cert_F_at_bins

ax.plot(BIN_CENTERS, diff_corrected, 'o-', color='green', markersize=5,
       linewidth=2, label='MCNP - Certificate', alpha=0.7)
ax.axhline(0.0, color='black', linestyle='-', linewidth=1.5, alpha=0.8)
ax.axhline(0.05, color='gray', linestyle=':', linewidth=1, alpha=0.5)
ax.axhline(-0.05, color='gray', linestyle=':', linewidth=1, alpha=0.5)
ax.set_title('Deviation from Certificate', fontsize=11, fontweight='bold')
ax.set_xlabel('Angle (degrees)', fontsize=10)
ax.set_ylabel('Delta F(theta)', fontsize=10)
ax.grid(True, alpha=0.3)
ax.legend(fontsize=9)
ax.set_xlim(-5, 185)

# ============ ROW 4: STATISTICS TABLE (full width) ============
ax = fig.add_subplot(gs[3, :])
ax.axis('off')

# Create statistics table
table_data = []
table_data.append(['Direction', 'File', 'Mean', 'Std Dev', 'Min', 'Max'])
table_data.append(['-'*10, '-'*15, '-'*8, '-'*8, '-'*8, '-'*8])

for dir_key, dir_name in directions:
    for file_name in ['ISO', 'ANI_CORRECTED']:
        if file_name in results:
            values = results[file_name][dir_key.lower()]
            if len(values) > 0:
                table_data.append([
                    dir_key,
                    file_name,
                    f"{np.mean(values):.4f}",
                    f"{np.std(values):.4f}",
                    f"{np.min(values):.4f}",
                    f"{np.max(values):.4f}"
                ])

table = ax.table(cellText=table_data, cellLoc='center', loc='center',
                colWidths=[0.12, 0.20, 0.12, 0.12, 0.12, 0.12])
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1, 2)

# Style header row
for i in range(6):
    table[(0, i)].set_facecolor('#4CAF50')
    table[(0, i)].set_text_props(weight='bold', color='white')

output_path = Path(__file__).parent / 'ambe_complete_analysis.png'
plt.savefig(output_path, dpi=150, bbox_inches='tight')
print(f"\n[SAVED] Complete analysis plot: {output_path}")
plt.show()

# ============================================================================
# DETAILED RESULTS
# ============================================================================

print(f"\n{'='*80}")
print("DETAILED COMPARISON TABLE")
print('='*80)
print(f"{'Angle':<8} {'Certificate':<12} {'MCNP':<12} {'Difference':<12} {'% Error':<10}")
print("-" * 60)

for i, theta in enumerate(BIN_CENTERS):
    idx_cert = np.argmin(np.abs(CERT_THETA - theta))
    cert_val = CERT_F[idx_cert]
    mcnp_val = F_corrected_norm[i]
    diff = mcnp_val - cert_val
    pct_error = (diff / cert_val) * 100 if cert_val > 0 else 0

    print(f"{theta:<8.0f} {cert_val:<12.3f} {mcnp_val:<12.3f} {diff:+12.3f} {pct_error:+10.2f}%")

# RMS difference
rms_corrected = np.sqrt(np.mean((F_corrected_norm - cert_F_at_bins)**2))

print('='*80)
print(f"\nRMS DIFFERENCE FROM CERTIFICATE:")
print(f"  RMS Error: {rms_corrected:.4f} ({(rms_corrected/np.mean(CERT_F)*100):.1f}% of mean)")
print('='*80)

print("\n[SUCCESS] Complete analysis finished!")
