# SWC Registry with CWE Categories

This simply meant as a Research tool for bugs found in Solidity Smart Contracts.
## Overview

The Smart Contract Weakness Classification Registry (SWC Registry) is an implementation of the weakness classification scheme proposed in EIP-1470.While investigating relationships between the SWC Registry and lists such as the OWASP Top 10, CWE Top 25 and NIST NVD I noticed that the SWC Registry does utilize CWE categories. This makes it difficult to categorize bugs found.  This app was a quick python project that parses the [SWC Registry](https://smartcontractsecurity.github.io/SWC-registry/) and matches them to their CWE categories. It places this data into a json file.

The [Python SWC Registry Lirary](https://github.com/SmartContractSecurity/SWC-registry-python) is used but as of now the CWE2 Python Library does not offer the same functionality.  The CWE2 data is pulled from the [CWE Comprehensive Categorization for Sofware Assurance Trends](https://cwe.mitre.org/data/definitions/1400.html) is missing reference to the Memebership so this was parsed.

## History

The DASP Top 10 was a project from 2018 that did something similar to this. However, it was not updated and did not include CWE categories. This app is not an attempt to update the DASP Top 10.  It is simply a tool to help compare the SWC Registry to the [CWE Comprehensive Categorization for Sofware Assurance Trends](https://cwe.mitre.org/data/definitions/1400.html).

The SWC is now considered retired as it is being incorporated into the EEA EthTrust Security Levels. The SWC Registry is still a useful resource for finding vulnerabilities in smart contracts at this point. It is expected that the Version 2 of the EEA EhtTrust Security LEvels will be release in Q4 2023. At that time we may revisit this project to see if this code can add more value.

## Future Work

- EEA EthTrust Security Levels - The SWC Registry is being incorporated into the EEA EthTrust Security Levels.  This would be a good next step to compare the SWC Registry to the EEA EthTrust Security Levels.
- Incorporating the CWE2 data which includes the OWASP Top 10, CWE Top 24 and NIST NVD Top 25 would be a good next step.  This would allow for a more complete comparison.

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