[Context: "Find PubMed articles related to the query 'hemoglobin', use elink
to find related articles, then use elink again to find proteins"]

```bash
esearch -db pubmed -query "hemoglobin" | \
elink -related | \
elink -target protein
```

Craps out for reason I have yet to diagnose correctly. Might have to go
[Biostars](https://www.biostars.org) for this one.
