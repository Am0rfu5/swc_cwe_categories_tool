# SWC Registry with CWE Categories

## Overview

While looking at the relationships between SWC Registry and OWASP Top 10, I noticed that the SWC Registry does not have CWE categories. This makes it difficult to compare the two lists. This app parses the [SWC Registry](https://smartcontractsecurity.github.io/SWC-registry/) and matches them to their CWE categories. It places this data into a json file

## History

The DASP Top 10 was a project from 2018 that did something similar to this. However, it was not updated and did not include CWE categories. This app is not an attempt to update the DASP Top 10.  It is simply a tool to help compare the SWC Registry to the CWE Comprehensive Categoreis of Weaknesses.

The SWC is now considered retired as it is being incorporated into the EEA EthTrust Security Levels. The SWC Registry is still a useful resource for finding vulnerabilities in smart contracts at this point.

## Usage

This was created in VSCode with Docker.  Easy way to run it is with the following command:

```bash
docker-compose up
```

I haven't tried it without Docker, but it should work based on the versioning with the following command using Python:

```bash
python3 app.py
```

## Output

The output is a json file called `swc_cwe_data.json`. 