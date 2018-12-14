#Purpose
The point of this exercise is to take a graph and color it so that no 2 touching nodes have the same color

# How To Play
## Generate a graph
### Full Graph
`python gen_full_graph.py 100`
### Possibly full graph
`python gen_graph.py 14 10` where 14 is the number of nodes and 10 is the number of colors

## Wire up colors
(whichever one you chose)

### Full graph
`python color_graph.py graph-100.json` 

`python verify_coloring graph-100.json colors.json`

### Possibly full graph
`python color_graph.py graph-14-10.json`

`python verify_coloring graph-100.json colors.json` 

If it came out true, the graph has been colored properly (you know, with numbers instead of colors...)
