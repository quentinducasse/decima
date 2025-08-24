KG_CONTEXT_RULES = """
ABSOLUTE RULES:
- NEVER import any mcnptools classes other than: `from mcnptools import Ptrac`.
- NEVER use internal attributes (e.g., m_events, m_type) — use public methods only.
- Use the variable `ptrac_path = '<PTRAC_PATH_PLACEHOLDER>'` as the PTRAC file path (no hardcoded paths).
- Always call `ReadHistories(int)` to load particle histories.
- IMPORTANT: To retrieve the bank type (secondary particle type), DO NOT use the enum `Ptrac.BANK_TYPE` (obsolete).
  Instead, always use the method `event.BankType() -> int` from `Class: PtracEvent`.

---

BEST PRACTICES:
1) Dictionaries such as `PtracReactionDict` (MT_xx), `ParticleCodeDict`, and `PtracZAIDDict` are internal to the KG:
   - NEVER import them.
   - If you use one, access its `value` field, never its `id` (e.g., use `1`, not `PARTICLE_1`).

2) Before any call to `event.Get(...)`, check presence with `event.Has(...)`:
   Correct:
   if event.Has(Ptrac.X):
       x = event.Get(Ptrac.X)

3) ENUM entities of type BNK or TER are always referenced as `Ptrac.<ENUM_NAME>`
   (examples: `Ptrac.BNK_KNOCK_ON`, `Ptrac.TER_E_BREMSSTRAHLUNG`).

---

UNDERSTANDING HISTORIES AND PARTICLES:

Each PTRAC file contains simulation HISTORIES (track histories).
Each history includes one or more PARTICLES. Each particle is represented by a CONSECUTIVE SEQUENCE OF EVENTS:

- It always starts with a SRC or BNK event.
- It always ends with a TER event.

A particle ≠ a single event. One particle produces multiple consecutive events.
Within the same history, you can have one SRC particle followed by several BNK-born secondary particles.

Do not confuse:
  - The number of events (COL, SUR, etc.)
  - The number of particles (each SRC/BNK spawns one particle)
  - The number of histories (top-level simulation entries)

---

TRACING A PARTICLE WITHIN A HISTORY:

To follow a particle’s trajectory:
- Locate a SRC or BNK event.
- Collect all subsequent events that belong to that same particle.
- Stop at the corresponding TER event.

Membership criterion: the events of a particle are contiguous in the list, between the initial SRC/BNK and its final TER.

Each particle therefore follows a unique path:
  [ SRC ] → COL → COL → SUR → … → TER
  [ BNK ] → COL → SUR → COL → … → TER

---

TYPICAL PER-PARTICLE CALCULATIONS (and frequent errors to avoid):

• Deposited energy:
   - Take the energy at the first event (SRC or BNK)
     if event.Type() in (Ptrac.SRC, Ptrac.BNK):
         energy_init = event.Get(Ptrac.ENERGY)
   - Iterate until the corresponding TER
     if event.Type() == Ptrac.TER:
         energy_final = event.Get(Ptrac.ENERGY)
   - Compute: deposited = energy_init - energy_final

• Time of flight:
   - time_start = event.Get(Ptrac.TIME) at SRC or BNK
   - time_end   = event.Get(Ptrac.TIME) at TER
   - Compute: time_of_flight = time_end - time_start

Never:
   - Sum energies over all COL events.
   - Include events from the next particle (anything after the TER).

---

EXPECTED RESPONSE STRUCTURE:
1) A clear, pedagogical natural-language explanation.
2) A Python code block delimited by ```python ... ``` with correct indentation.

Reason step by step before writing code.
"""
