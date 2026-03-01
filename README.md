# CAS502-trevorlines

This repo exists for the CAS 502 project, where we focus on examining entrepreneurial data.

Entrepreneurial Journey in Data

CAS 502 Project — Trevor Lines

Overview
This project analyzes data from entrepreneurs to understand what separates successful ventures from unsuccessful ones. We're building Python scripts to process, classify, and analyze the PSED I & II datasets.

Research Question
What patterns of activity and decision-making distinguish entrepreneurs who successfully launch ventures versus those who don’t?
Dataset
PSED I and PSED II — University of Michigan longitudinal studies tracking entrepreneurs over multiple years through phone survey interviews.
Format: Tabular data with encoded variables (requires codebook translation)
Sample questions: "Have you made your first sale?", "How many people own part of this business?"
Source: ICPSR

Planned Features
Core Functionality

Data Loader — Python module to load PSED files, handle missing values, create analysis-ready dataset

State Classifier — Rule-based system assigning ventures to stages: 
1) nascent-early
2) nascent-active 
3) launched 
4) operating 
5) profitable 
x) disengaged

Movement Calculator — Track stage transitions across survey waves

Extended Goals

- Predictive model for venture success probability
- Pattern identification among successful founders
- Anti-pattern detection for high-risk trajectories

## Author: 

Trevor Lines

## Bug Reporting and Feature Requests

Please open an issue on [github issue page](https://github.com/twlines/CAS502-trevorlines/issues)

Include 
- Description of bug
- How to reproduce
- Expected behavior

## Contributions

1) Fork repository
2) Create a feature branch 
3) Make changes and commit 
4) Push your fork and open a PR

## Installation 

See [INSTALL.md](https://github.com/twlines/CAS502-trevorlines/blob/main/install.md)

## Usage

See [USAGE.md](https://github.com/twlines/CAS502-trevorlines/blob/main/USAGE.md)

## License

See [License](https://github.com/twlines/CAS502-trevorlines/blob/main/LICENSE.md)



Repository Structure
├── data/           # Raw and processed data (gitignored)
├── src/            # Python modules
├── tests/          # Unit tests
└── docs/           # Documentation
