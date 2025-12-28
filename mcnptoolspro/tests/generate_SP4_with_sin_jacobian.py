"""Generate SP4 values with INVERSE jacobian: SP4 = F(theta) * sin(theta) / 2
The hypothesis: MCNP samples cos(theta) uniformly in each bin, then weighs by SP4.
To get F(theta) as output, we need to include sin(theta) in SP4.

Theory:
- MCNP samples W = cos(theta) uniformly in each SI4 bin
- For uniform sampling in cos(theta), dN/d(cos theta) = constant
- But we MEASURE in theta space: dN/dtheta = dN/d(cos theta) * |d(cos theta)/dtheta|
- Since d(cos theta)/dtheta = -sin(theta), we have: dN/dtheta ∝ sin(theta)
- Therefore, to get F(theta) = N_ani(theta)/N_iso(theta), we need:
  SP4_ani ∝ F(theta) * sin(theta)
"""
import numpy as np

# Certificate F(theta) at bin edges (19 values)
cert_theta_edges = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90,
                             100, 110, 120, 130, 140, 150, 160, 170, 180])

# F(theta) values at these angles
cert_F_values = np.array([0.569, 0.691, 0.831, 0.909, 0.962, 0.993, 1.024, 1.028, 1.038, 1.036,
                          1.036, 1.037, 1.019, 1.008, 1.000, 0.978, 0.985, 0.990, 0.991])

# SI4 bins in cos(theta) (19 edges)
SI4_costheta_edges = np.array([
    -1.000, -0.985, -0.940, -0.866, -0.766, -0.643, -0.500, -0.342, -0.174, 0.000,
     0.174,  0.342,  0.500,  0.643,  0.766,  0.866,  0.940,  0.985,  1.000
])

# Convert to theta
SI4_theta_edges = np.degrees(np.arccos(SI4_costheta_edges))

# Bin centers for SI4 (18 bins)
SI4_costheta_centers = 0.5 * (SI4_costheta_edges[:-1] + SI4_costheta_edges[1:])
SI4_theta_centers = np.degrees(np.arccos(SI4_costheta_centers))

print("="*80)
print("SP4 CALCULATION WITH SINE JACOBIAN: SP4 = F(theta) * sin(theta) / 2")
print("="*80)
print("\nTheoretical basis:")
print("  MCNP samples cos(theta) uniformly in each bin")
print("  Jacobian: dN/dtheta = dN/d(cos theta) * sin(theta)")
print("  To get F(theta) in theta space, we need: SP4 proportional to F(theta) * sin(theta)")
print("="*80)

# For each SI4 bin center, interpolate F(theta) from certificate
F_at_SI4_bins = np.interp(SI4_theta_centers, cert_theta_edges, cert_F_values)

# Calculate sin(theta) at bin centers
sin_theta_at_bins = np.sin(np.radians(SI4_theta_centers))

# Calculate SP4_raw = F(theta) * sin(theta) / 2
# The /2 comes from isotropic: p_iso(theta) = sin(theta)/2
SP4_raw = F_at_SI4_bins * sin_theta_at_bins / 2.0

# Normalize so integral over cos(theta) from -1 to 1 equals 1
delta_costheta = np.diff(SI4_costheta_edges)
integral = np.sum(SP4_raw * delta_costheta)
SP4_normalized = SP4_raw / integral

print(f"\nIntegral check (should be 1.0): {np.sum(SP4_normalized * delta_costheta):.6f}")
print(f"Number of SP4 values: {len(SP4_normalized)}")

# Print SP4 card
print("\n" + "="*80)
print("MCNP SDEF CARD - SP4 WITH SINE JACOBIAN")
print("="*80)
print("\nSI4 H  -1.000 -0.985 -0.940 -0.866 -0.766 -0.643 -0.500 -0.342 -0.174 0.000 &")
print("         0.174  0.342  0.500  0.643  0.766  0.866  0.940  0.985  1.000")
print("\nSP4 D   0  ", end="")
for i, val in enumerate(SP4_normalized):
    print(f"{val:.4f} ", end="")
    if (i+1) % 5 == 0 and i < len(SP4_normalized)-1:
        print("&\n           ", end="")
print()

