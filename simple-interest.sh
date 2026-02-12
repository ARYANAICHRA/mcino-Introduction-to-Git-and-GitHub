#!/usr/bin/env bash
# This script calculates simple interest given principal, annual rate of interest and time period in years.
# Do not use this in production. Sample purpose only.

# Author: Upkar Lidder (IBM)
# Additional Authors: <your Github username>

# Input:
# p, principal amount
# t, time period in years
# r, annual rate of interest (percent per year)

# Output:
# simple interest = p * t * r / 100

set -euo pipefail

printf "Enter the principal: "
read p
printf "Enter rate of interest per year: "
read r
printf "Enter time period in years: "
read t

# Use bc for floating point arithmetic and format to 2 decimal places
s=$(printf "%s" "scale=4; $p * $t * $r / 100" | bc -l)
printf "The simple interest is: %.2f\n" "$s"

exit 0
