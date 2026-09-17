# ⚡ [QUANT-SOURCE-214] Consolidated Quant & Algo Trading Repositories
**Category**: `HFT_MICROSTRUCTURE_LOB` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_214_HFT_MICROSTRUCTURE_LOB.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: LOB-Latent-Regimes (`PHASE4-QUANT-127`)
- **Full Name**: `PHASE4-QUANT-127_prakulhiremath__LOB-Latent-Regimes`
- **Description**: Identification and early detection of unobserved microstructure states in High-Frequency Limit Order Books using semi-parametric state-space models. Includes proofs of identifiability and lead-lag empirical analysis.
- **GitHub Stars**: 17
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
<div align="center">

<br/>

```
                    ╔══════════════════════════════════════════════════════════════════╗
                    ║   LATENT MICRO-REGIME EARLY DETECTION IN LIMIT ORDER BOOKS       ║
                    ║   Identifying structural market instability before it surfaces   ║
                    ╚══════════════════════════════════════════════════════════════════╝
```
[![arXiv](https://img.shields.io/badge/arXiv-2604.20949-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2604.20949)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19697687.svg?sanitize=true)](https://doi.org/10.5281/zenodo.19697687)
![Method](https://img.shields.io/badge/Method-Trigger%20Based-0078D4?style=flat-square)
![Model](https://img.shields.io/badge/Model-HMM-8A2BE2?style=flat-square)
![Precision](https://img.shields.io/badge/Precision-100%25%20(eval)-D4AF37?style=flat-square)
![Lead-Time](https://img.shields.io/badge/Lead--Time-Positive-28A745?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)


<img src="assets/detection.gif" width="860" alt="Detection Timeline — Latent regime transitions identified before observable stress"/>

<br/>

</div>

---

## The Core Idea

> **Market stress does not arrive without warning. It *accumulates*.**

Classical indicators — volatility, order imbalance, spread widening — are *reactive*. By the time they fire, the dislocation has already begun.

This research asks a harder question:

> *Can we detect the structural deterioration that **precedes** observable stress — before it becomes visible in price or spread?*

The answer is yes. We call it the **Latent Build-up Phase**.

---

## What "Latent" Means Here

The market moves through three regimes. The critical one is invisible to standard monitors:

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   STATE 0 ──────────────►  STATE 1 ──────────────►  STATE 2     │
│                                                                 │
│   Stable                   Latent Build-up          Stress      │
│   ─────────                ───────────────          ──────      │
│   Balanced liquidity       Depth eroding            Price shock │
│   High resilience          Spread drifting          Visible     │
│   Equilibrium              ⚠ Hidden instability     Reactive    │
│                                                                 │
│                            ◄────── detection window ──────►     │
│                            ↑                         ↑          │
│                        our signal fires          stress begins  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**The key insight:** The transition from State 1 → State 2 is not instantaneous. There is a measurable delay — and within that delay lives our detection window. We exploit it.

---

## Detection Framework

Three independent signal channels. One fused trigger.

### Signal Channels

| Channel | What It Measures | Why It's Early |
|---|---|---|
| **HMM Posterior Entropy** | Uncertainty in regime classification | Rises as the latent state becomes ambiguous, before the transition |
| **Temporal Depth Drift** | Recursive tracking of LOB depth erosion | Captures slow structural decay invisible to snapshot metrics |
| **Order Flow Toxicity** | Imbalance between informed and uninformed flow | Signals adverse selection building in the book |

### Trigger Logic

```
MAX-Fusion Trigger
├── Rising-edge detection (onset of change, not absolute level)
├── Cross-channel aggregation (fire when any channel breaches threshold)
└── Early-detection constraint τ < σ (signal must precede stress)
```

**Rising-edge detection** is the key design choice. We don't ask "is the spread wide?" We ask "is it *getting* wider *right now*?" This bypasses the noise floor that kills absolute-threshold methods.

---

## Results

```
╔════════════════════════════════════════════════════════════════╗
║  METHOD              LEAD-TIME     PRECISION    COVERAGE       ║
╠════════════════════════════════════════════════════════════════╣
║  ★ Adaptive Trigger  +18.6 steps   100%         52.6%          ║
║    HMM               +14.9 steps   100%         43.2%          ║
║    Multi-Trigger     +13.1 steps   100%         28.1%          ║
╠════════════════════════════════════════════════════════════════╣
║  ✗ Order Imbalance   −24.8 steps    54.9%        78.7%         ║
║  ✗ Volatility        −32.0 steps    45.5%        43.3%         ║
╚════════════════════════════════════════════════════════════════╝
```

**Reading the table:**
- **Positive lead-time** means the signal fires *before* stress begins. Baselines are strictly negative — they lag.
- **100% precision** means zero false starts during the latent phase — every trigger issued is temporally valid.
- **Coverage** reflects selectivity: we fire only when we're certain. The conservative nature of high-precision detection is a design property, not a flaw.

> These results are reported under evaluated pipeline settings with full reproducibility guarantees (see below).

---

## Empirical Findings

**1. Latent instability exists and is measurable.**
Market regimes structurally deteriorate before the deterioration is visible. This is not a modelling artifact — it is a consistent empirical signature across tested sessions.

**2. Depth erosion is the most reliable early signal.**
Depth decay in the LOB precedes spread widening and price impact. If the book is thinning quietly, something is coming.

**3. HMM posterior entropy is a structural stress barometer.**
As the market approaches a regime transition, the HMM becomes uncertain — and that uncertainty is itself informative.

**4. Rising-edge detection outperforms threshold detection.**
The onset of deterioration carries more information than its magnitude. Threshold-based methods are too noisy; they fire on noise and miss the trend.

**5. Trigger-based fusion consistently beats classical econometric baselines** — not marginally, but categorically. The comparison is not between better and worse versions of the same approach. It is between a predictive framework and a reactive one.

---

## Repository Structure

```
LOB-Latent-Regimes/
│
├── experiments/
│   ├── v1_baseline.py            # Initial HMM formulation
│   ├── v2_entropy.py             # Posterior entropy tracking
│   ├── v3_depth_drift.py         # Temporal depth signal
│   ├── v4_triggers.py            # Trigger logic development
│   ├── v5_fusion.py              # MAX-fusion framework
│   ├── v6_rising_edge.py         # Rising-edge detection
│   └── v7_final.py               # ★ Production pipeline
│
├── notebooks/
│   └── analysis.ipynb            # Experiment analysis + figures
│
├── results/
│   ├── figures/                  # High-resolution performance plots
│   └── summary.txt               # Quantified results
│
├── paper/                        # Technical manuscript
├── assets/                       # Visualizations, GIFs
└── README.md
```

---

## Reproducibility Guarantees

This pipeline was built to be trusted.

```
✓  Fully causal — no lookahead bias at any stage
✓  Rolling normalization only — no global statistics that leak future data  
✓  HMM re-fit periodically — no leakage across the evaluation window
✓  Deterministic seeds — results are exact across runs
✓  Validated on Google Colab (NVIDIA T4) and Apple Silicon (M4 Pro/Max)
```

---

## Quick Start

```bash
# Clone
git clone https://github.com/prakulhiremath/LOB-Latent-Regimes.git
cd LOB-Latent-Regimes

# Install
pip install -r requirements.txt

# Run the final pipeline
python experiments/v7_final.py
```

---

## Scope & Limitations

Be precise about what this is.

| This repo **is** | This repo **is not** |
|---|---|
| A detection framework for latent regime transitions | A trading strategy |
| An empirical study of LOB microstructure | Optimised for execution latency |
| A reproducible research pipeline | A production system |
| A contribution to predictive market microstructure | Financial advice |

---

## Contributions

- **Causal formulation** of the latent build-up → stress transition as a three-state latent process
- **Temporal drift identification** — subtle depth and spread drift as a leading precursor to liquidity voids
- **MAX-fusion + rising-edge trigger** — novel detection logic for sub-millisecond microstructure data
- **Empirical demonstration** of strictly positive lead-time over reactive benchmarks across all evaluated regimes

---

## Citation

```bibtex
@article{hiremath2026lob,
  title   = {Early Detection of Latent Micro-Regimes in Limit Order Books},
  author  = {Hiremath, Prakul Sunil and Hiremath, Vruksha Arun},
  year    = {2026},
  doi     = {10.5281/zenodo.19697687}
}
```

---

<div align="center">

Built for **reproducible research** in quantitative finance and machine learning.

*If the signal fires before the storm — it worked.*

</div>

### Core Implementation Code & Architecture
#### File: `Experiments/v2.py`
```python
# ============================================================
#  Latent Micro-Regimes in Limit Order Books:
#  Identification and Early Detection  — v2
#  ─────────────────────────────────────────
#  Key changes over v1:
#    1. Regime 1 = pre-stress build-up, Regime 2 = crisis
#       → HMM entry into regime 1 is the early-warning signal
#    2. Detection via posterior ENTROPY rise, not hard-switch
#    3. Minimum-gap deduplication (no signal flooding)
#    4. Posterior probability smoothing for cleaner signals
#    5. Baselines use identical deduplication
# ============================================================
# !pip install hmmlearn scikit-learn scipy numpy pandas matplotlib

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import gaussian_kde
from sklearn.preprocessing import StandardScaler
from hmmlearn.hmm import GaussianHMM

# ─────────────────────────────────────────
#  0. Global Configuration
# ─────────────────────────────────────────
SEED        = 42
T           = 12_000
N_REGIMES   = 3
MAX_LAG     = 60       # evaluation window (timesteps)
FW_WINDOW   = 20       # forward window for stress label
STRESS_PCT  = 95       # percentile for stress threshold
N_BOOT      = 2_000
MIN_GAP     = 15       # minimum timesteps between two signals (dedup)
PENALTY     = -MAX_LAG

np.random.seed(SEED)

# ─────────────────────────────────────────
#  1. Structured Latent Regime Generator
#     Regime 0 = Normal  (baseline, calm)
#     Regime 1 = Pre-stress build-up  ← the key early-warning state
#     Regime 2 = Crisis / stress peak
#
#  Causal chain:  0 → 1 → 2 → (0 or 1)
#  The HMM must learn that regime 1 is a harbinger of regime 2.
#  We encode this by:
#    • Making spread/depth in regime 1 intermediate
#    • Making transitions 0→1 more likely than 0→2 directly
#    • Stress events defined on FUTURE spread (no leakage)
# ─────────────────────────────────────────

REGIME_PARAMS = {
    # spread:  mu, sigma (log-normal)
    # depth:   mu, sigma (AR-1)
    # imb:     mu, sigma (truncated normal)
    # vol_base: scaling factor
    0: dict(sp_mu=1.5,  sp_sig=0.25, dp_mu=120, dp_sig=10, ib_mu=0.00, ib_sig=0.07, vb=0.35),
    1: dict(sp_mu=3.2,  sp_sig=0.55, dp_mu= 88, dp_sig=16, ib_mu=0.22, ib_sig=0.13, vb=1.10),
    2: dict(sp_mu=7.5,  sp_sig=1.20, dp_mu= 42, dp_sig=22, ib_mu=0.48, ib_sig=0.22, vb=2.90),
}

def build_causal_transition_matrix() -> np.ndarray:
    """
    Transition matrix with causal structure:
      - 0 → 1 much more likely than 0 → 2   (stress builds gradually)
      - 1 → 2 is the crisis trigger
      - 2 → 0 or 1 (recovery)
    """
    P = np.array([
        [0.970, 0.028, 0.002],   # Normal   → mostly stays
        [0.060, 0.900, 0.040],   # Pre-stress → can escalate
        [0.100, 0.150, 0.750],   # Crisis   → decays back
    ])
    # Normalise rows (safety)
    return P / P.sum(axis=1, keepdims=True)


def simulate_latent_chain(T, P, pi0, rng):
    K = P.shape[0]
    Z = np.empty(T, dtype=int)
    Z[0] = rng.choice(K, p=pi0)
    for t in range(1, T):
        Z[t] = rng.choice(K, p=P[Z[t - 1]])
    return Z


def generate_lob_data(T, rng):
    """
    Simulate LOB features under a causal Markov-switching model.

    Hawkes-like self-excitation on spread ensures bursts cluster
    without trivially revealing regime via a single feature.
    """
    P   = build_causal_transition_matrix()
    pi0 = np.array([0.85, 0.12, 0.03])
    Z   = simulate_latent_chain(T, P, pi0, rng)

    spread    = np.zeros(T)
    depth     = np.zeros(T)
    imbalance = np.zeros(T)

    # Spread: log-normal + Hawkes excitation
    hawkes = 0.0
    decay  = 0.88
    for t in range(T):
        p = REGIME_PARAMS[Z[t]]
        hawkes = hawkes * decay
        eps    = rng.normal(0, p['sp_sig'])
        spread[t] = np.exp(np.log(p['sp_mu']) + 0.12 * hawkes + eps)
        if spread[t] > np.exp(np.log(p['sp_mu']) + p['sp_sig']):
            hawkes += 0.25

    # Depth: mean-reverting AR(1)
    phi      = 0.93
    depth[0] = REGIME_PARAMS[Z[0]]['dp_mu']
    for t in range(1, T):
        p = REGIME_PARAMS[Z[t]]
        depth[t] = phi * depth[t-1] + (1-phi) * p['dp_mu'] + rng.normal(0, p['dp_sig'])
    depth = np.clip(depth, 5, None)

    # Imbalance: truncated normal
    for t in range(T):
        p = REGIME_PARAMS[Z[t]]
        imbalance[t] = np.clip(rng.normal(p['ib_mu'], p['ib_sig']), -1, 1)

    # Rolling spread vol (20-step)
    roll_vol = pd.Series(spread).pct_change().rolling(20).std().fillna(0).values

    # OFI proxy
    ofi = imbalance * np.abs(np.diff(spread, prepend=spread[0]))

    X = np.column_stack([spread, depth, imbalance, roll_vol, ofi])
    return X, Z


# ─────────────────────────────────────────
#  2. Feature Engineering & Normalisation
# ─────────────────────────────────────────

def engineer_features(X_raw):
    spread    = X_raw[:, 0]
    depth     = X_raw[:, 1]
    imbalance = X_raw[:, 2]
    roll_vol  = X_raw[:, 3]
    ofi       = X_raw[:, 4]

    sd_ratio   = spread / (depth + 1e-6)
    abs_imb    = np.abs(imbalance)
    cum_ofi    = pd.Series(ofi).rolling(50, min_periods=1).mean().values
    roll_depth = pd.Series(depth).rolling(20).mean().fillna(method='bfill').values

    X_full = np.column_stack([
        spread, depth, imbalance, roll_vol, ofi,
        sd_ratio, abs_imb, cum_ofi, roll_depth
    ])
    scaler   = StandardScaler()
    X_scaled = scaler.fit_transform(X_full)
    return X_scaled, scaler


# ─────────────────────────────────────────
#  3. HMM Fitting
# ─────────────────────────────────────────

def fit_hmm(X, n_components=N_REGIMES, n_restarts=10, rng_seed=SEED):
    best_score, best_model = -np.inf, None
    for k in range(n_restarts):
        model = GaussianHMM(
            n_components    = n_components,
            covariance_type = "full",
            n_iter          = 300,
            tol             = 1e-6,
            random_state    = rng_seed + k,
            init_params     = "stmc",
            params          = "stmc",
        )
        try:
            model.fit(X)
            score = model.score(X)
            if score > best_score:
                best_score, best_model = score, model
        except Exception:
            continue
    if best_model is None:
        raise RuntimeError("HMM fitting failed.")
    return best_model


# ─────────────────────────────────────────
#  4. Stress Event Definition (no leakage)
# ─────────────────────────────────────────

def define_stress_events(X_raw, fw=FW_WINDOW, pct=STRESS_PCT):
    spread    = X_raw[:, 0]
    threshold = np.percentile(spread, pct)
    sigma = [t for t in range(len(spread) - fw)
             if np.mean(spread[t+1:t+fw+1]) > threshold]
    return np.array(sigma, dtype=int)


# ─────────────────────────────────────────
#  5. Signal Computation (the core upgrade)
# ─────────────────────────────────────────

def state_entropy(posterior):
    """Shannon entropy of the posterior state distribution at each step."""
    eps = 1e-12
    return -np.sum(posterior * np.log(posterior + eps), axis=1)


def deduplicate(indices, min_gap=MIN_GAP):
    """
    Keep only the FIRST index in each cluster of indices
    that are within min_gap of each other.
    This prevents signal flooding.
    """
    if len(indices) == 0:
        return indices
    out  = [indices[0]]
    for idx in indices[1:]:
        if idx - out[-1] >= min_gap:
            out.append(idx)
    return np.array(out, dtype=int)


def model_signals(model, X_scaled, Z_hat,
                  entropy_pct=80, smooth_window=5, min_gap=MIN_GAP):
    """
    Uncertainty-based early-warning signal.

    Strategy (three complementary triggers, unioned then deduped):
      A) Entropy spike: posterior uncertainty rises sharply
         → captures "the HMM is unsure", a known pre-transition marker
      B) Pre-stress state entry: Z_hat transitions INTO the intermediate
         state (state with 2nd-highest mean spread)
         → aligns detection with causal regime structure
      C) Entropy trend: rolling entropy slope turns positive
         → catches gradual build-up before a hard switch

    All triggers are deduplicated so N(τ) stays controlled.
    """
    posterior = model.predict_proba(X_scaled)          # (T, K)

    # ── Smooth posterior to reduce HMM jitter ──
    smooth_post = pd.DataFrame(posterior).rolling(
        smooth_window, min_periods=1, center=True).mean().values

    entropy = state_entropy(smooth_post)

    # ── Identify the "pre-stress" HMM state ──
    # We rank states by their mean spread (feature 0 in raw space)
    means_raw = model.means_[:, 0]                    # spread dim of HMM means
    state_rank = np.argsort(means_raw)                 # [low, mid, high]
    prestress_state = state_rank[1]                    # intermediate spread state

    # ── Trigger A: entropy spike ──
    ent_thresh = np.percentile(entropy, entropy_pct)
    sig_A = np.where(entropy > ent_thresh)[0]

    # ── Trigger B: entry into pre-stress state ──
    enters_prestress = (Z_hat[1:] == prestress_state) & (Z_hat[:-1] != prestress_state)
    sig_B = np.where(enters_prestress)[0]

    # ── Trigger C: entropy slope turns positive ──
    ent_slope = pd.Series(entropy).diff(5).fillna(0).values
    slope_thresh = np.percentile(ent_slope[ent_slope > 0], 70)
    sig_C = np.where(ent_slope > slope_thresh)[0]

    # ── Union + deduplicate ──
    all_signals = np.unique(np.concatenate([sig_A, sig_B, sig_C]))
    tau = deduplicate(all_signals, min_gap=min_gap)
    return tau


def imbalance_baseline(X_raw, pct=90, min_gap=MIN_GAP):
    imb       = np.abs(X_raw[:, 2])
    threshold = np.percentile(imb, pct)
    raw       = np.where(imb > threshold)[0]
    return deduplicate(raw, min_gap=min_gap)


def volatility_baseline(X_raw, pct=90, min_gap=MIN_GAP):
    roll_vol  = X_raw[:, 3]
    threshold = np.percentile(roll_vol, pct)
    raw       = np.where(roll_vol > threshold)[0]
    return deduplicate(raw, min_gap=min_gap)


# ─────────────────────────────────────────
#  6. Lead-Time Evaluation
# ─────────────────────────────────────────

def compute_lead_times(tau, sigma, max_lag=MAX_LAG):
    deltas = np.empty(len(tau), dtype=float)
    for i, t in enumerate(tau):
        cands = sigma[(sigma > t) & (sigma <= t + max_lag)]
        deltas[i] = (cands[0] - t) if len(cands) > 0 else PENALTY
    return deltas


def evaluation_metrics(deltas):
    valid = deltas > 0
    return dict(
        mean_delta  = float(np.mean(deltas)),
        pct_early   = float(np.mean(valid)),
        mean_early  = float(np.mean(deltas[valid])) if valid.any() else 0.0,
        std_delta   = float(np.std(deltas)),
        n_tau       = int(len(deltas)),
        n_early     = int(valid.sum()),
    )


# ─────────────────────────────────────────
#  7. Bootstrap CI + Mann–Whitney
# ─────────────────────────────────────────

def bootstrap_ci(deltas, stat_fn=np.mean, n_boot=N_BOOT, alpha=0.05, seed=SEED):
    rng = np.random.default_rng(seed)
    boot = np.array([stat_fn(rng.choice(deltas, size=len(deltas), replace=True))
                     for _ in range(n_boot)])
    return float(np.percentile(boot, 100*alpha/2)), float(np.percentile(boot, 100*(1-alpha/2)))


def mannwhitney_test(a, b):
    return stats.mannwhitneyu(a, b, alternative="two-sided")


# ─────────────────────────────────────────
#  8. Publication-Quality Visualisation
# ─────────────────────────────────────────

PALETTE = {"Model": "#2C6FAC", "Imbalance": "#D94F3D", "Volatility": "#5AAE61"}

plt.rcParams.update({
    "font.family"      : "serif",
    "font.size"        : 11,
    "axes.spines.top"  : False,
    "axes.spines.right": False,
    "axes.linewidth"   : 0.8,
    "figure.dpi"       : 150,
})


def plot_entropy_and_regimes(X_raw, Z_true, Z_hat, entropy, tau_model,
                              sigma, n_show=2500):
    """
    Four-panel diagnostic:
      1. Spread with true regime shading
      2. Posterior entropy (with signal thresholds and triggers marked)
      3. Inferred HMM state
      4. Depth with stress events
    """
    t_end = min(n_show, len(Z_true))
    t_ax  = np.arange(t_end)
    spread = X_raw[:t_end, 0]
    depth  = X_raw[:t_end, 1]

    tau_vis   = tau_model[tau_model < t_end]
    sigma_vis = sigma[sigma < t_end]

    regime_colors = {0: "#DDEEFF", 1: "#FFF3CD", 2: "#FFDDDD"}

    fig, axes = plt.subplots(4, 1, figsize=(12, 9), sharex=True,
                              gridspec_kw={"height_ratios": [2, 2, 1, 2]})

    # Panel 1 — Spread + true shading
    ax = axes[0]
    for k, c in regime_colors.items():
        ax.fill_between(t_ax, 0, spread.max()*1.1,
                        where=Z_true[:t_end]==k, color=c, alpha=0.55,
                        label=f"State {k}")
    ax.plot(t_ax, spread, lw=0.7, color="#1A1A2E")
    ax.set_ylabel("Bid-Ask Spread")
    ax.legend(loc="upper right", fontsize=8, frameon=False, ncol=3)
    ax.set_title("True Regimes · Posterior Entropy · Inferred States · Market Depth",
                 fontsize=12, pad=8)

    # Panel 2 — Entropy + model triggers
    ax = axes[1]
    ent_vis = entropy[:t_end]
    ax.plot(t_ax, ent_vis, lw=0.9, color="#555555", alpha=0.85, label="Entropy")
    ent_thresh = np.percentile(entropy, 80)
    ax.axhline(ent_thresh, color="#FF8800", lw=1.0, ls="--", label="80th pct threshold")
    ax.vlines(tau_vis, ent_vis.min(), ent_vis.max(),
              color=PALETTE["Model"], lw=0.7, alpha=0.6, label="Model signal τ")
    ax.set_ylabel("Posterior Entropy")
    ax.legend(loc="upper right", fontsize=8, frameon=False)

    # Panel 3 — Inferred HMM state
    ax = axes[2]
    ax.step(t_ax, Z_hat[:t_end], lw=0.9, color=PALETTE["Model"])
    ax.set_ylabel("HMM State")
    ax.set_yticks([0, 1, 2])

    # Panel 4 — Depth + stress events
    ax = axes[3]
    ax.plot(t_ax, depth, lw=0.7, color="#2D6A4F")
    ax.vlines(sigma_vis, depth.min(), depth.max(),
              color=PALETTE["Imbalance"], lw=0.7, alpha=0.5, label="Stress event σ")
    ax.set_ylabel("Market Depth")
    ax.set_xlabel("Timestep")
    ax.legend(loc="upper right", fontsize=8, frameon=False)

    fig.tight_layout()
    plt.show()


def plot_lead_time_densities(delta_dict, max_lag=MAX_LAG):
    fig, ax = plt.subplots(figsize=(8, 4.5))
    x_grid = np.linspace(-max_lag-5, max_lag+5, 600)

    for i, (name, deltas) in enumerate(delta_dict.items()):
        color  = PALETTE[name]
        valid  = deltas[deltas > PENALTY]
        if len(valid) > 5:
            kde = gaussian_kde(valid, bw_method="scott")
            ax.plot(x_grid, kde(x_grid), lw=2.2, color=color, label=name)
            ax.fill_between(x_grid, kde(x_grid), alpha=0.13, color=color)
        pf = np.mean(deltas <= PENALTY)
        ax.annotate(f"missed={pf:.1%}", xy=(-max_lag+1, 0.004*(i+1)),
                    color=color, fontsize=8.5)

    ax.axvline(0, color="gray", lw=1.0, ls="--", label="Zero lead-time")
    ax.set_xlabel("Lead
# ... [TRUNCATED FILE CONTENT]
```

#### File: `Experiments/v1.py`
```python
# ============================================================
#  Latent Micro-Regimes in Limit Order Books:
#  Identification and Early Detection
#  ─────────────────────────────────────────
#  Research-grade pipeline — Colab-ready single script
#  Authors: [redacted for blind review]
# ============================================================
# Install (uncomment in Colab):
# !pip install hmmlearn scikit-learn scipy numpy pandas matplotlib

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy import stats
from scipy.stats import gaussian_kde
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from hmmlearn.hmm import GaussianHMM

# ─────────────────────────────────────────
#  0. Global Configuration
# ─────────────────────────────────────────
SEED       = 42
T          = 12_000          # total timesteps
N_REGIMES  = 3               # latent states: Normal, Stressed, Crisis
MAX_LAG    = 60              # evaluation window (timesteps)
FW_WINDOW  = 20              # forward window for stress event definition
N_BOOT     = 2_000           # bootstrap replicates
STRESS_PCT = 95              # percentile threshold for stress definition

np.random.seed(SEED)

# ─────────────────────────────────────────
#  1. Structured Latent Regime Data Generator
# ─────────────────────────────────────────

def build_transition_matrix(persist: list[float]) -> np.ndarray:
    """
    Build a row-stochastic transition matrix from persistence probabilities.
    Off-diagonal mass is split evenly among other states.

    Parameters
    ----------
    persist : list of length N_REGIMES
        Self-transition probability for each state.

    Returns
    -------
    P : (N_REGIMES, N_REGIMES) ndarray
    """
    K = len(persist)
    P = np.zeros((K, K))
    for i, p in enumerate(persist):
        P[i, i] = p
        off = (1 - p) / (K - 1)
        for j in range(K):
            if j != i:
                P[i, j] = off
    return P


def simulate_latent_chain(T: int, P: np.ndarray, pi0: np.ndarray,
                           rng: np.random.Generator) -> np.ndarray:
    """
    Simulate a discrete-time Markov chain.

    Parameters
    ----------
    T   : int — number of timesteps
    P   : (K, K) transition matrix
    pi0 : (K,) initial distribution
    rng : numpy Generator

    Returns
    -------
    Z : (T,) int array of latent states
    """
    K = P.shape[0]
    Z = np.empty(T, dtype=int)
    Z[0] = rng.choice(K, p=pi0)
    for t in range(1, T):
        Z[t] = rng.choice(K, p=P[Z[t - 1]])
    return Z


# Regime-specific parameter sets
#   State 0 — Normal:   tight spread, deep book, balanced flow
#   State 1 — Stressed: wider spread, shallower book, directional flow
#   State 2 — Crisis:   very wide spread, thin book, extreme imbalance
REGIME_PARAMS = {
    #           spread_mu, spread_sig, depth_mu, depth_sig, imb_mu, imb_sig, vol_base
    0: dict(sp_mu=1.5,  sp_sig=0.30, dp_mu=120, dp_sig=12, ib_mu=0.00, ib_sig=0.08, vb=0.40),
    1: dict(sp_mu=3.5,  sp_sig=0.60, dp_mu= 85, dp_sig=18, ib_mu=0.18, ib_sig=0.14, vb=1.20),
    2: dict(sp_mu=7.0,  sp_sig=1.20, dp_mu= 45, dp_sig=22, ib_mu=0.40, ib_sig=0.22, vb=2.80),
}


def generate_lob_data(T: int, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """
    Generate synthetic LOB microstructure data driven by a latent Markov chain.

    Design choices:
    - Regime-conditional mean and volatility for each feature.
    - Spread follows a regime-switching log-normal process (always positive).
    - Depth follows a regime-switching AR(1) process (mean-reverting).
    - Order-flow imbalance is beta-distributed (bounded in [-1, 1]).
    - Cross-sectional noise is injected so no feature alone trivially reveals
      the regime.
    - A Hawkes-inspired self-exciting component adds burst clustering to spread.

    Returns
    -------
    X : (T, 5) feature matrix  [spread, depth, imbalance, roll_vol, ofi]
    Z : (T,)   true latent state sequence
    """
    # 1) Latent chain
    persist = [0.97, 0.93, 0.89]   # high persistence → realistic regimes
    P  = build_transition_matrix(persist)
    pi0 = np.array([0.80, 0.15, 0.05])
    Z  = simulate_latent_chain(T, P, pi0, rng)

    spread     = np.zeros(T)
    depth      = np.zeros(T)
    imbalance  = np.zeros(T)

    # ── Spread: log-normal with Hawkes-like self-excitation ──
    hawkes_intensity = np.zeros(T)
    decay = 0.90
    for t in range(T):
        p = REGIME_PARAMS[Z[t]]
        hawkes_intensity[t] = (hawkes_intensity[t - 1] * decay if t > 0 else 0)
        noise = rng.normal(0, p['sp_sig'])
        log_sp = np.log(p['sp_mu']) + 0.15 * hawkes_intensity[t] + noise
        spread[t] = np.exp(log_sp)
        if spread[t] > np.exp(np.log(p['sp_mu']) + p['sp_sig']):
            hawkes_intensity[t] += 0.30           # self-excite on spike

    # ── Depth: mean-reverting AR(1) per regime ──
    depth[0] = REGIME_PARAMS[Z[0]]['dp_mu']
    phi = 0.92                                    # AR coefficient
    for t in range(1, T):
        p = REGIME_PARAMS[Z[t]]
        depth[t] = phi * depth[t - 1] + (1 - phi) * p['dp_mu'] + rng.normal(0, p['dp_sig'])
    depth = np.clip(depth, 5, None)               # depth always positive

    # ── Order-flow imbalance: truncated normal ──
    for t in range(T):
        p = REGIME_PARAMS[Z[t]]
        raw = rng.normal(p['ib_mu'], p['ib_sig'])
        imbalance[t] = np.clip(raw, -1, 1)

    # ── Engineered features ──
    # Rolling 20-step realised volatility of spread
    roll_vol = pd.Series(spread).pct_change().rolling(20).std().fillna(0).values

    # Order-flow imbalance sign × magnitude (OFI proxy)
    ofi = imbalance * np.abs(np.diff(spread, prepend=spread[0]))

    X = np.column_stack([spread, depth, imbalance, roll_vol, ofi])
    return X, Z


# ─────────────────────────────────────────
#  2. Feature Engineering & Normalisation
# ─────────────────────────────────────────

def engineer_features(X_raw: np.ndarray) -> tuple[np.ndarray, StandardScaler]:
    """
    Augment and normalise the raw feature matrix.

    Raw columns : [spread, depth, imbalance, roll_vol, ofi]
    Added       : [spread/depth ratio, |imbalance|, cumulative ofi (50-step)]

    Returns
    -------
    X_scaled : (T, n_features) normalised array
    scaler   : fitted StandardScaler (for reproducibility)
    """
    spread    = X_raw[:, 0]
    depth     = X_raw[:, 1]
    imbalance = X_raw[:, 2]
    roll_vol  = X_raw[:, 3]
    ofi       = X_raw[:, 4]

    spread_depth_ratio = spread / (depth + 1e-6)
    abs_imb            = np.abs(imbalance)
    cum_ofi            = pd.Series(ofi).rolling(50, min_periods=1).mean().values

    X_full = np.column_stack([
        spread, depth, imbalance, roll_vol, ofi,
        spread_depth_ratio, abs_imb, cum_ofi
    ])

    scaler   = StandardScaler()
    X_scaled = scaler.fit_transform(X_full)
    return X_scaled, scaler


# ─────────────────────────────────────────
#  3. HMM Fitting with Robust Initialisation
# ─────────────────────────────────────────

def fit_hmm(X: np.ndarray, n_components: int = N_REGIMES,
            n_restarts: int = 10, rng_seed: int = SEED) -> GaussianHMM:
    """
    Fit a Gaussian HMM with multiple random restarts and select
    the run with highest log-likelihood.

    Parameters
    ----------
    X           : normalised feature matrix
    n_components: number of latent states
    n_restarts  : number of random restarts
    rng_seed    : base seed

    Returns
    -------
    best_model : GaussianHMM with highest converged log-likelihood
    """
    best_score = -np.inf
    best_model = None

    for k in range(n_restarts):
        model = GaussianHMM(
            n_components    = n_components,
            covariance_type = "full",
            n_iter          = 200,
            tol             = 1e-5,
            random_state    = rng_seed + k,
            init_params     = "stmc",
            params          = "stmc",
        )
        try:
            model.fit(X)
            score = model.score(X)
            if score > best_score:
                best_score = score
                best_model = model
        except Exception:
            continue

    if best_model is None:
        raise RuntimeError("HMM fitting failed across all restarts.")

    return best_model


# ─────────────────────────────────────────
#  4. Liquidity Stress Event Definition
# ─────────────────────────────────────────

def define_stress_events(X_raw: np.ndarray, fw: int = FW_WINDOW,
                          pct: float = STRESS_PCT) -> np.ndarray:
    """
    Identify liquidity stress events WITHOUT lookahead leakage.

    A timestep t is a stress event if the mean spread over
    [t+1, t+fw] exceeds the global spread 'pct'-percentile.

    The threshold is computed on the FULL spread series but
    the forward window ensures the label at t uses only future data.

    Parameters
    ----------
    X_raw : raw feature matrix (column 0 = spread)
    fw    : forward window length
    pct   : percentile for threshold

    Returns
    -------
    sigma : 1-D array of stress event timestep indices
    """
    spread    = X_raw[:, 0]
    threshold = np.percentile(spread, pct)
    sigma     = []
    for t in range(len(spread) - fw):
        if np.mean(spread[t + 1: t + fw + 1]) > threshold:
            sigma.append(t)
    return np.array(sigma, dtype=int)


# ─────────────────────────────────────────
#  5. Regime Transition Detection
# ─────────────────────────────────────────

def detect_transitions(Z_hat: np.ndarray) -> np.ndarray:
    """
    Return indices just *before* each detected regime change.

    Parameters
    ----------
    Z_hat : (T,) array of inferred (or true) state labels

    Returns
    -------
    tau : 1-D int array of transition indices
    """
    return np.where(np.diff(Z_hat) != 0)[0]


# ─────────────────────────────────────────
#  6. Lead-Time Evaluation
# ─────────────────────────────────────────

PENALTY = -MAX_LAG   # assigned delta when no stress event found in window


def compute_lead_times(tau: np.ndarray, sigma: np.ndarray,
                        max_lag: int = MAX_LAG) -> np.ndarray:
    """
    For each detected transition τ, find the first stress event σ
    in (τ, τ + max_lag].

    Returns
    -------
    deltas : (len(tau),) array
        Positive  → transition preceded stress (early detection)
        PENALTY   → no stress event in window (missed / false alarm)
    """
    deltas = np.empty(len(tau), dtype=float)
    for i, t in enumerate(tau):
        candidates = sigma[(sigma > t) & (sigma <= t + max_lag)]
        deltas[i] = (candidates[0] - t) if len(candidates) > 0 else PENALTY
    return deltas


def evaluation_metrics(deltas: np.ndarray, max_lag: int = MAX_LAG
                        ) -> dict:
    """
    Summarise lead-time performance.

    Metrics
    -------
    mean_delta   : mean lead time (penalised)
    pct_early    : fraction of transitions that preceded a stress event
    mean_early   : mean lead time conditional on early detection
    std_delta    : standard deviation of delta
    n_tau        : total number of detected transitions
    n_early      : number of early detections
    """
    valid = deltas > 0
    return dict(
        mean_delta  = float(np.mean(deltas)),
        pct_early   = float(np.mean(valid)),
        mean_early  = float(np.mean(deltas[valid])) if valid.any() else 0.0,
        std_delta   = float(np.std(deltas)),
        n_tau       = int(len(deltas)),
        n_early     = int(valid.sum()),
    )


# ─────────────────────────────────────────
#  7. Baseline Detectors
# ─────────────────────────────────────────

def imbalance_baseline(X_raw: np.ndarray, pct: float = 90) -> np.ndarray:
    """
    Trigger when |order-flow imbalance| exceeds a percentile threshold.
    Noise is NOT added here; the baseline uses the same raw features as the
    HMM to ensure a fair comparison.
    """
    imb       = np.abs(X_raw[:, 2])
    threshold = np.percentile(imb, pct)
    return np.where(imb > threshold)[0]


def volatility_baseline(X_raw: np.ndarray, pct: float = 90) -> np.ndarray:
    """
    Trigger when rolling spread volatility exceeds a percentile threshold.
    """
    roll_vol  = X_raw[:, 3]
    threshold = np.percentile(roll_vol, pct)
    return np.where(roll_vol > threshold)[0]


# ─────────────────────────────────────────
#  8. Bootstrap Confidence Intervals
# ─────────────────────────────────────────

def bootstrap_ci(deltas: np.ndarray, stat_fn=np.mean,
                  n_boot: int = N_BOOT, alpha: float = 0.05,
                  seed: int = SEED) -> tuple[float, float]:
    """
    Percentile bootstrap confidence interval for a scalar statistic.

    Returns
    -------
    (lower, upper) CI at (1-alpha) level
    """
    rng      = np.random.default_rng(seed)
    boot_stats = np.array([
        stat_fn(rng.choice(deltas, size=len(deltas), replace=True))
        for _ in range(n_boot)
    ])
    return (float(np.percentile(boot_stats, 100 * alpha / 2)),
            float(np.percentile(boot_stats, 100 * (1 - alpha / 2))))


def mannwhitney_test(a: np.ndarray, b: np.ndarray) -> tuple[float, float]:
    """
    Two-sided Mann–Whitney U test (non-parametric, appropriate for
    skewed lead-time distributions).

    Returns (U-statistic, p-value).
    """
    return stats.mannwhitneyu(a, b, alternative="two-sided")


# ─────────────────────────────────────────
#  9. Publication-Quality Visualisation
# ─────────────────────────────────────────

PALETTE = {
    "Model"      : "#2C6FAC",
    "Imbalance"  : "#D94F3D",
    "Volatility" : "#5AAE61",
}

plt.rcParams.update({
    "font.family"      : "serif",
    "font.size"        : 11,
    "axes.spines.top"  : False,
    "axes.spines.right": False,
    "axes.linewidth"   : 0.8,
    "xtick.major.width": 0.8,
    "ytick.major.width": 0.8,
    "figure.dpi"       : 150,
})


def plot_lead_time_densities(delta_dict: dict, max_lag: int = MAX_LAG,
                              save_path: str = None):
    """
    Overlapping KDE plots of lead-time distributions for each detector.

    Parameters
    ----------
    delta_dict : {'Model': deltas, 'Imbalance': deltas, 'Volatility': deltas}
    max_lag    : used to shade the penalty region
    save_path  : if provided, saves the figure to this path
    """
    fig, ax = plt.subplots(figsize=(8, 4.5))

    x_grid = np.linspace(-max_lag - 5, max_lag + 5, 500)

    for name, deltas in delta_dict.items():
        color = PALETTE[name]
        # KDE on non-penalty values only (for readability)
        valid  = deltas[deltas > PENALTY]
        if len(valid) > 5:
            kde = gaussian_kde(valid, bw_method="scott")
            ax.plot(x_grid, kde(x_grid), lw=2.2, color=color, label=name)
            ax.fill_between(x_grid, kde(x_grid), alpha=0.12, color=color)

       
# ... [TRUNCATED FILE CONTENT]
```

#### File: `Experiments/v3.py`
```python
# ============================================================
#  Latent Micro-Regimes in Limit Order Books:
#  Identification and Early Detection  — v3
#  ─────────────────────────────────────────
#  KEY UPGRADE over v2:
#    Hard regime-switch detection → Pre-transition instability
#    detection via HMM posterior-based composite signal.
#
#  Signal components (all from posterior probabilities):
#    H_t  = Shannon entropy of p(z | x_t)            [primary]
#    U_t  = 1 - max_z p(z | x_t)                     [uncertainty]
#    TI_t = ||p(z|x_t) - p(z|x_{t-1})||_1            [transition intensity]
#    PS_t = pre-stress state posterior (regime 1)     [regime-specific]
#
#  Composite score = weighted average → adaptive percentile threshold
#  + minimum-gap deduplication → sparse, meaningful signals τ
#
#  Evaluation pipeline (UNCHANGED from v2):
#    - leakage-free stress events
#    - lead-time Δ = σ − τ
#    - bootstrap CI + Mann–Whitney
#    - baselines (imbalance + volatility) with same dedup
# ============================================================

# !pip install hmmlearn scikit-learn scipy numpy pandas matplotlib

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import gaussian_kde
from sklearn.preprocessing import StandardScaler
from hmmlearn.hmm import GaussianHMM

# ─────────────────────────────────────────
#  0. Global Configuration
# ─────────────────────────────────────────
SEED        = 42
T           = 12_000
N_REGIMES   = 3
MAX_LAG     = 60       # evaluation window (timesteps)
FW_WINDOW   = 20       # forward window for stress label
STRESS_PCT  = 95       # percentile for stress threshold
N_BOOT      = 2_000
MIN_GAP     = 20       # min timesteps between two signals (dedup)
PENALTY     = -MAX_LAG

# Composite signal weights
W_ENTROPY   = 0.40
W_UNCERT    = 0.25
W_TRANS     = 0.20
W_PRESTRESS = 0.15

# Detection threshold: fire when composite > this percentile
SIGNAL_PCT  = 82

np.random.seed(SEED)

# ─────────────────────────────────────────
#  1. Structured Latent Regime Generator
#     Regime 0 = Normal  (baseline, calm)
#     Regime 1 = Pre-stress build-up  ← harbinger state
#     Regime 2 = Crisis / stress peak
#
#  Causal chain:  0 → 1 → 2 → (0 or 1)
# ─────────────────────────────────────────

REGIME_PARAMS = {
    0: dict(sp_mu=1.5,  sp_sig=0.25, dp_mu=120, dp_sig=10,
            ib_mu=0.00, ib_sig=0.07, vb=0.35),
    1: dict(sp_mu=3.2,  sp_sig=0.55, dp_mu= 88, dp_sig=16,
            ib_mu=0.22, ib_sig=0.13, vb=1.10),
    2: dict(sp_mu=7.5,  sp_sig=1.20, dp_mu= 42, dp_sig=22,
            ib_mu=0.48, ib_sig=0.22, vb=2.90),
}


def build_causal_transition_matrix() -> np.ndarray:
    P = np.array([
        [0.970, 0.028, 0.002],
        [0.060, 0.900, 0.040],
        [0.100, 0.150, 0.750],
    ])
    return P / P.sum(axis=1, keepdims=True)


def simulate_latent_chain(T, P, pi0, rng):
    K = P.shape[0]
    Z = np.empty(T, dtype=int)
    Z[0] = rng.choice(K, p=pi0)
    for t in range(1, T):
        Z[t] = rng.choice(K, p=P[Z[t - 1]])
    return Z


def generate_lob_data(T, rng):
    P   = build_causal_transition_matrix()
    pi0 = np.array([0.85, 0.12, 0.03])
    Z   = simulate_latent_chain(T, P, pi0, rng)

    spread    = np.zeros(T)
    depth     = np.zeros(T)
    imbalance = np.zeros(T)

    hawkes = 0.0
    decay  = 0.88
    for t in range(T):
        p = REGIME_PARAMS[Z[t]]
        hawkes = hawkes * decay
        eps    = rng.normal(0, p['sp_sig'])
        spread[t] = np.exp(np.log(p['sp_mu']) + 0.12 * hawkes + eps)
        if spread[t] > np.exp(np.log(p['sp_mu']) + p['sp_sig']):
            hawkes += 0.25

    phi      = 0.93
    depth[0] = REGIME_PARAMS[Z[0]]['dp_mu']
    for t in range(1, T):
        p = REGIME_PARAMS[Z[t]]
        depth[t] = phi * depth[t-1] + (1-phi) * p['dp_mu'] + rng.normal(0, p['dp_sig'])
    depth = np.clip(depth, 5, None)

    for t in range(T):
        p = REGIME_PARAMS[Z[t]]
        imbalance[t] = np.clip(rng.normal(p['ib_mu'], p['ib_sig']), -1, 1)

    roll_vol = pd.Series(spread).pct_change().rolling(20).std().fillna(0).values
    ofi = imbalance * np.abs(np.diff(spread, prepend=spread[0]))

    X = np.column_stack([spread, depth, imbalance, roll_vol, ofi])
    return X, Z


# ─────────────────────────────────────────
#  2. Feature Engineering & Normalisation
# ─────────────────────────────────────────

def engineer_features(X_raw):
    spread    = X_raw[:, 0]
    depth     = X_raw[:, 1]
    imbalance = X_raw[:, 2]
    roll_vol  = X_raw[:, 3]
    ofi       = X_raw[:, 4]

    sd_ratio   = spread / (depth + 1e-6)
    abs_imb    = np.abs(imbalance)
    cum_ofi    = pd.Series(ofi).rolling(50, min_periods=1).mean().values
    roll_depth = pd.Series(depth).rolling(20).mean().fillna(method='bfill').values

    X_full = np.column_stack([
        spread, depth, imbalance, roll_vol, ofi,
        sd_ratio, abs_imb, cum_ofi, roll_depth
    ])
    scaler   = StandardScaler()
    X_scaled = scaler.fit_transform(X_full)
    return X_scaled, scaler


# ─────────────────────────────────────────
#  3. HMM Fitting
# ─────────────────────────────────────────

def fit_hmm(X, n_components=N_REGIMES, n_restarts=10, rng_seed=SEED):
    best_score, best_model = -np.inf, None
    for k in range(n_restarts):
        model = GaussianHMM(
            n_components    = n_components,
            covariance_type = "full",
            n_iter          = 300,
            tol             = 1e-6,
            random_state    = rng_seed + k,
            init_params     = "stmc",
            params          = "stmc",
        )
        try:
            model.fit(X)
            score = model.score(X)
            if score > best_score:
                best_score, best_model = score, model
        except Exception:
            continue
    if best_model is None:
        raise RuntimeError("HMM fitting failed.")
    return best_model


# ─────────────────────────────────────────
#  4. Stress Event Definition (no leakage)
# ─────────────────────────────────────────

def define_stress_events(X_raw, fw=FW_WINDOW, pct=STRESS_PCT):
    spread    = X_raw[:, 0]
    threshold = np.percentile(spread, pct)
    sigma = [t for t in range(len(spread) - fw)
             if np.mean(spread[t+1:t+fw+1]) > threshold]
    return np.array(sigma, dtype=int)


# ─────────────────────────────────────────
#  5. Posterior-Based Signal Computation
#     *** CORE UPGRADE ***
#
#  Four posterior-derived measures fused into a composite score.
#  Signals fire when the composite exceeds an adaptive threshold.
# ─────────────────────────────────────────

def smooth_posterior(posterior, window=5):
    """Causal rolling average to reduce HMM jitter (no look-ahead)."""
    return pd.DataFrame(posterior).rolling(window, min_periods=1).mean().values


def entropy_signal(post):
    """H_t = -∑ p_k log p_k  (high = uncertain = pre-transition)"""
    eps = 1e-12
    return -np.sum(post * np.log(post + eps), axis=1)


def uncertainty_signal(post):
    """U_t = 1 - max_k p_k  (high = diffuse posterior)"""
    return 1.0 - post.max(axis=1)


def transition_intensity_signal(post):
    """TI_t = L1 distance between consecutive posteriors."""
    diff = np.abs(np.diff(post, axis=0))
    ti   = diff.sum(axis=1)
    return np.concatenate([[0.0], ti])


def prestress_posterior_signal(post, model):
    """PS_t = posterior mass on the pre-stress (intermediate) HMM state."""
    means_raw    = model.means_[:, 0]        # spread dimension
    state_rank   = np.argsort(means_raw)
    prestress_id = state_rank[1]             # intermediate spread state
    return post[:, prestress_id]


def build_composite_score(post, model,
                           w_h=W_ENTROPY, w_u=W_UNCERT,
                           w_ti=W_TRANS,  w_ps=W_PRESTRESS):
    """
    Weighted composite of four posterior-derived instability signals.
    Each component is min-max normalised before weighting so that
    differences in scale do not bias the fusion.
    """
    H  = entropy_signal(post)
    U  = uncertainty_signal(post)
    TI = transition_intensity_signal(post)
    PS = prestress_posterior_signal(post, model)

    def _norm(x):
        lo, hi = x.min(), x.max()
        return (x - lo) / (hi - lo + 1e-12)

    score = (w_h  * _norm(H)  +
             w_u  * _norm(U)  +
             w_ti * _norm(TI) +
             w_ps * _norm(PS))
    return score, H, U, TI, PS


def deduplicate(indices, min_gap=MIN_GAP):
    """Keep only the first index in each cluster within min_gap."""
    if len(indices) == 0:
        return indices
    out = [indices[0]]
    for idx in indices[1:]:
        if idx - out[-1] >= min_gap:
            out.append(idx)
    return np.array(out, dtype=int)


def model_signals(model, X_scaled,
                  smooth_win=5,
                  signal_pct=SIGNAL_PCT,
                  min_gap=MIN_GAP):
    """
    Generate early-warning signals τ from the composite instability score.

    Steps:
      1. Compute smoothed posterior (causal rolling mean)
      2. Build composite score from 4 posterior-derived measures
      3. Threshold at adaptive percentile (signal_pct)
      4. Deduplicate to enforce minimum gap

    Returns τ (signal times), composite score, and component signals.
    """
    posterior   = model.predict_proba(X_scaled)
    post_smooth = smooth_posterior(posterior, window=smooth_win)

    score, H, U, TI, PS = build_composite_score(post_smooth, model)

    threshold = np.percentile(score, signal_pct)
    raw       = np.where(score > threshold)[0]
    tau       = deduplicate(raw, min_gap=min_gap)

    return tau, score, H, U, TI, PS


def imbalance_baseline(X_raw, pct=90, min_gap=MIN_GAP):
    imb       = np.abs(X_raw[:, 2])
    threshold = np.percentile(imb, pct)
    raw       = np.where(imb > threshold)[0]
    return deduplicate(raw, min_gap=min_gap)


def volatility_baseline(X_raw, pct=90, min_gap=MIN_GAP):
    roll_vol  = X_raw[:, 3]
    threshold = np.percentile(roll_vol, pct)
    raw       = np.where(roll_vol > threshold)[0]
    return deduplicate(raw, min_gap=min_gap)


# ─────────────────────────────────────────
#  6. Lead-Time Evaluation (UNCHANGED)
# ─────────────────────────────────────────

def compute_lead_times(tau, sigma, max_lag=MAX_LAG):
    deltas = np.empty(len(tau), dtype=float)
    for i, t in enumerate(tau):
        cands = sigma[(sigma > t) & (sigma <= t + max_lag)]
        deltas[i] = (cands[0] - t) if len(cands) > 0 else PENALTY
    return deltas


def evaluation_metrics(deltas):
    valid = deltas > 0
    return dict(
        mean_delta = float(np.mean(deltas)),
        pct_early  = float(np.mean(valid)),
        mean_early = float(np.mean(deltas[valid])) if valid.any() else 0.0,
        std_delta  = float(np.std(deltas)),
        n_tau      = int(len(deltas)),
        n_early    = int(valid.sum()),
    )


# ─────────────────────────────────────────
#  7. Bootstrap CI + Mann–Whitney (UNCHANGED)
# ─────────────────────────────────────────

def bootstrap_ci(deltas, stat_fn=np.mean, n_boot=N_BOOT, alpha=0.05, seed=SEED):
    rng  = np.random.default_rng(seed)
    boot = np.array([stat_fn(rng.choice(deltas, size=len(deltas), replace=True))
                     for _ in range(n_boot)])
    return float(np.percentile(boot, 100*alpha/2)), float(np.percentile(boot, 100*(1-alpha/2)))


def mannwhitney_test(a, b):
    return stats.mannwhitneyu(a, b, alternative="two-sided")


# ─────────────────────────────────────────
#  8. Visualisation
# ─────────────────────────────────────────

PALETTE = {
    "Model"     : "#2C6FAC",
    "Imbalance" : "#D94F3D",
    "Volatility": "#5AAE61",
}

plt.rcParams.update({
    "font.family"      : "serif",
    "font.size"        : 11,
    "axes.spines.top"  : False,
    "axes.spines.right": False,
    "axes.linewidth"   : 0.8,
    "figure.dpi"       : 150,
})


def plot_composite_signal(X_raw, Z_true, score, H, U, TI, tau_model,
                           sigma, n_show=3000):
    """
    Five-panel diagnostic:
      1. Spread + true regime shading
      2. Composite instability score + threshold + signal fires
      3. Entropy H_t
      4. Uncertainty U_t + Transition intensity TI_t
      5. Pre-stress posterior PS_t
    """
    t_end = min(n_show, len(Z_true))
    t_ax  = np.arange(t_end)
    spread  = X_raw[:t_end, 0]

    tau_vis   = tau_model[tau_model < t_end]
    sigma_vis = sigma[sigma < t_end]

    regime_colors = {0: "#DDEEFF", 1: "#FFF3CD", 2: "#FFDDDD"}

    fig, axes = plt.subplots(5, 1, figsize=(13, 13), sharex=True,
                              gridspec_kw={"height_ratios": [2, 2.5, 1.5, 1.5, 1.5]})
    fig.suptitle("Posterior-Based Pre-Transition Instability Detection\n"
                 "Latent Micro-Regimes in Limit Order Books (v3)",
                 fontsize=13, y=1.01, fontweight="bold")

    # ── Panel 1: Spread + true regime shading ──
    ax = axes[0]
    for k, c in regime_colors.items():
        ax.fill_between(t_ax, 0, spread.max()*1.1,
                        where=Z_true[:t_end] == k, color=c, alpha=0.55,
                        label=f"Regime {k}")
    ax.plot(t_ax, spread, lw=0.6, color="#1A1A2E")
    ax.set_ylabel("Bid-Ask Spread")
    ax.legend(loc="upper right", fontsize=8, frameon=False, ncol=3)

    # ── Panel 2: Composite score + signals ──
    ax = axes[1]
    sc = score[:t_end]
    thresh = np.percentile(score, SIGNAL_PCT)
    ax.plot(t_ax, sc, lw=0.8, color="#444444", alpha=0.85, label="Composite score")
    ax.axhline(thresh, color="#FF8800", lw=1.2, ls="--",
               label=f"{SIGNAL_PCT}th pct threshold")
    ax.fill_between(t_ax, thresh, sc, where=sc > thresh,
                    color=PALETTE["Model"], alpha=0.18)
    ax.vlines(tau_vis, sc.min(), sc.max(),
              color=PALETTE["Model"], lw=1.0, alpha=0.7, label="Signal τ (model)")
    ax.vlines(sigma_vis, sc.min(), sc.max(),
              color=PALETTE["Imbalance"], lw=0.6, ls=":", alpha=0.4, label="Stress event σ")
    ax.set_ylabel("Instability Score")
    ax.legend(loc="upper right", fontsize=8, frameon=False, ncol=2)

    # ── Panel 3: Entropy ──
    ax = axes[2]
    ax.plot(t_ax, H[:t_end], lw=0.7, color="#6A3D9A", alpha=0.85)
    ax.set_ylabel("Entropy H_t")

    # ── Panel 4: Uncertainty + Transition Intensity ──
    ax = axes[3]
    ax2 = ax.twinx()
    ax.plot(t_ax, U[:t_end],  lw=0.7, color="#1F78B4", alpha=0.9, label="Uncertainty U_t")
    ax2.plot(t_ax, TI[:t_end], lw=0.7, color="#33A02C", alpha=0.6, label="Trans. Intensity TI_t")
    ax.set_ylabel("Uncertainty U_t", color="#1F78B4")
    ax2.set_ylabel("TI_t", color="#33A02C")
    lines, labels = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines + lines2, labels + labels2, fontsize=8, frameon=False, loc="upper right")

    # ── Panel 5: Pre-stress posterior ──
    ax = axes[4]
    # Recompute PS for display
    posterior   = None  # computed via score pipeline;
# ... [TRUNCATED FILE CONTENT]
```


==================================================


## [2/3] Repository: OrderBook-rs (`PHASE4-QUANT-120`)
- **Full Name**: `PHASE4-QUANT-120_joaquinbejar__OrderBook-rs`
- **Description**: A high-performance, thread-safe limit order book implementation written in Rust. This project provides a comprehensive order matching engine designed for low-latency trading systems, with a focus on concurrent access patterns and lock-free data structures.
- **GitHub Stars**: 530
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
[![Dual License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![Crates.io](https://img.shields.io/crates/v/orderbook-rs.svg)](https://crates.io/crates/orderbook-rs)
[![Downloads](https://img.shields.io/crates/d/orderbook-rs.svg)](https://crates.io/crates/orderbook-rs)
[![Stars](https://img.shields.io/github/stars/joaquinbejar/OrderBook-rs.svg)](https://github.com/joaquinbejar/OrderBook-rs/stargazers)
[![Issues](https://img.shields.io/github/issues/joaquinbejar/OrderBook-rs.svg)](https://github.com/joaquinbejar/OrderBook-rs/issues)
[![PRs](https://img.shields.io/github/issues-pr/joaquinbejar/OrderBook-rs.svg)](https://github.com/joaquinbejar/OrderBook-rs/pulls)

[![Build Status](https://img.shields.io/github/actions/workflow/status/joaquinbejar/OrderBook-rs/build.yml)](https://github.com/joaquinbejar/OrderBook-rs/actions)
[![Coverage](https://img.shields.io/codecov/c/github/joaquinbejar/OrderBook-rs)](https://codecov.io/gh/joaquinbejar/OrderBook-rs)
[![Dependencies](https://img.shields.io/librariesio/github/joaquinbejar/OrderBook-rs)](https://libraries.io/github/joaquinbejar/OrderBook-rs)
[![Documentation](https://img.shields.io/badge/docs-latest-blue.svg)](https://docs.rs/orderbook-rs)



## High-Performance Lock-Free Order Book Engine

A high-performance, thread-safe limit order book implementation written in Rust. This project provides a comprehensive order matching engine designed for low-latency trading systems, with a focus on concurrent access patterns and lock-free data structures.

### Key Features

- **Lock-Free Architecture**: Built using atomics and lock-free data structures to minimize contention and maximize throughput in high-frequency trading scenarios.

- **Multiple Order Types**: Support for various order types including standard limit orders, iceberg orders, post-only, fill-or-kill, immediate-or-cancel, good-till-date, trailing stop, pegged, market-to-limit, and reserve orders with custom replenishment logic.

- **Thread-Safe Price Levels**: Each price level can be independently and concurrently modified by multiple threads without blocking.

- **Advanced Order Matching**: Efficient matching algorithm for both market and limit orders, correctly handling complex order types and partial fills.

- **Performance Metrics**: Built-in statistics tracking for benchmarking and monitoring system performance.

- **Memory Efficient**: Designed to scale to millions of orders with minimal memory overhead.

### Design Goals

This order book engine is built with the following design principles:

1. **Correctness**: Ensure that all operations maintain the integrity of the order book, even under high concurrency.
2. **Performance**: Optimize for low latency and high throughput in both write-heavy and read-heavy workloads.
3. **Scalability**: Support for millions of orders and thousands of price levels without degradation.
4. **Flexibility**: Easily extendable to support additional order types and matching algorithms.

### Use Cases

- **Trading Systems**: Core component for building trading systems and exchanges
- **Market Simulation**: Tool for back-testing trading strategies with realistic market dynamics
- **Research**: Platform for studying market microstructure and order flow
- **Educational**: Reference implementation for understanding modern exchange architecture

### What's New in Version 0.13.0

#### v0.13.0 — the public API hands out no level handles (#228); exclusive submit gate under STP (#225); replay re-executes coded submit rejections (#224)

- **Breaking (semver-minor under 0.x): `OrderBook::get_bids` and
  `OrderBook::get_asks` are removed (#228).** Both cloned the book's live
  `Arc<PriceLevel>` handles into a `DashMap`, and `PriceLevel` exposes
  `add_order`, `update_order` and `match_order` publicly, so a caller
  holding one could mutate a price level behind the submit gate, the
  `order_locations` / user-order indices, the risk state, self-trade
  prevention, the kill switch, the order-state tracker and the trade /
  book-change listeners. Deprecating them would have left the bypass
  reachable, so they are gone and 0.13.0 is the release boundary for
  breaking changes. Migrate to the read-only APIs, which return values
  rather than handles: `create_snapshot(depth)` for a full snapshot of
  every level and order; `levels_with_cumulative_depth`,
  `levels_until_depth`, `levels_in_range` and `find_level` for `LevelInfo`
  views; `order_count_at_price`, `get_orders_at_price`, `get_all_orders`
  and `total_depth_at_levels` for per-price and per-book order data;
  `best_bid` / `best_ask` for the top of book. Every level mutation now
  goes through `OrderBook`.
- **Breaking (semver-minor under 0.x): the level iterators' `new`
  constructors are crate-private (#228).**
  `LevelsWithCumulativeDepth::new`, `LevelsUntilDepth::new` and
  `LevelsInRange::new` each take a reference to the book's live price-level
  map, and with `get_bids` / `get_asks` gone no public API yields one. The
  iterator types stay public; obtain them from
  `OrderBook::levels_with_cumulative_depth`, `levels_until_depth` and
  `levels_in_range`.
- **Self-trade prevention holds under concurrent same-user admission
  (#225).** An STP-relevant submit decided a price level's `STPAction`
  from a queue snapshot and then filled that level in a second operation,
  both under the *shared* side of the submit gate — so a concurrent
  same-user admission could land between the two and be filled by the very
  sweep the scan was protecting. STP-relevant submits and the
  cancel-then-add modify variants whose re-add can match (`UpdatePrice`,
  `UpdatePriceAndQuantity`, `Replace`) now take the **exclusive** side, so
  the scan and the fill it authorises observe the same queue. Cost: on an
  STP book every identified submit except post-only, and every
  matching-capable re-price, is serialized. `STPMode::None` books,
  post-only submits, `UpdateQuantity` and `Cancel` keep the shared, fully
  concurrent path. With no level handles left to bypass it (#228), the
  gate now covers every mutation.
- **`SequencerResult::RejectedWithCode { reason, code, may_have_mutated,
  stp_mode }`.** `add_order` emits real fills and *then* returns `Err`
  for an IOC's unfillable remainder and for a taker STP cancels after
  non-self fills; `ReplayEngine` skipped every rejected event, so replay
  rebuilt liquidity the live book had consumed. Producers now opt in by
  recording the typed outcome — `SequencerResult::from(&error)` fills
  all four fields — and replay decides by the recorded code: a submit
  rejected under a code replay can reproduce from the book state and
  `ReplayBookConfig` is re-executed and must fail the same way again,
  while codes whose trigger lives outside the config (kill switch, risk
  limits, `Other`) are skipped rather than re-executed, because a
  rejection that never touched the book is reproduced by doing nothing.
  `last_applied_seq` / the applied count / the progress callback follow
  what was **dispatched**, so a re-executed rejection advances them.
- **The two facts the reject code cannot carry.** `may_have_mutated`
  flags the errors the engine can return after changing the book,
  including the residual-admission `PriceLevelError` that maps to
  `RejectReason::Other(0)`; a flagged submit is re-executed whatever its
  code says, so that rejection no longer replays as a no-op that
  resurrects consumed liquidity. `stp_mode` records the mode that
  decided a self-trade-prevention rejection, and replay refuses a
  mismatched `ReplayBookConfig`.
- **`ReplayError::OutcomeMismatch { sequence_num, recorded, actual }`**
  aborts replay when a re-executed rejection succeeds or fails under a
  different code than the journal recorded;
  **`ReplayError::StpModeMismatch { sequence_num, recorded, actual }`**
  aborts it when a journaled STP rejection was decided under a different
  `STPMode` than the replay book uses.
- **Migration.** The string-only `SequencerResult::Rejected` keeps its
  historical skip, so a journal written with it keeps the pre-existing
  gap for traded-then-rejected submits; switch producers to
  `RejectedWithCode`. Journals carrying the new variant cannot be
  decoded by older readers (existing journals decode unchanged, as for
  `MarketOrderByAmount`). **Limitations:** only the reject code is
  reconciled, never the error's details or the fills behind it, so a
  discrepancy confined to them can go undetected — `snapshots_match`
  (directly, or via `ReplayEngine::verify`) is the check that catches a
  diverged book, and `replay_from` performs none. The `stp_mode` guard
  only fires on journals that recorded an STP rejection.
  **Breaking (semver-minor under 0.x):** `ReplayError` gained two
  variants, so exhaustive matches need new arms; 0.13.0 is the release
  boundary for them together with the #228 removal. No snapshot format
  change.
- **Reserve orders are lot-size validated per tranche and on their
  replenishment transfer (#226).** A `ReserveOrder` used to be checked on
  its **total** only, so a 15 visible / 5 hidden reserve was admitted to a
  lot-10 book while the identical iceberg was rejected. It now takes the
  iceberg's per-tranche rule and, additionally, validates the capped
  quantity replenishment transfers from hidden into the visible tranche —
  `min(replenish_amount.unwrap_or(DEFAULT_RESERVE_REPLENISH_AMOUNT),
  hidden)`, checked while `hidden > 0` and `auto_replenish` is on.
  Admission is strictly tighter: a shape previously admitted on its total
  is now rejected with `InvalidLotSize`, carrying the offending tranche or
  transfer.
- **A reserve residual follows `auto_replenish` (#230).** The
  residual-resting helper behind `OrderQuantity::set_total_remaining`
  refreshed an emptied visible tranche from `replenish_amount` alone,
  ignoring `auto_replenish`, falling back to a refresh of zero (which
  could rest a zero-visible order) and never consulting
  `replenish_threshold`. It now applies `pricelevel`'s rule: with
  automatic replenishment on and hidden left, a visible tranche below
  `max(replenish_threshold, 1)` grows by the explicit amount or
  `DEFAULT_RESERVE_REPLENISH_AMOUNT`, capped by hidden; with it off the
  residual does not rest at all and its hidden remainder is discarded,
  mirroring the removal of a depleted non-auto maker. A 10 visible / 20
  hidden reserve with `replenish_amount = Some(10)` and no automatic
  replenishment, filled for 10, used to rest 10 / 10 and now ends as
  `Filled { filled_quantity: 10 }`; the same order with automatic
  replenishment and a threshold of 5, filled for 8, used to rest 2 / 20
  and now rests 12 / 10. The discard needs the visible tranche to be
  **exhausted**: with automatic replenishment off, a 10 / 20 reserve
  filled for 5 still rests 5 / 20. An explicit `replenish_amount` is the
  transfer, added to whatever visible quantity survived, not a target
  display size. The accounting rule is
  `submitted = executed + resting (visible + hidden) + discarded`, and
  discarded quantity is never counted as executed. A discard emits an
  `INFO` trace and, under the `metrics` feature, the new
  `orderbook_reserve_discards_total` /
  `orderbook_reserve_hidden_discarded_total` counters, carrying a `path`
  field so the aggressive taker and the removed maker report the same
  discard the same way; the returned order handle carries both tranches
  at zero. Because the three
  cancel-then-add modify variants re-add the order as a taker, a
  validate-first pre-check now rejects a re-price that would exhaust such
  a reserve's visible tranche with the new
  `OrderBookError::ReserveResidualWouldBeDiscarded` **before** the
  original is cancelled, so **a re-price of such a reserve cannot destroy
  the order it modifies**: the exclusive guard covers the lookup, the
  validation, the cancel and the re-add, so the dry run is exact. That
  is the scope of the guarantee; it is not a claim about every possible
  modification failure. Crossing into depth smaller than the visible tranche, a
  non-crossing re-price and a projected full fill are all allowed
  through. The error carries both the projected `hidden_quantity` and the
  `discarded_quantity` that would actually be destroyed. `RejectReason`
  gains the matching wire code 14; both enums are `#[non_exhaustive]`.
  In a book that **holds** such a reserve, every sweep now takes the
  **exclusive** submit gate in every `STPMode` — matching-capable
  submits, cancel-then-add re-prices and the match-only entry points
  alike, plus the admission of the first one — so nothing can cancel,
  admit or replace an order inside a sweep's capture window: the sweep
  cannot consume a maker it never captured, nor report a captured maker
  after a cancel freed its id. Cancels and mass cancels keep the shared
  side. Those books serialize their sweeps; books holding none are
  unchanged.
- **A non-replenishing reserve must display a positive visible tranche
  (#230).** A `ReserveOrder` with `auto_replenish == false`,
  `visible_quantity == 0` and `hidden_quantity > 0` used to rest as a
  ghost: no visible depth, and `pricelevel` removes it without a trade,
  stranding the whole hidden tranche, on the first taker to reach the
  level. Since #221 a zero quantity on `UpdatePriceAndQuantity` /
  `Replace` could drive a healthy resting reserve into that shape too;
  `UpdateQuantity` with a zero quantity cannot, because it is a removal
  taken before the validator runs (#223, below). `validate_order_shape`
  now rejects it with the new `OrderBookError::ZeroVisibleTranche`,
  covering `add_order`,
  every modify projection and snapshot restore; a rejected modify leaves
  the original resting and a rejected restore leaves the book untouched.
  The rule is that shape **only**: a zero-visible iceberg draws its whole
  hidden tranche into visible on match, and a zero-visible
  auto-replenishing reserve refreshes and re-queues, so both execute and
  stay admissible. Single-tranche kinds are unaffected. Maps to the
  existing `RejectReason::InvalidQuantity`.
- **`OrderUpdate::UpdateQuantity` with a zero quantity cancels the order
  (#223).** A zero `new_quantity` was accepted and applied as a resize:
  `pricelevel` keeps a non-growing total in place, so the maker rested at
  zero depth, held `best_bid` / `best_ask` on a level with nothing behind
  it and was later dropped by a sweep with no trade and no cancel event,
  leaking its `order_locations` entry — `cancel_order` then returned
  `Ok(None)` while re-adding the id reported `DuplicateOrderId`. The arm
  now routes to the same `UserRequested` cancel `OrderBook::cancel_order`
  performs, so the level-change event, the `Cancelled { UserRequested }`
  transition, the per-account risk release, the location / user-index
  untrack and the empty-level removal happen in lockstep. **A zero
  requested quantity is a removal, not a resize:** it cancels the
  *entire* order, hidden depth of an iceberg or reserve included (a
  nonzero `new_quantity` still resizes only the visible tranche), and it
  runs neither the projected-order validator nor the modify-aware risk
  check, so neither a configured `min_order_size` nor a risk limit vetoes
  it. The kill switch still refuses it, as it refuses every modify. The
  removal semantic is `UpdateQuantity`'s alone: a zero quantity on
  `Replace` / `UpdatePriceAndQuantity` re-adds through validate-first
  (#230 above). Compatibility: a journal recorded before this change that
  contains a zero `UpdateQuantity` replays to the new outcome, so the
  replayed book legitimately differs from the one the original run
  produced.
- **Reserve `UpdatePriceAndQuantity` honours the requested visible
  quantity (#221).** `OrderQuantity::set_quantity` read a reserve's
  argument as a **total** target and only ever reduced, so a requested
  increase was silently dropped (a 30 / 70 reserve asked to move to 80
  ended at 10 / 70) and a decrease was drawn across both tranches. It now
  sets the **visible** tranche and leaves hidden untouched for both
  two-tranche kinds, matching `UpdateQuantity`, `Replace` and the upstream
  `pricelevel` contract.
- **`CancelTaker` and `CancelBoth` fire only on a same-user maker the
  taker can reach (#222).** Both arms used to cancel unconditionally once
  a same-user maker rested at a crossed level, even when the non-self
  depth queued ahead of it already satisfied the taker. A client saw
  `SelfTradePrevented` on an order that had in fact filled, and
  `CancelBoth` destroyed a maker the sweep never touched — silently on
  the market paths, which drop the taker-cancelled flag and return `Ok`.
  The arms now execute against the non-self depth first and cancel only
  if the taker could still execute at that price afterwards.
  `STPMode::CancelMaker` is deliberately unchanged: it still cancels every
  same-user order at a level the sweep touches, since it never destroys
  the taker. The modify pre-check `check_modify_stp_self_cross` follows
  the same per-level rule and sizes the pre-match with `pricelevel`'s
  authoritative dry run rather than the counted visible depth, so it
  cannot admit a re-price the sweep would then kill after the original
  was cancelled.
- **A quote-notional sell walks past a bid it cannot afford (#222).** A
  zero per-level quantity cap ended the whole sweep. That is right for a
  base-quantity budget, whose cap ignores the level price, and for a
  notional buy, which walks asks ascending so the cap only shrinks. It
  was wrong for a notional sell, which walks bids descending: a budget
  too small at one bid can fund a whole lot at a cheaper one. Selling 150
  into bids of 100, 75 and 50 executed one unit instead of two. The sell
  walk now skips the unaffordable level and stops only on a spent budget,
  an exhausted side, or a remainder below one lot — the point at which no
  price could fund a lot. It may therefore visit every level on the bid
  side; each skipped level costs one division and mutates nothing.

### What's New in Version 0.12.0

#### v0.12.0 — pricelevel 0.9 hardening bump; upsize demotion survives snapshot restore (#205)

- **`pricelevel` 0.8.4 → 0.9.1.** Major upstream hardening release: level
  admission validates before mutating (duplicate id, counter capacity,
  price/side topology), PostOnly / fill-or-kill decisions are atomic with
  the sweep, execution statistics are torn-read-safe, and level snapshots
  materialize orders in queue-consumption order. 0.9.1 fixes the
  `MatchResult` bincode round-trip (PriceLevel#135), keeping the
  `bincode` feature's trade-event round-trip intact.
- **The upsize queue-priority demotion now survives a snapshot
  round-trip (#205).** Restoring a snapshot rebuilds each level's queue
  exactly as matching would consume it, so an order demoted by a quantity
  increase keeps its back-of-queue position after
  `restore_from_snapshot_package`. Locked in by a proptest regression
  (`tests/unit/props_quantity_update_priority.rs`). Snapshots captured
  with pricelevel < 0.9 restore demoted orders at their old
  `(timestamp, seq)` position — re-snapshot to pin the corrected order.
- **Breaking (semver-minor under 0.x):** `get_bt_bids` / `get_bt_asks`
  now return `Result<BTreeMap<u128, PriceLevel>, OrderBookError>`
  (snapshot-to-level conversion is validating and fallible upstream), and
  the re-exported pricelevel surface changed —
  `PriceLevel::add_order` returns `Result`, `matchable_quantity` takes
  the taker id, `PriceLevelError` gained `DuplicateOrderId`.
- **Atomic PostOnly / multi-level FOK (#209).** PostOnly submits thread
  `TakerKind::PostOnly` into every per-level match, making it
  structurally impossible for a post-only order to take liquidity under
  any interleaving; fill-or-kill submits hold a new book-level submit
  gate exclusively across feasibility + sweep, so multi-level
  all-or-nothing can no longer partially execute against concurrent
  cancels. Other mutating entry points take the gate's uncontended read
  side; the matching core stays lock-free. Full 0.11.0 → 0.12.0 HDR
  tail-latency comparison in `BENCH.md`: every scenario's median is
  unchanged by this release's book-level work; the one median shift
  (`stp_sweep`, from the pricelevel 0.9 hardening) is documented there
  with its bisection.
- **Atomic, observable mutation failures (#211).** `UpdateQuantity` is
  validate-first (projected tick / lot / min-max / representability /
  risk before touching the level), propagates upstream
  `PriceLevelError`s instead of returning `Ok(None)`, and updates risk
  counters on success; a taker whose residual cannot rest is rejected
  before the sweep trades; a failed racy admission cleans up any empty
  level it created.
- **Two-tranche quantity conservation (#210).** An aggressive iceberg's
  residual rests with exactly the unmatched total distributed across
  tranches (`visible = min(display, remainder)`, rest hidden) instead of
  inflating the book, and a `visible + hidden` overflow is rejected at
  admission with the new typed `OrderBookError::QuantityOverflow`
  before any trade or mutation. Conservation
  (`executed + resting == submitted`) is property-tested.
- **`snapshots_match` compares full maker state and FIFO (#208).** The
  replay oracle now checks every level's order vector in
  queue-consumption order (ids, variants, users, quantities,
  timestamps, TIF, type-specific fields) and the deterministic
  statistics counters including `stats_degraded`; only the wall-time
  statistics aggregates (`first_arrival_time`, `last_execution_time`,
  `sum_waiting_time` — see the `snapshots_match` docs for why each is
  inherently divergent) and the capture timestamp stay excluded.
  Contract tightening: aggregate-equal books with reversed FIFO or
  different maker identity no longer certify as replay-equal.
- **Failure-atomic snapshot restore (#207).** `restore_from_snapshot` and
  `restore_from_snapshot_package` validate every level (and reject
  cross-level duplicate order ids with `DuplicateOrderId`) against
  off-book structures before clearing the live book, so a failed restore
  leaves the pre-restore state — orders, indices, config, risk,
  kill-switch, engine sequence — completely untouched.
- **Snapshot package format v3 (#206).** Pricelevel 0.9 statistics can
  serialize a `stats_degraded` field that 0.8 readers reject, so newly
  written packages are stamped `ORDERBOOK_SNAPSHOT_FORMAT_VERSION = 3`.
  Reads accept `ORDERBOOK_SNAPSHOT_MIN_READ_VERSION (2)..=3` — legacy v2
  packages still restore — while `1` and future versions stay rejected
  with the existing typed error.

### What's New in Version 0.11.0

#### v0.11.0 — replay reproduces the trade-ID stream: namespace in `ReplayBookConfig` (#200)

- **`ReplayBookConfig.trade_id_namespace: Option<Uuid>`.** v0.10.5 (#199)
  made the trade-ID namespace injectable on `OrderBook`, but every
  `ReplayEngine::replay_from*` entry point still built its book with a
  random namespace, so trade IDs produced through the shipped replay API
  were not reproducible. The config now carries the live book's
  namespace and applies it via `OrderBook::set_trade_id_namespace`
  before any journal events are replayed; a `*_with_config` replay under
  an injected `Clock` then reproduces the live trade-ID stream
  byte-identically. `ReplayBookConfig::new` keeps its six structural
  parameters (namespace defaults to `None`) — chain the new
  `with_trade_id_namespace(namespace)` builder to set it. Without a
  namespace the fresh book keeps a random one, as before.
- **Suffix replays with a namespace are rejected.** Applying a
  namespace restarts the trade-ID counter at 0, so a namespace-carrying
  config with `from_sequence != 0` would mint wrong or duplicate IDs;
  the `*_with_config` entry points return the new typed
  `ReplayError::NamespaceRequiresFullReplay` instead. Namespace-free
  suffix replay keeps working.
- **Breaking (semver-minor under 0.x):** `ReplayBookConfig` gained a
  public field, so exhaustive struct literals no longer compile — add
  `trade_id_namespace: None` or use `..Default::default()`; and
  `ReplayError` gained the `NamespaceRequiresFullReplay` variant, so
  exhaustive matches need a new arm.
  `ReplayBookConfig::new(...)` callers are unaffected. No journal or
  snapshot format change, no `ORDERBOOK_SNAPSHOT_FORMAT_VERSION` bump.

### What's New in Version 0.10.5

#### v0.10.5 — injectable trade-ID namespace (#199)

- **`OrderBook::set_trade_id_namespace(&mut self, namespace: Uuid)`.**
  Every constructor used to mint the trade-ID namespace internally with
  `Uuid::new_v4()`, so trade IDs differed between a live run and its
  replay even with an injected `Clock` and an identical command stream —
  the namespace was the only entropy left in the trade-ID stream
  (`pricelevel::UuidGenerator` is UUID v5 over namespace + counter).
  The new setter, symmetric with `set_clock`
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `src/utils/tests/mod.rs`
```python
mod time;
```

#### File: `benches/simple/mod.rs`
```python
pub mod basic;
```

#### File: `rust-toolchain.toml`
```python
[toolchain]
channel = "stable"
```

#### File: `src/utils/mod.rs`
```python
mod time;

mod tests;

pub use time::current_time_millis;

#[cfg(feature = "alloc-counters")]
pub mod counting_allocator;

#[cfg(feature = "alloc-counters")]
pub use counting_allocator::{AllocSnapshot, CountingAllocator};
```

#### File: `tests/unit/common/mod.rs`
```python
//! Shared test helpers for `orderbook-rs` integration tests.
//!
//! Kept intentionally thin — add new sub-modules here as future proptest
//! issues (#57 byte-identical replay widening, #52 engine_seq monotonicity,
//! etc.) need shared machinery.

pub mod strategies;
```

#### File: `tests/metrics/mod.rs`
```python
//! Standalone integration-test binary for the optional `metrics`
//! feature (issue #60). Lives in its own crate test entry point so
//! the global `metrics` recorder isn't perturbed by the broader
//! integration suite under `tests/unit/`.

#[cfg(feature = "metrics")]
mod metrics_tests;
```


==================================================


## [3/3] Repository: Limit-Order-Book (`PHASE4-QUANT-125`)
- **Full Name**: `PHASE4-QUANT-125_brprojects__Limit-Order-Book`
- **Description**: High-performance limit order book engine with C++ core and Python SDK. Processes 20M+ msgs/sec with µs latency. Supports real crypto/equity data replay, spread/imbalance/impact analytics, and backtesting of VWAP, TWAP, POV, and market-making strategies with reproducible PnL and risk metrics.
- **GitHub Stars**: 85
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Limit Order Book

This Limit Order Book is developed in `C++` from scratch and able to handle over 1,400,000 TPS (transactions per second), including Market, Limit, Stop and Stop Limit orders. 

Performance testing of the order book was also quite a challenging task as it required getting order data for testing, performing the testing to collect latency statistics, and finally analysing and visualising the collected data. All functionality testing was completed thorough a set of unit tests and integration tests using `GoogleTest`.

## Background

### Matching Engine

<img src="./figures/exchange.png" alt="Exchange Diagram" width="500"/>


The matching engine is the core component of trading systems such as stock exchanges. It serves as the intersection where buyers' and sellers' interests meet, enabling trades through order matching. The matching engine maintains a limit order book, which consists of all orders that have not yet been matched. The matching process for trading instruments is inherently sequential. While requests from traders or brokers can be processed concurrently before entering a single queue in the requests pipeline, the sequential nature of the matching process makes the matching engine the throughput bottleneck of the exchange. Consequently, the number of requests an exchange can handle per second is constrained by the throughput of the matching engine and order book, thus explaining the desire for a low latency system. Additionally, the exchange is responsible for disseminating market data, including trade executions and order book updates, to the traders.

The matching engine uses a `FIFO` (First In, First Out) and `Price Priority` algorithm to determine the execution order of entries in the limit order book.

### Order Types

This limit order book supports all common order types usually available in trading systems. This includes:
- Market Order - Orders to buy or sell at the best market price.
- Limit Order (Add, Modify & Cancel) - Orders to buy or sell at the defined limit price and that does not produce trades instantly.
- Market Limit Order - Limit orders that cross the limit order book and produces trades.
- Stop Order (Add, Modify & Cancel) - Orders that are converted into a Market order when the current market price crosses their stop price. 
- Stop Limit Order (Add, Modify & Cancel) - Orders that are converted into a Limit order when the current market price crosses their stop price. 

## Project Tree

```
Limit_Order_Book/
├── Limit_Order_Book/   *files that make up Limit Order Book
│ ├── Book.cpp
│ ├── Book.hpp
│ ├── Limit.cpp
│ ├── Limit.hpp
│ ├── Order.cpp
│ └── Order.hpp
├── Generate_Orders/    *files to generate sample order data
│ ├── GenerateOrders.cpp
│ ├── GenerateOrders.hpp
│ ├── initialOrders.txt
│ └── orders.txt (removed because file size too large)
├── Process_Orders/     *files to process sample order data
│ ├── OrderPipeline.cpp
│ ├── OrderPipeline.hpp
│ ├── data_visualisation.py
│ └── order_processing_times.csv
├── test/               *unit tests
│ ├── CMakeLists.txt
│ ├── ExampleOrdersTests.cpp
│ └── LimitOrderBookTests.cpp
├── figures/
├── googletest/
├── main.cpp
├── .gitignore
├── CMakeLists.txt
└── README.md
```

## Architecture

<img src="./figures/architecture.png" alt="Architecture" width="800"/>

```cpp
Order
    int idNumber;
    bool buyOrSell;
    int shares;
    int limit;
    Order *nextOrder;
    Order *prevOrder;
    Limit *parentLimit;

Limit  // representing a single limit price
    int limitPrice;
    int size;
    int totalVolume;
    Limit *parent;
    Limit *leftChild;
    Limit *rightChild;
    Order *headOrder;
    Order *tailOrder;

Book
    Limit *buyTree;
    Limit *sellTree;
    Limit *lowestSell;
    Limit *highestBuy;
    Limit *stopBuyTree;
    Limit *stopSellTree;
    Limit *lowestStopBuy;
    Limit *highestStopSell;
```

The idea is to implement a binary tree of `Limit` objects sorted by `limitPrice`, each containing a doubly linked list of `Order` objects. Each side of the book, the buy limits and the sell limits, should be in separate trees. This structure ensures that the inside of the book corresponds to the end of the buy limit tree and the beginning of the sell limit tree. Pointers to the `highestBuy` and `lowestSell` allow for quick retrieval of relevant orders during order matching.

Each order is also stored in a map keyed by `idNumber`, and each limit is stored in a map keyed by `limitPrice`. Buy and sell limits can share the same hash map, as they will be at opposite ends of the table (apart from orders that cross). Additionally, two more binary trees and a map keyed by `stopPrice` are required to store the buy and sell stop and stop-limit orders, with corresponding pointers to the `lowestStopBuy` and `highestStopSell`. All stop and stop-limit orders at a given node in these binary trees are executed if an order is executed at or beyond the node's stop price.

With this structure, you can efficiently implement the following key operations:

- Add Order – O(log M) for the first order at a limit, O(1) for all others, where M is the number of price Limits (generally << N the number of orders).
- Cancel Order – O(1)
- Modify Order – O(1)
- Execute – O(1)
- GetVolumeAtLimit – O(1)
- GetBestBid/Offer – O(1)

The binary trees are AVL trees, ensuring they remain balanced. This is crucial because market conditions frequently involve removing orders from one side of the tree while adding them to the other. To maintain O(1) performance for `GetBestBid/Offer`, it is important to update `lowestSell`/`highestBuy` in O(1) time when a limit is added or deleted, which necessitates that each Limit object has a pointer to its parent (`Limit *parent`).

Assumptions:
- Order shares are greater than 0.
- Limit and stop prices are greater than 0.
- Order ID numbers are unique.

## Testing & Performance


### Testing Data

To conduct testing, we need appropriate data. I developed a data generator that produces requests for the matching engine based on statistical models, using a slightly modified version of the limit order book itself. The test data sample consists of 5,000,000 requests, starting with an initial 11,000 orders to populate the limit order book. Order prices follow a normal distribution centered at 300 with a standard deviation of 50. Initially, all buy orders are below 300, and all sell orders are above 300, but the center of the book shifts according to the generated data.

The average number of active limit orders for the test data is 10,000, and the average number of active stop or stop-limit orders is 1,000. The proportions of the different types of orders are illustrated in the pie chart below.

<img src="./figures/OrderTypes.png" alt="OrderTypes" width="500"/>

### Latency Results

To measure throughput, I recorded the timestamps for each request as it entered the matching engine and once the matching engine had finished all resulting operations. The latency for processing a single request was calculated as the difference between the two timestamps. I conducted the test on an Intel i5-12450H (2.00 GHz) processor.

<img src="./figures/LatencyHistogram.png" alt="Order Latency Histogram" width="600"/>

Above is a histogram illustrating the latencies for all 5 million orders. The average latency is 713ns per order, resulting in around 1.4 million orders per second.

<img src="./figures/OrderTypeLatencies.png" alt="Latency by Order Type" width="600"/>

The next figure shows the mean latency for different order types that did not result in trades (i.e., not market or market limit orders). The error bars represent the 15th to 85th percentiles of orders. Canceling orders was the quickest, averaging 400ns, while modifying and adding orders took slightly longer, around 700ns. Interestingly, actions involving stop limit orders took slightly longer, and modifying stop and stop limit orders exhibited larger variance.

<img src="./figures/ExecutedOrders.png" alt="Executed Orders" width="600"/>

The figure above shows how latency was affected by the number of trades resulting from a market or market limit order. A total of 845,242 trades were executed during the test. For each data point, the mean latency for that number of executed trades was calculated. The data stops following a consistent trend at higher numbers of executed trades due to fewer data points. There is a clear positive correlation between latency and the number of trades executed, showing that for each additional trade, latency increases by approximately 440ns. Only values with over 5 data points were used to limit the influence of random variation (this is also true for the remaining two other graphs).

<img src="./figures/AVLTreeBalances.png" alt="Latency by AVL Tree Balances" width="600"/>

Another key factor affecting latency was the number of AVL tree rebalances required after each order. This occurred when a limit/stop/stop limit order was added at a new price level, an order was canceled leaving the price level empty, or, most commonly, when a market or market limit order triggered multiple stop orders. Over the test, there were 252,504 AVL tree rebalances. The figure above shows that each tree rebalance significantly increased latency, averaging 2500ns per additional tree rebalance.

<img src="./figures/3D.png" alt="3D Plot" width="600"/>

Since the number of executed orders and AVL tree rebalances are linked, as more trades being executed trigger more tree rebalances, it is important to plot both factors in one graph to determine which factor most contributes to increasing latency. The figure above, shows that more trades being executed does correlate to move AVL tree rebalances, due to no data in the bottom left and top right quadrants, and that both factors isolated do in fact increase latency. However, AVL tree rebalances have a more significant impact on latency, with each extra rebalance clearly increasing latency.

### Conclusion

This limit order book can handle over 1.4 million orders per second by utilizing an architecture focused on efficient data structures to support high-frequency trading (`HFT`). The results suggest that the number of orders per second could be further increased by reducing the number of required AVL tree rebalances. Additionally, using a faster CPU should also significantly improve performance.

## References

[How to Build a Fast Limit Order Book - wkselph](https://web.archive.org/web/20110219163448/http://howtohft.wordpress.com/2011/02/15/how-to-build-a-fast-limit-order-book/)

[Millions of Orders per Second Matching Engine Testing - Alex Zus](https://habr.com/en/articles/581170/)

### Core Implementation Code & Architecture
#### File: `Limit_Order_Book/Order.hpp`
```python
#ifndef ORDER_HPP
#define ORDER_HPP

class Limit;

class Order {
private:
    int idNumber;
    bool buyOrSell;
    int shares;
    int limit;
    Order *nextOrder;
    Order *prevOrder;
    Limit *parentLimit;

    friend class Limit;
public:
    Order(int _idNumber, bool _buyOrSell, int _shares, int _limit);

    int getShares() const;
    int getOrderId() const;
    bool getBuyOrSell() const;
    int getLimit() const;
    Limit* getParentLimit() const;

    void partiallyFillOrder(int orderedShares);
    void cancel();
    void execute();
    void modifyOrder(int newShares, int newLimit);
    void setShares(int newShares);

    void print() const;
};

#endif
```

#### File: `Generate_Orders/GenerateOrders.hpp`
```python
#ifndef GENERATEORDERS_HPP
#define GENERATEORDERS_HPP

#include <random>
#include <fstream>

class Book;

class GenerateOrders {
private:
    Book* book;
    int orderId = 11001;
    std::ofstream file;

    // Seed for random number generation
    std::random_device rd;
    std::mt19937 gen;

    void market();
    void addLimit();
    void cancelLimit();
    void modifyLimit();
    void addLimitMarket();
    void addStop();
    void cancelStop();
    void modifyStop();
    void addStopLimit();
    void cancelStopLimit();
    void modifyStopLimit();

public:
    GenerateOrders(Book* book);
    void createInitialOrders(int numberOfOrders, int centreOfBook);
    void createOrders(int numberOfOrders);
};

#endif
```

#### File: `Limit_Order_Book/Limit.hpp`
```python
#ifndef LIMIT_HPP
#define LIMIT_HPP

class Order;

class Limit {
private:
    int limitPrice;
    int size;
    int totalVolume;
    bool buyOrSell;
    Limit *parent;
    Limit *leftChild;
    Limit *rightChild;
    Order *headOrder;
    Order *tailOrder;

    friend class Order;
public:
    Limit(int _limitPrice, bool _buyOrSell, int _size=0, int _totalVolume=0);
    ~Limit();

    Order* getHeadOrder() const;
    int getLimitPrice() const;
    int getSize() const;
    int getTotalVolume() const;
    bool getBuyOrSell() const;
    Limit* getParent() const;
    Limit* getLeftChild() const;
    Limit* getRightChild() const;
    void setParent(Limit* newParent);
    void setLeftChild(Limit* newLeftChild);
    void setRightChild(Limit* newRightChild);
    void partiallyFillTotalVolume(int orderedShares);

    void append(Order *_order);

    void printForward() const;
    void printBackward() const;
    void print() const;
};

#endif
```

#### File: `Process_Orders/OrderPipeline.hpp`
```python
#ifndef ORDERPIPELINE_HPP
#define ORDERPIPELINE_HPP

#include <string>
#include <unordered_map>
#include <string_view>
#include <sstream>

class Book;

class OrderPipeline {
private:
    Book* book;

    using OrderFunction = void(OrderPipeline::*)(std::istringstream&);
    std::unordered_map<std::string_view, OrderFunction> orderFunctions;

    void processMarketOrder(std::istringstream& iss);
    void processAddLimitOrder(std::istringstream& iss);
    void processCancelLimitOrder(std::istringstream& iss);
    void processModifyLimitOrder(std::istringstream& iss);
    void processAddStopOrder(std::istringstream& iss);
    void processCancelStopOrder(std::istringstream& iss);
    void processModifyStopOrder(std::istringstream& iss);
    void processAddStopLimitOrder(std::istringstream& iss);
    void processCancelStopLimitOrder(std::istringstream& iss);
    void processModifyStopLimitOrder(std::istringstream& iss);

public:
    OrderPipeline(Book* book);
    void processOrdersFromFile(const std::string& filename);
};

#endif
```

#### File: `main.cpp`
```python
#include "./Generate_Orders/GenerateOrders.hpp"
#include "./Process_Orders/OrderPipeline.hpp"
#include "./Limit_Order_Book/Book.hpp"
#include "./Limit_Order_Book/Limit.hpp"
#include "./Limit_Order_Book/Order.hpp"
#include <iostream>
#include <vector>
#include <chrono>

int main() {
    Book* book = new Book();

    OrderPipeline orderPipeline(book);

    // GenerateOrders generateOrders(book);

    // generateOrders.createInitialOrders(10000, 300);

    orderPipeline.processOrdersFromFile("./initialOrders.txt");

    // generateOrders.createOrders(5000000);


    // Start measuring time
    auto start = std::chrono::high_resolution_clock::now();

    orderPipeline.processOrdersFromFile("./Orders.txt");

    // Stop measuring time
    auto stop = std::chrono::high_resolution_clock::now();

    // Calculate the duration
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(stop - start);

    std::cout << "Time taken to process orders: " << duration.count() << " milliseconds" << std::endl;

    delete book;
    return 0;
}
```

#### File: `test/ExampleOrdersTests.cpp`
```python
#include "../Limit_Order_Book/Limit.hpp"
#include "../Limit_Order_Book/Order.hpp"
#include "../Limit_Order_Book/Book.hpp"
#include "../Process_Orders/OrderPipeline.hpp"
#include "../Generate_Orders/GenerateOrders.hpp"

#include <gtest/gtest.h>

struct ExampleOrdersTests: public ::testing::Test
{
    Book* book;
    OrderPipeline* orderPipeline;
    GenerateOrders* generateOrders;

    virtual void SetUp() override{
        book = new Book();
        orderPipeline = new OrderPipeline(book);
        generateOrders = new GenerateOrders(book);
    }

    virtual void TearDown() override{
        delete generateOrders;
        delete orderPipeline;
        delete book;
    }
};

TEST_F(ExampleOrdersTests, CreateInitialOrdersTest) {
    generateOrders->createInitialOrders(10000, 300);
}

TEST_F(ExampleOrdersTests, ProcessInitialOrdersTest) {
    orderPipeline->processOrdersFromFile("C:/Users/benja/Documents/Limit_order_book/initialOrders.txt");
}

TEST_F(ExampleOrdersTests, CreateOrdersTest) {
    orderPipeline->processOrdersFromFile("C:/Users/benja/Documents/Limit_order_book/initialOrders.txt");
    generateOrders->createOrders(100000);
}
```


==================================================
