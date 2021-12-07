[Context: searching for FASTA entries pertaining to a given protein in the
Protein database]

I had to modify this one. The original query was against the protein
hemoglobin. Here's the output of `esearch -db protein -query 'hemoglobin'`:

```xml
<ENTREZ_DIRECT>
  <Db>protein</Db>
  <WebEnv>MCID_61aea850a2907a7f13162db0</WebEnv>
  <QueryKey>1</QueryKey>
  <Count>248580</Count>
  <Step>1</Step>
</ENTREZ_DIRECT>
```

Pay close attention to the `<Count>` tag. Yeah, no thanks. I have no idea
whether `efetch` was rate-limited back in 2015 when this book was written, but
it certainly seems to be now. Granted, that may not have mattered on the
author's system, assuming the inter-process communication in the full
suggested pipeline `esearch -db protein -query "hemoglobin" | efetch -format
fasta | head -6` has `head` wrapping up as soon as those first six lines
showed up. That wasn't the case on my system though, and I wanted to ensure
that the process exited successfully.

In addition, the FASTA results I was getting were of variable line length, so
a fixed number of lines supplied to `head` when I don't know what I'm going to
get makes no sense. I found a much less-known protein and output *all* the
results into [snap-25.txt](snap-25.txt). (SNAP-25 is some sort of neural
protein.) Here was the invocation:

```bash
esearch -db protein -query 'SNAP-25' | efetch -format fasta > snap-25.txt
```
