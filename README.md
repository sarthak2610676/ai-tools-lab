# AI Tools Lab

A Python project demonstrating fundamental programming concepts, sorting algorithms, and reusable utility functions. This project was developed as part of the Artificial Intelligence Tools and Applications Lab.

## Project Description

**AI Tools Lab** contains Python implementations of sorting algorithms and commonly used utility functions. The project demonstrates practical use of GitHub for version control, feature branches, commits, and collaborative development.

### Features

* Bubble Sort implementation
* Palindrome checking
* Word counting
* Celsius-to-Fahrenheit conversion
* Modular and reusable Python functions
* GitHub-based version control

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-tools-lab.git
```

### 2. Navigate to the Project

```bash
cd ai-tools-lab
```

### 3. Verify Python Installation

Make sure Python 3.x is installed:

```bash
python --version
```

No external Python packages are required for the basic project.

## Usage

### Bubble Sort

Run the sorting program:

```bash
python sorting.py
```

Example:

```text
Original list: [64, 34, 25, 12, 22, 11, 90]
Sorted list: [11, 12, 22, 25, 34, 64, 90]
```

### Utility Functions

The `utils.py` module provides reusable functions.

```python
from utils import is_palindrome, count_words, celsius_to_fahrenheit

print(is_palindrome("madam"))
print(count_words("AI tools make coding faster"))
print(celsius_to_fahrenheit(100))
```

Example output:

```text
True
5
212.0
```

## Project Structure

```text
ai-tools-lab/
│
├── hello.py
├── sorting.py
├── utils.py
└── README.md
```

## Contributors

**Sarthak Mahajan**
Class: **CSE3(B)**
Roll No.: **2550910**

## License

This project is licensed under the **MIT License**.

```text
MIT License

Copyright (c) 2026 Sarthak Mahajan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
