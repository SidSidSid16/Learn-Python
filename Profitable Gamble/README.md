# Profitable Gamble
## [Task](https://edabit.com/challenge/SNM5EZ3FePECt2HQn)
Create a function that takes in three arguments (prob, prize, pay) and returns `true` if `prob * prize > pay` otherwise return `false`.

To illustrate, `profitable_gamble(0.2, 50, 9)` should yield `true`, since the net profit is 1 (`0.2 * 50 - 9`), and `1 > 0`.

## Example
`profitable_gamble(0.2, 50, 9) ➞ True`

`profitable_gamble(0.9, 1, 2) ➞ False`

`profitable_gamble(0.9, 3, 2) ➞ True`
