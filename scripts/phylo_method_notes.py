#!/usr/bin/env python3
"""
The Neighbor-Joining (NJ) method is a distance-based algorithm that
clusters taxa based on a matrix of pairwise distances. It assumes that the
distances accurately reflect the evolutionary divergence. One limitation is
its sensitivity to long branch attraction, which may result in inaccurate
tree topologies when rates of evolution vary significantly among lineages.

Parsimony analysis seeks the tree that requires the smallest number of
evolutionary changes (mutations). The main assumption is that simpler
evolutionary scenarios (fewer changes) are more likely to be correct.
However, parsimony can be misled by phenomena such as convergent evolution
and long branch attraction, especially when evolutionary rates are highly
variable among branches.
""
