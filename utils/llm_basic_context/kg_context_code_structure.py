KG_CONTEXT_CODE_STRUCTURE = """
[KG_CONTEXT_CODE_STRUCTURE LLM READY]

# ==== Classes principales ====

Class: Ptrac(PtracEnums)
  - ReadHeader() -> void
  - ReadHistories(num: int) -> List[PtracHistory]
  - ReadHistoriesLegacy(num: int) -> List[PtracHistory]
  - ReadHistory() -> PtracHistory

Class: PtracHistory
  - GetNPS() -> PtracNps
  - GetNumEvents() -> int
  - GetEvent(i: int) -> PtracEvent

Class: PtracEvent
  - Type() -> int         # Enum from PtracEventType
  - BankType() -> int     # Enum from PtracBankType
  - Has(d: int) -> bool   # d = enum from PtracDataType
  - Get(d: int) -> float or int  # depends on d

Class: PtracNps
  - NPS() -> int
  - Cell() -> int
  - Surface() -> int
  - Tally() -> int
  - Value() -> float

Relation: Ptrac.ReadHistories() → List[PtracHistory]
Relation: PtracHistory.GetNPS() → PtracNps
Relation: PtracHistory.GetEvent(i) → PtracEvent
Relation: PtracEvent.Get(d) → value (int or float) dépendant de d ∈ PtracDataType


# ==== Enums et valeurs ====
Class: PtracEnums
  Enum: PtracFormat
    id: BIN_PTRAC, value: 0
    id: ASC_PTRAC, value: 1
    id: HDF5_PTRAC, value: 2

  Enum: PtracEventType
    id: SRC, value: 1000
    id: BNK, value: 2000
    id: SUR, value: 3000
    id: COL, value: 4000
    id: TER, value: 5000
    id: LST, value: 9000

  Enum: PtracBankType
    id: BNK_DXT_TRACK, value: 1
    id: BNK_ERG_TME_SPLIT, value: 2
    id: BNK_WWS_SPLIT, value: 3
    id: BNK_WWC_SPLIT, value: 4
    id: BNK_UNC_TRACK, value: 5
    id: BNK_IMP_SPLIT, value: 6
    id: BNK_N_XN_F, value: 7
    id: BNK_N_XG, value: 8
    id: BNK_FLUORESCENCE, value: 9
    id: BNK_ANNIHILATION, value: 10
    id: BNK_PHOTO_ELECTRON, value: 11
    id: BNK_COMPT_ELECTRON, value: 12
    id: BNK_PAIR_ELECTRON, value: 13
    id: BNK_AUGER_ELECTRON, value: 14
    id: BNK_PAIR_POSITRON, value: 15
    id: BNK_BREMSSTRAHLUNG, value: 16
    id: BNK_KNOCK_ON, value: 17
    id: BNK_K_X_RAY, value: 18
    id: BNK_N_XG_MG, value: 19
    id: BNK_N_XF_MG, value: 20
    id: BNK_N_XN_MG, value: 21
    id: BNK_G_XG_MG, value: 22
    id: BNK_ADJ_SPLIT, value: 23
    id: BNK_WWT_SPLIT, value: 24
    id: BNK_PHOTONUCLEAR, value: 25
    id: BNK_DECAY, value: 26
    id: BNK_NUCLEAR_INT, value: 27
    id: BNK_RECOIL, value: 28
    id: BNK_DXTRAN_ANNIHIL, value: 29
    id: BNK_N_CHARGED_PART, value: 30
    id: BNK_H_CHARGED_PART, value: 31
    id: BNK_N_TO_TABULAR, value: 32
    id: BNK_MODEL_UPDAT1, value: 33
    id: BNK_MODEL_UPDATE, value: 34
    id: BNK_DELAYED_NEUTRON, value: 35
    id: BNK_DELAYED_PHOTON, value: 36
    id: BNK_DELAYED_BETA, value: 37
    id: BNK_DELAYED_ALPHA, value: 38
    id: BNK_DELAYED_POSITRN, value: 39

  Enum: PtracTerminationType
    id: TER_ESCAPE, value: 1
    id: TER_ENERGY_CUTOFF, value: 2
    id: TER_TIME_CUTOFF, value: 3
    id: TER_WEIGHT_WINDOW, value: 4
    id: TER_CELL_IMPORTANCE, value: 5
    id: TER_WEIGHT_CUTOFF, value: 6
    id: TER_ENERGY_IMPORTANCE, value: 7
    id: TER_DXTRAN, value: 8
    id: TER_FORCED_COLLISION, value: 9
    id: TER_EXPONENTIAL_TRANSFORM, value: 10
    id: TER_N_DOWNSCATTERING, value: 11
    id: TER_N_CAPTURE, value: 12
    id: TER_N_N_XN, value: 13
    id: TER_N_FISSION, value: 14
    id: TER_N_NUCLEAR_INTERACTION, value: 15
    id: TER_N_PARTICLE_DECAY, value: 16
    id: TER_N_TABULAR_BOUNDARY, value: 17
    id: TER_P_COMPTON_SCATTER, value: 11
    id: TER_P_CAPTURE, value: 12
    id: TER_P_PAIR_PRODUCTION, value: 13
    id: TER_P_PHOTONUCLEAR, value: 14
    id: TER_E_SCATTER, value: 11
    id: TER_E_BREMSSTRAHLUNG, value: 12
    id: TER_E_INTERACTION_DECAY, value: 13
    id: TER_GENNEUT_NUCLEAR_INTERACTION, value: 11
    id: TER_GENNEUT_ELASTIC_SCATTER, value: 12
    id: TER_GENNEUT_DECAY, value: 13
    id: TER_GENCHAR_MULTIPLE_SCATTER, value: 11
    id: TER_GENCHAR_BREMSSTRAHLUNG, value: 12
    id: TER_GENCHAR_NUCLEAR_INTERACTION, value: 13
    id: TER_GENCHAR_ELASTIC_SCATTER, value: 14
    id: TER_GENCHAR_DECAY, value: 15
    id: TER_GENCHAR_CAPTURE, value: 16
    id: TER_GENCHAR_TABULAR_SAMPLING, value: 17

  Enum: PtracDataType
    id: NPS, value: 1
    id: FIRST_EVENT_TYPE, value: 2
    id: NPSCELL, value: 3
    id: NPSSURFACE, value: 4
    id: TALLY, value: 5
    id: VALUE, value: 6
    id: NEXT_EVENT_TYPE, value: 7
    id: NODE, value: 8
    id: NSR, value: 9
    id: ZAID, value: 10
    id: RXN, value: 11
    id: SURFACE, value: 12
    id: ANGLE, value: 13
    id: TERMINATION_TYPE, value: 14
    id: BRANCH, value: 15
    id: PARTICLE, value: 16
    id: CELL, value: 17
    id: MATERIAL, value: 18
    id: COLLISION_NUMBER, value: 19
    id: X, value: 20
    id: Y, value: 21
    id: Z, value: 22
    id: U, value: 23
    id: V, value: 24
    id: W, value: 25
    id: ENERGY, value: 26
    id: WEIGHT, value: 27
    id: TIME, value: 28
    id: SOURCE_TYPE, value: 29
    id: BANK_TYPE, value: 30


# ==== Dictionnaires (partiels, à compléter si besoin) ====

Dictionary: PtracReactionDict
  id: MT_5, MT_18, MT_101, MT_201, ...

Dictionary: ParticleCodeDict
  id: PARTICLE_1, PARTICLE_2, PARTICLE_3, ...

Dictionary: PtracZAIDDict
  id: NUCLIDE_1H, NUCLIDE_12C, NUCLIDE_235U, ...


"""

