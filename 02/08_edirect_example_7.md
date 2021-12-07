[Context: finding the taxonomic family name and BLAST division for a set of
organisms]

The book uses a `bash` script. While that's initially more convenient in the
short run, my impression is that Python has taken the bioinformatics world by
storm and, generally speaking, Python is more maintainable than are shell
scripts. So I rewrote `taxonomy.sh` as [`taxonomy.py`](taxonomy.py).
