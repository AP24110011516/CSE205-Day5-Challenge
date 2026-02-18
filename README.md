# CSE205-Day5-Challenge
A Python program developed for the CSE205 Day-5 Code2Xplore challenge to analyze emergency resource requests. It classifies demands, applies personalized filtering using PLI, and generates a final dispatch report using basic Python concepts.

# Emergency Resource Dispatch Analyzer

- Title: Emergency Resource Dispatch Analyzer

## Description
This project analyzes emergency resource requests during disaster drills. It classifies requests into different categories and applies a personalized filtering rule using PLI to generate a final dispatch report.

## Personalization Details
- Name Length (L): ______
- PLI Value: ______
- Applied Rule: Rule A / Rule B / Rule C

## Classification Rules
| Request Value | Category        |
|---------------|-----------------|
| < 0           | Invalid         |
| 0             | No Demand       |
| 1 – 20        | Low Demand      |
| 21 – 50       | Moderate Demand |
| > 50          | High Demand     |

## PLI Rules
- PLI = 0 → Rule A (Remove Low Demand)
- PLI = 1 → Rule B (Remove High Demand)
- PLI = 2 → Rule C (Keep Only Moderate Demand)

## Features
- Uses lists and for loops
- No built-in functions
- No external libraries
- Manual data processing
- Personalized filtering logic

## How to Run
1. Clone the repository
2. Open the file `dispatch_analyzer.py`
3. Run using:

