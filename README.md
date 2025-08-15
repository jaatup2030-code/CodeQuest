# CodeQuest — Interactive Coding Skill Trainer

## Overview
CodeQuest is a lightweight, console-based learning tool designed to help beginner programmers master key concepts like variables, conditionals, loops, and functions.  
It provides adaptive exercises, spaced review for retention, and detailed teacher reports that highlight where students excel and where they struggle.

## Features
- Interactive lessons for four core topics:
  - Variables
  - Conditionals
  - Loops
  - Functions
- Adaptive difficulty that adjusts based on student performance.
- Spaced repetition to reinforce past topics.
- Teacher reports that:
  - Summarize each student’s mastery per topic.
  - Identify class-wide weak areas.
  - Track improvement trends over time.
- Local CSV data storage for progress tracking.

## How to Run
**Requirements:**
- Python 3.x installed
- A terminal or console to run the program

**Steps:**
1. Download or clone the repository.
2. Open a terminal in the project folder.
3. Run the command:
   ```bash
   python codequest.py

## Sample Interatcion
Welcome to CodeQuest!
Select your profile or create a new one:
> Create new profile
Enter your name: Alex

Choose a topic:
1. Variables
2. Loops
> 1

Lesson: Variables store values for later use.
Example: x = 5

Question: What will this code print?
x = 3
y = x + 2
print(y)

Your answer: 5
Correct! Points earned: +10

### Sample Teacher Report Output (TO BE IMPROVED)

**Example: Indivdual Student Report**
Student: Alex Rivera
----------------------------------
Topic Mastery:
Variables: 85%  (Improved from 65% last month)
Conditionals: 60%  (Needs review)
Loops: 78%  (Steady)
Functions: 55%  (Lowest mastery)

Strength: Variables
Weakness: Functions
Recommended Focus: Functions & Conditionals
Trend: Overall improving (+10% average over last 4 weeks)

 **Example: Class Summary Report**
Class: Section Carnation - CS2
----------------------------------
Average Mastery:
Variables: 80%
Conditionals: 62%
Loops: 75%
Functions: 58%

Weakest Topic (Class-wide): Functions
Strongest Topic: Variables

Patterns Observed:
- 70% of students show a drop in Function mastery after Week 3.
- Students who struggle with Conditionals often struggle with Loops.

Suggested Teacher Action:
- Conduct review activities for Functions and Conditionals.
- Pair students strong in Loops with those struggling in related topics.

### Contributors

- Atup
- Cuevo
- Escala
