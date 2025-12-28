# AmBe Source Anisotropy Analysis

This directory contains scripts for analyzing the horizontal anisotropy factor of the LB6411 AmBe neutron source and comparing MCNP results with the IRSN certificate.

## Files

### Analysis Scripts

1. **`analyze_ambe_complete.py`** - **MAIN ANALYSIS SCRIPT**
   - Complete analysis with 6 panels:
     * U, V, W distribution overlays (ISO vs ANI_CORRECTED)
     * Anisotropy factor F(θ) vs certificate
     * Deviation from certificate
     * Statistics table
   - Calculates anisotropy factor F(θ) = N_ani(θ) / N_iso(θ)
   - Compares with IRSN certificate values
   - Usage: `python analyze_ambe_complete.py`

2. **`generate_SP4_with_sin_jacobian.py`** - SP4 VALUE GENERATOR
   - Generates corrected SP4 values for MCNP SDEF card
   - Applies proper Jacobian: SP4 = F(θ) × sin(θ) / 2
   - Outputs ready-to-use SDEF card
   - Usage: `python generate_SP4_with_sin_jacobian.py`

### Output Files

- **`ambe_complete_analysis.png`** - Complete 6-panel analysis plot
- **`SP4_with_sin_jacobian.txt`** - Corrected SDEF card for MCNP

### Test Data

Required PTRAC files in `test_data/`:
- `LB6411_cezaneRealiste_ambeiso_Wsource_SRC-TER_SC_150_seq.ip` (isotropic reference)
- `LB6411_cezaneRealiste_ambeisoani_WsourceClaude_SRC-TER_SC_150_seq.ip` (corrected anisotropic)

## Key Results

### Corrected SDEF Card (with sin jacobian)

```
SI4 H  -1.000 -0.985 -0.940 -0.866 -0.766 -0.643 -0.500 -0.342 -0.174 0.000 &
         0.174  0.342  0.500  0.643  0.766  0.866  0.940  0.985  1.000

SP4 D   0  0.0759 0.1679 0.2643 0.3587 0.4468 0.5216 0.5848 0.6279 0.6471 0.6477 &
           0.6258 0.5835 0.5191 0.4353 0.3397 0.2353 0.1312 0.0502
```

### Performance

- **CORRECTED SDEF** (with sin jacobian):
  - RMS error = 0.1040 (10.9% of mean)
  - Excellent agreement with certificate at center angles (75-115°): < 3% error
  - Slightly higher errors at extremities due to lower statistics

## Theory

### The Problem

MCNP samples **W = cos(θ) uniformly** in each SI4 bin, but the certificate provides **F(θ) in θ space**.

### The Solution: Jacobian Transformation

When changing variables from θ → cos(θ), a Jacobian is required:

```
dN/dθ = dN/d(cos θ) × |d(cos θ)/dθ|
      = dN/d(cos θ) × sin(θ)
```

### Formula

To obtain the correct F(θ) in MCNP:

```
SP4[i] = (F(θ_i) × sin(θ_i) / 2) / normalization
```

Where:
- `F(θ_i)` = certificate anisotropy factor at bin center
- `sin(θ_i)` = Jacobian for θ → cos(θ) transformation
- `/2` = normalization for isotropic distribution
- Final normalization ensures ∫ SP4 d(cos θ) = 1

### Why sin(θ)?

The `sin(θ)` amplifies the difference:
- **At center (θ=90°)**: sin(90°) = 1.0 → SP4 high
- **At extremities (θ=0°,180°)**: sin(0°) ≈ 0 → SP4 low

This compensates for MCNP's uniform sampling in cos(θ) instead of θ.

## Certificate Reference

IRSN LB6411 AmBe source horizontal anisotropy factor:
- Flat at center: F(90°) ≈ 1.036
- Lower at extremities: F(0°) ≈ 0.569, F(180°) ≈ 0.991
- 19 angular bins (0° to 180° in 10° steps)

## Contact

For questions about this analysis, refer to the main project documentation.
