# Numerology

A Python class to calculate lucky numbers from names or dates of birth using numerology principles.

## Overview

This module applies numerology calculations to generate "lucky numbers" based on name letters or birth dates.

## Features

- 🔢 **Name to Number** — Calculate number from name
- 📅 **Birth Date Number** — Derive number from date of birth
- ✨ **Lucky Number Generation** — Combines calculations

## Installation

```python
from numerology import Numerology
```

## Usage

```python
n = Numerology()

# From name
lucky = n.from_name("John Doe")
print(lucky)  # Returns calculated number

# From date of birth
lucky = n.from_dob("1990-05-15")
print(lucky)
```

## How It Works

Names are converted to numbers using letter-to-number mapping:
- A=1, B=2, C=3... Z=26
- Numbers are summed and reduced to single digit

## Disclaimer

This is for entertainment purposes. Numerology is not a science.

## License

MIT
