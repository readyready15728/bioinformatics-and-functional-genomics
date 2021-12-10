[Context: I'm trying to get a tutorial of a web-based sequence alignment tool
to work]

Apparently blastp used to work differently. The book suggests aligning human
beta globin with myoglobin, which doesn't work with the default parameters
anymore. Switching over to the PAM250 scoring matrix made it succeed.
(BLOSUM50 was also effective.) 
