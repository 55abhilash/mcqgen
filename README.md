# mcqgen

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://www.python.org/downloads/)

Generate MCQs with options and correct answers in JSON Format. Uses GPT.

## Installation

You can install the package using pip:

```bash
pip install mcqgen
```
Make sure you have OpenAI key stored in environment variable `OPENAI_API_KEY`

## Usage

Simply call function `generate_mcqs` as below.
First argument (Topic) is mandatory. 
Default Model (model) is GPT3.5 and default number of questions (no) is 5.

```console
from mcqgen import mcqgen
gen = mcqgen.MCQGenerator()
data = gen.generate_mcqs('Cricket', model="gpt-3.5-turbo", no=3)
print(data)
```
```
{'questions': [{'question': 'Who holds the record for the highest individual score in Test cricket?', 'options': ['a) Sachin Tendulkar', 'b) Brian Lara', 'c) Don Bradman', 'd) Ricky Ponting'], 'answer': 'b) Brian Lara'}, {'question': 'Which cricketer has scored the most centuries in One Day Internationals (ODIs)?', 'options': ['a) Sachin Tendulkar', 'b) Ricky 
Ponting', 'c) Virat Kohli', 'd) Kumar Sangakkara'], 'answer': 'a) Sachin Tendulkar'}, {'question': 'Who has the best bowling figures in a Test innings?', 'options': ['a) Jim Laker', 'b) Anil Kumble', 'c) Muttiah Muralitharan', 'd) Shaun Pollock'], 'answer': 'a) Jim Laker'}]}

```