# Introduction to Git and GitHub

This repository contains simple example calculators used to demonstrate
basic Git and GitHub workflows.

## Files

- `compound_interest.py` — Python script to compute compound amount and compound interest.
- `simple-interest.sh` — Bash script to compute simple interest.

## Usage

Simple interest (Bash):

```
$ bash simple-interest.sh
Enter the principal: 1000
Enter rate of interest per year: 5
Enter time period in years: 2
The simple interest is: 100.00
```

Compound interest (Python):

```
$ python3 -c "from compound_interest import compound_amount; print('{:.2f}'.format(compound_amount(1000,2,5)))"
1102.50
```

## License

This project is licensed under the Apache License 2.0. See the `LICENSE` file.

© 2022 IBM Developer Skills Network
