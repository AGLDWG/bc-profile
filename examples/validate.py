import sys
from pathlib import Path
import re
from pyshacl import validate
from rdflib import Graph

sg = Graph().parse("../validator.ttl")
eg = Graph().parse("_dcceew.ttl")

if len(sys.argv) == 1:
    for f in sorted(list(Path(".").glob("*.ttl"))):
        if re.match(r"^([0-9]{2}).*\.ttl$", str(f.name)):
            dg = Graph().parse(f)
            v = validate(dg + eg, shacl_graph=sg)
            print(f"{f.name}: {v[0]}")
else:
    dg = Graph().parse(sys.argv[1])
    v = validate(dg + eg, shacl_graph=sg)
    if v[0]:
        print("True")
    else:
        print(v[2])