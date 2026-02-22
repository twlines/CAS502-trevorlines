# Usage

## Step 1: Parse the codebook

Creates JSON dictionary to decode the data

```bash
python src/codebook_parser.py
```
Output: data/codebook.json

## Step 2: Load and decode the data 

Loads the decoded data and create a csv

```bash
python src/psed_loader.py
```
Output: data/decoded_psed.csv

## Run Tests

```bash
pytest tests/
```
