[Context: installing edirect CLI utilities]

The instructions in the book are outdated. Go figure! Instead I got the right
idea [here](https://www.ncbi.nlm.nih.gov/books/NBK179288/), namely:

```bash
sh -c "$(curl -fsSL ftp://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh)"
```

The install script offered to add `$HOME/edirect` to my `.bashrc` but since I
wasn't using bash I declined and did that step manually.
