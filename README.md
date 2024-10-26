# DIE (Dice Interactive Emulator)

## Overview

**DIE** is a simple Python program that allows users to generate a random number from a specified range and interval. The user inputs a minimum value, a maximum value, and a count interval. The program generates a list of numbers based on these parameters and selects one at random, simulating the roll of a die.

## Features

- User-defined range for generating numbers
- Customizable interval for generating numbers within the range
- Random selection of a number from the generated list, simulating a dice roll

## Requirements

- Python 3.x

## Installation

1. Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone this repository or download the `main.py` file directly.
   
   ```bash
   git clone https://github.com/emi-rose/DIE
   cd DIE/src 
   ```

3. Run the program using the following command:
   
   ```bash
   python main.py
   ```

## Usage

1. When prompted, enter the **minimum value** for the range.
2. Next, enter the **maximum value** for the range.
3. Finally, specify the **count interval**. This determines the step size for generating numbers in the range.
4. The program will output a randomly selected number from the generated list, simulating the result of rolling a die.
### Example

```
Enter the minimum value: 1
Enter the maximum value: 100
Enter the count interval: 10
Random number: 30
```

## Quick Rolls /w Arguments
```bash
python main.py -min 0 -max 20 -interval 1
```

## License

This program is free software: you can redistribute it and/or modify it under the terms of the [GNU General Public License](https://www.gnu.org/licenses/) as published by the Free Software Foundation, either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful, but **WITHOUT ANY WARRANTY**; without even the implied warranty of merchantability or fitness for a particular purpose. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

## Author

Copyright 2024 Emi
