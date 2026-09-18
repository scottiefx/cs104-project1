# Scottie's Fantabulous Deadlock Quiz (that nobody will understand)
> A short one-line tagline for your quiz or questionnaire

## Overview
> This program is a quiz based on the game Deadlock created by Valve. It's been a fixation for me for a while and it's one of the few things I have specialized knowledge in so I decided to base this quiz on it. The users input their answers to the question and try to get to the end without losing too many lives. At the end, their current lives are listed.

## Sample Questions and Responses
> Does the item Toxic Bullets do damage based on current health or max health?
> 1. Current Health (incorrect)
> 2. Max Health (correct)
> How many lanes were on the map before the map rework?
> 1. 3 (incorrect)
> 2. 4 (correct)
> 3. 5 (incorrect)
> When was the last major update (as of September 18th 2026)?
> January (correct)
> March (incorrect)
> June (incorrect)
> How many souls does a tier 4 item cost?
> 3,200 (incorrect)
> 4,800 (incorrect)
> 6,400 (correct)
> Who was the most recently added Hero?
> Graves (incorrect)
> Apollo (correct)
> Celeste (incorrect)

## Variables
> lives (int): determines how many chances the user has to get a question wrong before failure
> answer (int): the answer of the user, forced into an integer position for simplicity
> Qstate (int): The current question the user is on

## Conditional Logic Outline
> FOR EVERY QUESTION:
> Asks the user the question, displays the possible answers, asks for input.
> If user's input is incorrect, display "Incorrect!" and then deduct from their lives.
> If user's input is correct, display "Correct!" and move to next question, increase Qstate by 1.
> If user runs out of lives, display a failure message and end quiz

## How to Run
1. Clone this repo
2. Run `python3 main.py` or `python main.py`

## Demo Video
[DELETE AND REPLACE ME: link to your 5-minute explanation video]
