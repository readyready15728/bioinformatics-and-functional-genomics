[Context: listing the genes on human chromosome 16 including their start and
stop positions]

```bash
esearch -db gene -query "16[chr] AND human[orgn] AND alive[prop]" | \
esummary | \
xtract -pattern DocumentSummary -element Id -block LocationHistType -match "AssemblyAccVer:GCF_000001405.25" -pfx "\n" -element AnnotationRelease,ChrAccVer,ChrStart,ChrStop > chromosome-16.txt
```

Goes off without a hitch. Not much to say here.
