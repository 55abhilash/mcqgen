# mcqgen

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://www.python.org/downloads/)

Generate MCQs with options and correct answers in JSON Format.

## Installation

You can install the package using pip:

```bash
pip install mcqgen
```
Make sure you have OpenAI key stored in environment variable `OPENAI_API_KEY`

## Usage

Simply call function `generate_mcqs` as below.
First argument (Topic) is mandatory. Default Model is GPT3.5 and default number of questions is 5
```
from mcqgen import mcqgen
gen = mcqgen.MCQGenerator()
data = gen.generate_mcqs('Topic', model="gpt-3.5-turbo", no=3)
```