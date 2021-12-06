I was instructed to run:

```bash
esearch -db pubmed -query 'bioinformatics [MAJR] AND software [TIAB]' | efetch -format xml | xtract -pattern PubmedArticle -block Author -sep ' ' -tab '\n' -element LastName,Initials | sort-uniq-count-rank
```

It went off without a hitch after I remembered that the conjunction in the
`esearch` query needs to be capitalized. However, the output was very
unwieldy, at well over 26,000 lines as measured by `wc -l`. I then used `head
-n 100` to obtain a greatly reduced and more usable output:

```
84      Wang Y
69      Wang J
64      Zhang Y
56      Zhang J
53      Wang X
53      Zhang X
52      Liu X
50      Liu Y
48      Li Y
47      Liu J
45      Li J
44      Chen Y
42      Wang L
41      Li L
40      Aebersold R
40      Li X
35      Zhang H
34      Chen J
34      Deutsch EW
34      Li H
34      Martens L
33      Liu S
32      Chen L
31      Chen X
31      Zhang L
30      Hermjakob H
30      Jones AR
29      Li C
29      Wang H
29      Wang Z
27      Liu Z
27      Zhang W
27      Zhao Y
25      Li M
25      Li S
25      Wu J
25      Yang X
25      Zhao X
24      Xu Y
24      Yang J
24      Zhang B
24      Zhang Z
23      Hucka M
23      Liu H
23      Wang C
22      Eisenacher M
22      Kim S
22      Maccoss MJ
22      Sun H
22      Vizcaíno JA
22      Wu Y
21      Kohlbacher O
21      Lisacek F
21      Moritz RL
21      Smith RD
21      Yang Y
20      Li W
20      Zhang Q
19      Goesmann A
19      Yates JR
19      Zhang P
18      Barsnes H
18      Levander F
18      Li F
18      Liu C
18      Li Z
18      Perez-Riverol Y
18      Wang D
18      Wang T
18      Xu D
18      Yang H
18      Zhang C
18      Zhu Y
17      Bergmann FT
17      Liu L
17      Sauro HM
17      Tang H
17      Zhang M
16      Cox J
16      Huang X
16      Wang M
16      Wang R
16      Wang W
16      Zhang F
16      Zhou J
15      Chen Z
15      Dräger A
15      Karp PD
15      Le Novère N
15      Liu G
15      Liu Q
15      Mendes P
15      Nesvizhskii AI
15      Sahle S
15      Smith LM
15      Song J
15      Vaudel M
15      Wang K
15      Wang Q
15      Wu X
```
