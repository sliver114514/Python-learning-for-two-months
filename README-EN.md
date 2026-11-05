# Python Learning Journey: 44 Projects in 2 Months

##  Table of Contents

- [About This Repository](#about-this-repository)
- [Environment Setup](#environment-setup)
- [Project Difficulty Ratings](#project-difficulty-ratings)
- [Self-Practice Area](#self-practice-area)
- [Data Notes](#data-notes)
- [How to Use](#how-to-use)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

Starting from zero, I completed 44 Python projects in roughly two months. Every file contains highly detailed annotations. Beginner-level projects have relatively concise notes, while Intermediate-level projects are annotated in greater detail.

> **Study Tip**: Beginners are strongly encouraged to turn off code auto-completion while practicing — it helps you better understand the underlying logic of the code.

This repository is designed to help Python learners at all levels, starting from beginner-friendly projects and gradually progressing to more advanced ones. Working through the projects requires some foundation: at minimum, you should be able to understand fairly simple code and keywords. If you can see it through to the end, you will thank yourself. If you make it all the way, you have already accomplished something remarkable.

##  About This Repository

This is a complete record of my journey from zero Python knowledge to being able to independently build practical tools.

**Total projects:** 44
**Beginner projects:** 32
**Intermediate projects:** 12

The projects are built on classic programming exercises, with my own understanding and improvements added:
- Detailed annotations for every line of code
- Refactoring of selected code
- Added input validation and exception handling
- Reorganized file structure by difficulty and topic

##  Environment Setup

- Make sure Python `3.6` or later is installed on your machine (`3.12` or later is recommended).
- Make sure you have an IDE or an environment in which you can write and run a Python interpreter.

##  How to Use

```bash
git clone https://github.com/sliver114514/Python-learning-for-two-months.git
cd Python-learning-for-two-months
```


> [!TIP]
> I use PyCharm for development, which is extremely beginner-friendly. If you already have some experience, you can use Visual Studio Code (VS Code). It is fast, efficient, and offers a rich set of extensions and customization options.


##  Project Difficulty Ratings

| Project | Category | Difficulty |
| :--- | :--- | :--- |
| [Calculator](#1-calculator) | Beginner | 1.5/10 |
| [Number Guessing Game](#2-number-guessing-game) | Beginner | 2.0/10 |
| [Password Generator](#3-password-generator) | Beginner | 2.5/10 |
| [Tip Calculator](#4-tip-calculator) | Beginner | 1.5/10 |
| [Temperature Converter](#5-temperature-converter) | Beginner | 1.5/10 |
| [Palindrome Checker](#6-palindrome-checker) | Beginner | 1.5/10 |
| [Word Counter](#7-word-counter) | Beginner | 2.0/10 |
| [Text Encryption](#8-text-encryption) | Beginner | 2.5/10 |
| [Countdown Timer](#9-countdown-timer) | Beginner | 2.5/10 |
| [Rock Paper Scissors](#10-rock-paper-scissors) | Beginner | 2.5/10 |
| [Mad Libs Generator](#11-mad-libs-generator) | Beginner | 2.0/10 |
| [Dice Roll Simulator](#12-dice-roll-simulator) | Beginner | 1.5/10 |
| [Word Guessing Game](#13-word-guessing-game) | Beginner | 3.5/10 |
| [Address Book](#14-address-book) | Beginner | 4.0/10 |
| [Pomodoro Timer](#15-pomodoro-timer) | Beginner | 3.0/10 |
| [Budget Tracker](#16-budget-tracker) | Beginner | 4.5/10 |
| [File Organizer](#17-file-organizer) | Beginner | 3.5/10 |
| [Text Reverser](#18-text-reverser) | Beginner | 1.0/10 |
| [Simple Quiz Game](#19-simple-quiz-game) | Beginner | 2.5/10 |
| [Prime Number Generator](#20-prime-number-generator) | Beginner | 2.5/10 |
| [Fibonacci Sequence](#21-fibonacci-sequence) | Beginner | 2.0/10 |
| [Email Splitter](#22-email-splitter) | Beginner | 1.5/10 |
| [BMI Calculator](#23-bmi-calculator) | Beginner | 1.5/10 |
| [Currency Converter](#24-currency-converter) | Beginner | 2.5/10 |
| [Task Tracker](#25-task-tracker) | Beginner | 3.0/10 |
| [Unit Converter](#26-unit-converter) | Beginner | 2.5/10 |
| [Leap Year Checker](#27-leap-year-checker) | Beginner | 1.5/10 |
| [Odd/Even Checker](#28-oddeven-checker) | Beginner | 0.5/10 |
| [Multiplication Table Generator](#29-multiplication-table-generator) | Beginner | 0.5/10 |
| [Simple Interest Calculator](#30-simple-interest-calculator) | Beginner | 0.5/10 |
| [Anagram Checker](#31-anagram-checker) | Beginner | 1.0/10 |
| [Acronym Generator](#32-acronym-generator) | Beginner | 1.0/10 |
| [Tic-Tac-Toe](#1-tic-tac-toe) | Intermediate | 6.0/10 |
| [Text Adventure Game](#2-text-adventure-game) | Intermediate | 5.5/10 |
| [Sudoku Solver](#3-sudoku-solver) | Intermediate | 8.5/10 |
| [Basic Sorting Algorithms](#4-basic-sorting-algorithms) | Intermediate | 6.5/10 |
| [Sieve of Eratosthenes](#5-sieve-of-eratosthenes) | Intermediate | 5.0/10 |
| [Basic Caesar Cipher](#6-basic-caesar-cipher) | Intermediate | 4.5/10 |
| [Bank Account Simulator (OOP)](#7-bank-account-simulator-oop) | Intermediate | 5.5/10 |
| [File Metadata Extractor](#8-file-metadata-extractor) | Intermediate | 5.0/10 |
| [CSV to JSON Converter](#9-csv-to-json-converter) | Intermediate | 4.5/10 |
| [Fractal Generator](#10-fractal-generator) | Intermediate | 6.5/10 |
| [File Explorer](#11-file-explorer) | Intermediate | 6.5/10 |
| [File Viewer](#12-file-viewer) | Intermediate | 4.5/10 |

The repository is continuously updated, and some projects are still being uploaded.

##  Self-Practice Area

In addition to completing the 44 core projects, I recorded my extra learning outcomes in the `Self-Practice/` folder:

| Folder | Content | Description |
| :--- | :--- | :--- |
| `modified/` | Remixed versions | Core logic modified on top of the original projects, exploring different implementation approaches |
| `optimized/` | Optimized versions | Refactored original code with added exception handling, input validation, and modern idioms |
| `exercises/` | Miscellaneous exercises | Small exercises and experimental code written along the way |

**Why keep these separate?**
Because learning to program is not just about “typing it out once” — what matters more is “changing it, testing it, playing with it.”
This folder records my growth from “following the tutorial” to “rewriting it myself.”

## Some code generates data, which is stored in the data/ directory

Note: The code for every project includes detailed annotations. Some annotations were AI-assisted, which helped me better understand the code logic.

##  License

This project is open-sourced under the [MIT License](LICENSE).

You are free to use, copy, modify, merge, publish, and distribute the code in this project, including for commercial purposes.
The only requirement is that you retain the original author's copyright notice and license notice when redistributing.

In short: **anyone may use, modify, and distribute it without prior permission.**

##  Acknowledgements

Most of the exercise ideas in this project are inspired by [Infinitode/Python-Projects](https://github.com/Infinitode/Python-Projects).

Thanks to the original author for the excellent project framework, which helped me grow quickly through hands-on practice.

**Building on the original author's work, my independent contributions include:**
1. In 50 days starting from zero, I hand-typed, debugged, and got all 44 projects running.
2. Added highly detailed annotations to every line of code, so Chinese-speaking beginners can follow along.
3. Refactored parts of the code using more modern idioms.
4. Added crash-prevention mechanisms such as input validation and exception handling.
5. Reorganized the file structure and difficulty rating table according to the learning progression.

Anyone is welcome to fork, modify, or submit a Pull Request or Issue.
If you have a better approach or more detailed annotations, your contributions are welcome.
If this repository has helped you, please consider giving it a ⭐ Star so more Chinese-speaking beginners can find it.