# Verification table
print("\n" + "="*80)
print("VERIFICATION TABLE")
print("="*80)
print(f"{'Bin':<4} {'theta_center':<12} {'cos(th) range':<22} {'F(th)':<8} {'sin(th)':<10} {'SP4 raw':<10} {'SP4 norm':<10}")
print("-"*90)

for i in range(len(SP4_normalized)):
    theta_c = SI4_theta_centers[i]
    costh_low = SI4_costheta_edges[i]
    costh_high = SI4_costheta_edges[i+1]
    F_val = F_at_SI4_bins[i]
    sin_val = sin_theta_at_bins[i]
    sp4_raw = SP4_raw[i]
    sp4_norm = SP4_normalized[i]

    print(f"{i+1:<4} {theta_c:>6.1f} deg   [{costh_low:>6.3f}, {costh_high:>6.3f}]   {F_val:<8.3f} {sin_val:<10.4f} {sp4_raw:<10.4f} {sp4_norm:<10.4f}")

# Expected behavior check
print("\n" + "="*80)
print("EXPECTED BEHAVIOR:")
print("="*80)
print("With sin(theta) jacobian:")
print("  - SP4 should be HIGH at center (theta~90, F~1.04, sin~1.0)")
print("  - SP4 should be LOW at extremities (theta~0/180, F~0.6-1.0, sin~0)")
print("")
print("Check SP4 values:")
print(f"  SP4 at theta=5deg (bin 18):   {SP4_normalized[-1]:.4f} (should be SMALL)")
print(f"  SP4 at theta=85deg (bin 10):  {SP4_normalized[9]:.4f} (should be LARGE)")
print(f"  SP4 at theta=95deg (bin 9):   {SP4_normalized[8]:.4f} (should be LARGE)")
print(f"  SP4 at theta=175deg (bin 1):  {SP4_normalized[0]:.4f} (should be SMALL)")
print("="*80)

# Save to file for easy copy-paste
output_file = "SP4_with_sin_jacobian.txt"
with open(output_file, 'w') as f:
    f.write("C Angular distribution - WITH sin(theta) jacobian\n")
    f.write("C Theory: SP4 = F(theta) * sin(theta) / 2, normalized\n")
    f.write("C This accounts for MCNP sampling cos(theta) uniformly in each bin\n")
    f.write("SI4 H  -1.000 -0.985 -0.940 -0.866 -0.766 -0.643 -0.500 -0.342 -0.174 0.000 &\n")
    f.write("         0.174  0.342  0.500  0.643  0.766  0.866  0.940  0.985  1.000\n")
    f.write("SP4 D   0  ")
    for i, val in enumerate(SP4_normalized):
        f.write(f"{val:.4f} ")
        if (i+1) % 5 == 0 and i < len(SP4_normalized)-1:
            f.write("&\n           ")
    f.write("\n")

print(f"\n[SAVED] SDEF card saved to: {output_file}")

# Compare with previous attempt (without sin jacobian)
SP4_previous = np.array([
    0.4952, 0.4936, 0.4907, 0.4949, 0.5021, 0.5069, 0.5142, 0.5183, 0.5181, 0.5186,
    0.5166, 0.5131, 0.5045, 0.4891, 0.4686, 0.4368, 0.3857, 0.3274
])

print("\n" + "="*80)
print("COMPARISON: NEW (with sin) vs PREVIOUS (without sin)")
print("="*80)
print(f"{'Bin':<4} {'theta':<8} {'Previous':<12} {'New (sin)':<12} {'Ratio new/prev':<15}")
print("-"*60)
for i in range(len(SP4_normalized)):
    theta_c = SI4_theta_centers[i]
    prev_val = SP4_previous[i]
    new_val = SP4_normalized[i]
    ratio = new_val / prev_val if prev_val > 0 else 0

    print(f"{i+1:<4} {theta_c:>6.1f}  {prev_val:<12.4f} {new_val:<12.4f} {ratio:<15.3f}")

print("\n" + "="*80)
print("KEY INSIGHT:")
print("  Previous (no sin): SP4 values were ~0.50 at center, ~0.33 at extremities")
print("  New (with sin):    SP4 values should be HIGHER at center, LOWER at extremities")
print("  This is because sin(theta) amplifies the difference!")
print("="*80)
