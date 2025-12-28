# kg_context_example_code.py

KG_CONTEXT_EXAMPLE_CODE = """
from mcnptoolspro import Ptrac
from sys import stdout

# Open PTRAC file - format (BIN_PTRAC, ASC_PTRAC, HDF5_PTRAC) is auto-detected by EVA sandbox
# You can use any mode here, it will be replaced automatically with the correct one
p = Ptrac("<PTRAC_PATH_PLACEHOLDER>", Ptrac.BIN_PTRAC)

# initialize counter
cnt = 0

# read histories in batches of 10000
hists = p.ReadHistories(10000)
while hists:

    # loop over all histories
    for h in hists:
        # loop over all events in the history
        for e in range(h.GetNumEvents()):

            event = h.GetEvent(e)

            if event.Type() == Ptrac.BNK:
                cnt += 1

                stdout.write(
                    "{:13d}{:13.5e}{:13.5e}{:13.5e}{:13.5e}\\n".format(
                        cnt,
                        event.Get(Ptrac.X),
                        event.Get(Ptrac.Y),
                        event.Get(Ptrac.Z),
                        event.Get(Ptrac.ENERGY),
                    )
                )

    hists = p.ReadHistories(10000)
"""
