# main.py
#
# Copyright 2024 Emi
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import random
import argparse

# Set up command-line argument parsing
parser = argparse.ArgumentParser(description="Generate a random number within a specified range and interval.")
parser.add_argument('-min', type=int, help="Minimum value (inclusive).")
parser.add_argument('-max', type=int, help="Maximum value (inclusive).")
parser.add_argument('-interval', type=int, help="Count interval.")

args = parser.parse_args()

# Ask the user for the range if not provided as an argument
if args.min is not None:
    min_value = args.min
else:
    min_value = int(input("Enter the minimum value: "))

if args.max is not None:
    max_value = args.max
else:
    max_value = int(input("Enter the maximum value: "))

# Ask the user for the count interval if not provided as an argument
if args.interval is not None:
    interval = args.interval
else:
    interval = int(input("Enter the count interval: "))

# Generate a list of numbers in the specified range and interval
number_list = list(range(min_value, max_value + 1, interval))

# Print the generated list for debugging
# print(f"Generated list: {number_list}")

# Select a random number from the list
random_number = random.choice(number_list)

# Print the random number
print(f"Random number: {random_number}")

