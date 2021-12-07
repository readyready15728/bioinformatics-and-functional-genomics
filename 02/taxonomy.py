#!/usr/bin/env python3

import subprocess
import sys

for line in sys.stdin:
    organism = line.rstrip()

    esearch = subprocess.Popen(['esearch', '-db', 'taxonomy', '-query', f'{organism} [LNGE] AND family [RANK]', '<', '/dev/null'],
                               stdout=subprocess.PIPE)
    efetch = subprocess.Popen(['efetch', '-format', 'docsum'],
                              stdin=esearch.stdout,
                              stdout=subprocess.PIPE)
    xtract = subprocess.Popen(['xtract', '-pattern', 'DocumentSummary', '-lbl', organism, '-element', 'ScientificName', 'Division'],
                              stdin=efetch.stdout,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)

    stdout, stderr = xtract.communicate()

    print(stdout.decode('utf-8').rstrip())
