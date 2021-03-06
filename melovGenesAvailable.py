#!/usr/bin/env python

"""
A python script to plot gene expression data generated by
Simon Melov, Ph.D.  This utility will use the R-project for
statistical computing to analyze data and generate bar graphs
of gene expression as a function of C. elegans age (in days).
"""

from melovGeneLibrary import *

plotFiles, genes, oligos = getAllPlotFiles()

print "<table name=\"genesAvailable\" >"
geneNames = genes.keys()
geneNames.sort()
for gene in geneNames:
    print "<tr><td>%s</td>" % gene,
    oligos = genes[gene]
    oligos.sort()
    for oligo in oligos:
        # consider changing the format of these outputs (maybe a table?)
        # maybe include the oligo values on each line?
        print "<td><input type=\"checkbox\" name=\"geneset\" class=\"oligo\" value=\"%s\" checked>%s</td>" % (oligo, oligo)
    print "</tr>"
print "</table>"
sys.exit(0)

