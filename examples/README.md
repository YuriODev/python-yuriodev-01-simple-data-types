# Examples 👨🏼‍💻

Here are some examples to get you started.

**Covered topics:** 
- **Numbers** (Integers, Floating-Point Numbers, Type Conversion, Mathematical Functions, Operator Precedence)

## Example 1
**Problem:** A natural number is given. Find the digit that stands in the tens place in the decimal notation of the number (the second digit, counting from the end of the record).
 

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 1981   | 8       |
| 2   | 158    | 5       |
| 3   | 5      | 0       |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input number from the user
number = int(input("Enter a natural number: "))

# Get ten place digit using integer division and modulo
tens_place = (number // 10) % 10
hundreds_place = (number // 100) % 10

# Print the result using f-string
print(f"The tens place digit of {number} is {tens_place}")
print(f"The hundreds place digit of {number} is {hundreds_place}")

```
</details>

## Example 2

**Problem:** A positive three-digit integer is entered. Find the sum of the digits of the number.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 153    | 9       |
| 2   | 123    | 6       |
| 3   | 565    | 16      |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input number from the user
number = int(input("Enter a three-digit number: "))

# Extract each digit
hundreds = number // 100

# -- Explanation --
# To extract the first digit in a number you need to divide by 10^(n-1) 
# where n is the number of digits in the number

tens = (number // 10) % 10
ones = number % 10

# Calculate the sum of the digits
sum_of_digits = hundreds + tens + ones

# Print the result using f-string
print(f"The sum of the digits of {number} is {sum_of_digits}")

```
</details>


## Example 3

**Problem:** Tatiana goes to bed at midnight every day and recently learned that the optimal time for her sleep is `t` minutes. Tatiana wants to set an alarm clock to ring exactly `t` minutes after midnight, but for this it is necessary to specify the alarm time in hours and minutes. Help Tatiana determine what time to set the alarm for. Hours and minutes in the program's output should be on separate lines.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 450    | 7<br>30   |
| 2   | 1240   | 20<br>40  |
| 3   | 150    | 2<br>30   |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input number from the user
t = int(input("Enter the number of minutes after midnight: "))

# Calculate the hours and minutes
hours = t // 60
minutes = t % 60

# Print the result using f-string
print(f"{hours}\n{minutes}")

```
</details>


## Example 4

**Problem:** Helen learned that she needs `t` minutes to sleep. Unlike Tatiana, Helen goes to bed after midnight at `h` hours and `m` minutes. Help Helen determine what time she should set the alarm to ring exactly `t` minutes after she goes to bed. The values of `t`, `h` and `m` are entered on separate lines. It is guaranteed that Helen should wake up on the same day she fell asleep. The program should output the time to set the alarm: hours on the first line, minutes on the second line.

| No. | Inputs     | Outputs |
| --- | ---------- | ------- |
| 1   | 430<br>1<br>40 | 8<br>50   |
| 2   | 300<br>23<br>0 | 5<br>0    |
| 3   | 1440<br>0<br>0 | 0<br>0    |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input numbers from the user
t = int(input("Enter the number of minutes Helen needs to sleep: "))
h = int(input("Enter the hour Helen goes to bed: "))
m = int(input("Enter the minute Helen goes to bed: "))

# Calculate the total minutes from midnight when Helen should wake up
total_minutes = h * 60 + m + t

# Convert the total minutes to hours and minutes
wake_up_hour = (total_minutes // 60) % 24
wake_up_minute = total_minutes % 60

# Print the hours and minutes on separate lines
print(wake_up_hour)
print(wake_up_minute)

```
</details>


## Example 5

**Problem:** Write a program to convert the entered seconds into days, hours, minutes and seconds.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 6785   | 0 day(s), 1 hour(s), 53 minute(s), 5 second(s) |
| 2   | 456789 | 5 day(s), 6 hour(s), 53 minute(s), 9 second(s) |
| 3   | 86401  | 1 day(s), 0 hour(s), 0 minute(s), 1 second(s)  |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Define constants for the number of seconds in a day, hour, and minute
SECONDS_IN_A_DAY = 24 * 60 * 60
SECONDS_IN_AN_HOUR = 60 * 60
SECONDS_IN_A_MINUTE = 60

# Read the input number from the user
s = int(input("Enter the number of seconds: "))

# Calculate the number of days
days = s // SECONDS_IN_A_DAY
s %= SECONDS_IN_A_DAY

# Calculate the number of hours
hours = s // SECONDS_IN_AN_HOUR
s %= SECONDS_IN_AN_HOUR

# Calculate the number of minutes
minutes = s // SECONDS_IN_A_MINUTE
s %= SECONDS_IN_A_MINUTE

# The remaining seconds
seconds = s

# Print the result
print(f"{days} day(s), {hours} hour(s), {minutes} minute(s), {seconds} second(s)")

```
</details>


## Example 6

**Problem:** Given an integer `n` - the number of minutes that have passed since midnight - how many hours and minutes are displayed on a 24-hour digital clock? The program should print two numbers: the number of hours (from 0 to 23) and the number of minutes (from 0 to 59).

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 150    | 2, 30   |
| 2   | 25     | 0, 25   |
| 3   | 440    | 7, 20   |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Define constants for the number of minutes in an hour and the number of hours in a day
MINUTES_IN_AN_HOUR = 60
HOURS_IN_A_DAY = 24

# Read the input number from the user
n = int(input("Enter the number of minutes that have passed since midnight: "))

# Calculate the number of hours
hours = (n // MINUTES_IN_AN_HOUR) % HOURS_IN_A_DAY

# Calculate the number of minutes
minutes = n % MINUTES_IN_AN_HOUR

# Print the result
print(f"{hours}, {minutes}")

```
</details>


## Example 7

**Problem:** An integer `n` is entered, it is necessary to "cut off" the last `k` digits from it. For example, when `n` = 123456 and `k` = 3 the answer should be 123.

| No. | Inputs     | Outputs |
| --- | ---------- | ------- |
| 1   | 456712<br>2 | 4567 |
| 2   | 123456<br>3 | 123  |
| 3   | 123456<br>6 | 0    |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input numbers from the user
n = int(input("Enter the integer: "))
k = int(input("Enter the number of digits to cut off: "))

# Calculate the divisor
divisor = 10**k

# Calculate the result
result = n // divisor

# Print the result
print(result)

```
</details>


## Example 8

**Problem:** A book costs `a` pounds and `b` pennies. Determine how many pounds and pennies need to be paid for `n` books. The values are entered by the user in the order `a`, `b`, `n` on separate lines, and the amount to pay in two lines: the number of pounds on the first line and the number of pennies on the second line, respectively.

| No. | Inputs     | Outputs |
| --- | ---------- | ------- |
| 1   | 10<br>15<br>2 | 20<br>30 |
| 2   | 5<br>50<br>4  | 22<br>0  |
| 3   | 1<br>99<br>1  | 1<br>99  |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input numbers from the user
a = int(input("Enter the cost of a book in pounds: "))
b = int(input("Enter the cost of a book in pennies: "))
n = int(input("Enter the number of books: "))

# Calculate the total cost in pennies
total_cost_in_pennies = (a * 100 + b) * n

# Calculate the number of pounds to be paid
pounds = total_cost_in_pennies // 100

# Calculate the number of pennies to be paid
pennies = total_cost_in_pennies % 100

# Print the number of pounds and pennies to be paid
print(pounds)
print(pennies)

```
</details>


## Example 9

**Problem:** Write a program to sum the first `n` natural numbers. The result must be an integer.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 100 | 5050 |
| 2   | 15  | 120  |
| 3   | 99  | 4950 |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input number from the user
n = int(input("Enter the number of natural numbers to sum: "))

# Calculate the sum of the first n natural numbers
sum_of_numbers = n * (n + 1) // 2

# Print the result
print(sum_of_numbers)

```
</details>


## Example 10

**Problem:** Get the reverse (in reverse order) entry of the three-digit number `n` entered by the user.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 184 | 481 |
| 2   | 123 | 321 |
| 3   | 567 | 765 |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input number from the user
n = int(input("Enter a three-digit number: "))

# Extract the hundreds, tens, and units digits
hundreds = n // 100
tens = (n // 10) % 10
units = n % 10

# Construct the reversed number
reversed_n = units * 100 + tens * 10 + hundreds

# Print the result
print(reversed_n)

```
</details>


**Notes:** All the examples above are solved using Python. You can find the solutions in the [examples](./examples) folder. Covered with explanations and comments, these examples will help you understand the practical implementation of the concepts covered in this module. Python tests are also included to verify the correctness of the solutions.
