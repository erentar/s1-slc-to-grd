# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
from snapista import Graph
from snapista import Operator
from snapista import TargetBand
from snapista import TargetBandDescriptors

# %%
import os
cwd = os.getcwd()

# %%
g = Graph()
operators = [
    Operator(
        "Read",
        formatName = "SENTINEL-1",
        file=cwd+"/S1A_EW_GRDM_1SDH_20240513T080157_20240513T080301_053850_068B6C_4AB2.zip"
    ),
    Operator(
        "Apply-Orbit-File"
    ),
    Operator(
        "Ellipsoid-Correction-RD"
    ),
    Operator(
        "Reproject",
        crs="EPSG:4326"
    ),
    Operator("Write",
        file="out"
    )
]

for index, operator in enumerate(operators):
    print(f"Adding Operator {operator.operator}")
    if index == 0:            
        source_node_id = None
    else:
        source_node_id = operators[index - 1].operator if isinstance(operators[index - 1], Operator) else operators[index - 1]
    g.add_node(operator, operator.operator, source_node_id)

# %%
g.run()

# %%
g.view()

# %%
