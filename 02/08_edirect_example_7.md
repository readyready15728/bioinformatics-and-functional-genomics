[Context: finding the taxonomic family name and BLAST division for a set of
organisms]

The book uses a `bash` script. While that's initially more convenient in the
short run, my impression is that Python has taken the bioinformatics world by
storm and, generally speaking, Python is more maintainable than are shell
scripts. So I rewrote `taxonomy.sh` as [`taxonomy.py`](taxonomy.py). The
input comes from [`organisms.txt`](organisms.txt) and here's the output:

```
Escherichia coli	Enterobacteriaceae	enterobacteria
Saccharomyces cerevisiae	Saccharomycetaceae	budding yeasts
Arabidopsis thaliana	Brassicaceae	eudicots
Caenorhabditis elegans	Rhabditidae	nematodes
Drosophila melanogaster	Drosophilidae	flies
Danio rerio	Danionidae	bony fishes
Mus musculus	Muridae	rodents
Homo sapiens	Hominidae	primates
```

No idea why but I had to do this outside of `tmux` to preserve the hard tabs
in the output above.
