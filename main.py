import math

# -------------------------
# Part I: Geometric series
# -------------------------
def part_I():
    # Series: sum_{k=0}^{9} 2*(3/4)^k
    print("Part I: List first 10 terms and sum of  Σ_{k=0}^{9} 2*(3/4)^k")
    terms = []
    total = 0.0

    for k in range(10):
        term = 2 * (3/4) ** k
        terms.append(term)
        total += term

    print("\nFirst 10 terms:")
    for k, term in enumerate(terms):
        print(f"Term {k+1} (k={k}): {term}")

    print(f"\nSum of terms: {total}")


# -------------------------
# Part II: Quadratic solver
# -------------------------
def read_float(prompt):
    # Keeps asking until the user enters a valid real number
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("Invalid input. Please enter a real number (no letters or symbols).")

def part_II():
    print("Part II: Quadratic equation solver for ax^2 + bx + c = 0")
    a = read_float("Enter a: ")
    if a == 0:
        print("a must be a non-zero real number. This is not a quadratic equation.")
        return

    b = read_float("Enter b: ")
    c = read_float("Enter c: ")

    disc = b*b - 4*a*c
    print(f"\nDiscriminant (b^2 - 4ac) = {disc}")

    if disc > 0:
        x1 = (-b + math.sqrt(disc)) / (2*a)
        x2 = (-b - math.sqrt(disc)) / (2*a)
        print("Two real solutions:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif disc == 0:
        x = (-b) / (2*a)
        print("One real solution:")
        print(f"x = {x}")
    else:
        # Complex solutions
        real = (-b) / (2*a)
        imag = math.sqrt(-disc) / (2*a)
        print("Two imaginary (complex) solutions:")
        print(f"x1 = {real} + {imag}i")
        print(f"x2 = {real} - {imag}i")


# -------------------------
# Part III: Base conversions
# -------------------------
def part_III():
    print("Part III: Base conversions (binary <-> decimal, decimal -> octal, decimal -> hex)")
    print("Choose input type:")
    print("1) Decimal")
    print("2) Binary")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        dec_str = input("Enter a decimal integer (base 10): ").strip()
        if not dec_str.lstrip("-").isdigit():
            print("Invalid decimal integer.")
            return
        n = int(dec_str, 10)

        # Output all bases
        if n >= 0:
            binary = format(n, "b")
            octal = format(n, "o")
            hexa = format(n, "X")
        else:
            # For negatives, show sign + converted magnitude
            binary = "-" + format(abs(n), "b")
            octal = "-" + format(abs(n), "o")
            hexa = "-" + format(abs(n), "X")

        print("\nOutput:")
        print(f"Decimal: {n} (base 10)")
        print(f"Binary:  {binary} (base 2)")
        print(f"Octal:   {octal} (base 8)")
        print(f"Hex:     {hexa} (base 16)")

    elif choice == "2":
        bin_str = input("Enter a binary number (base 2): ").strip()
        # Validate binary
        s = bin_str
        if s.startswith("-"):
            s2 = s[1:]
        else:
            s2 = s

        if any(ch not in "01" for ch in s2) or len(s2) == 0:
            print("Invalid binary number.")
            return

        n = int(bin_str, 2)

        # Output all bases
        if n >= 0:
            octal = format(n, "o")
            hexa = format(n, "X")
        else:
            octal = "-" + format(abs(n), "o")
            hexa = "-" + format(abs(n), "X")

        print("\nOutput:")
        print(f"Decimal: {n} (base 10)")
        print(f"Binary:  {bin_str} (base 2)")
        print(f"Octal:   {octal} (base 8)")
        print(f"Hex:     {hexa} (base 16)")

    else:
        print("Invalid choice.")


# -------------------------
# Part IV: Option A vs B
# -------------------------
def part_IV():
    print("Part IV: Compare two earning options for 31 days")

    days = 31

    # Option A: $10,500/day for 31 days
    optionA_daily = 10500
    optionA_total = optionA_daily * days

    # Option B: starts at 2 cents, doubles daily for 31 days
    cents = 2  # day 1
    optionB_total_cents = 0

    print("\nOption B daily earnings (in dollars):")
    for day in range(1, days + 1):
        optionB_total_cents += cents
        dollars = cents / 100
        print(f"Day {day}: ${dollars}")
        cents *= 2

    optionB_total = optionB_total_cents / 100

    print("\nTotals:")
    print(f"Option A total: ${optionA_total}")
    print(f"Option B total: ${optionB_total}")

    if optionA_total > optionB_total:
        print("\nBetter option: A (higher total)")
    elif optionB_total > optionA_total:
        print("\nBetter option: B (higher total)")
    else:
        print("\nBoth options are the same total.")


# -------------------------
# Part V: Debug/analyze program
# -------------------------
def part_V():
    # Line 1:
    # Explanation: Prints a title so the user knows they are running Part V.
    print("Part V: Debug + explain what the given program does")

    # Line 2:
    # Explanation: Prints a short description of the program’s goal (summing powers of 2 up to n).
    print("\nOriginal idea: sum powers of 2 up to n (1 + 2 + 4 + 8 + ... <= n)\n")

    # Line 3:
    # Explanation: Comment indicating the code below is the corrected version of the intended program.
    # Corrected version of the program:

    # Line 4:
    # Explanation: Prompts the user to enter n, reads it as a string, and strips whitespace.
    n_str = input("Enter n: ").strip()

    # Line 5:
    # Explanation: Checks whether the input consists only of digits (i.e., a positive integer).
    if not n_str.isdigit():
        # Line 6:
        # Explanation: If the input is not a positive integer, print an error message.
        print("Please enter a positive integer.")

        # Line 7:
        # Explanation: Stop the function early to avoid errors from invalid input.
        return

    # Line 8:
    # Explanation: Converts the validated string input into an integer value.
    n = int(n_str)

    # Line 9:
    # Explanation: Initializes the first power-of-2 term (2^0 = 1).
    previous_term = 1

    # Line 10:
    # Explanation: Initializes the running total (sum) to 0.
    total = 0

    # Line 11:
    # Explanation: Loop continues while the current term is less than or equal to n.
    while previous_term <= n:
        # Line 12:
        # Explanation: Add the current power-of-2 term to the running total.
        total = total + previous_term

        # Line 13:
        # Explanation: Update the term to the next power of 2 by doubling it.
        previous_term = previous_term * 2

    # Line 14:
    # Explanation: Prints the final sum after the loop finishes.
    print(f"The sum is: {total}")

    # Line 15:
    # Explanation: Prints a label before the short summary explanation.
    print("\nWhat it does (short):")

    # Line 16:
    # Explanation: One-sentence summary of the program’s behavior.
    print("It adds 1 + 2 + 4 + 8 + ... (powers of 2) until the next term would be bigger than n.")


# -------------------------
# Main menu
# -------------------------
def main():
    print("Numerical Analysis Project (CS Major) - Parts I to V")
    print("Choose a part to run:")
    print("1) Part I  (Geometric series)")
    print("2) Part II (Quadratic solver)")
    print("3) Part III(Base conversions)")
    print("4) Part IV (Option A vs B earnings)")
    print("5) Part V  (Debug/analyze program)")
    choice = input("Enter 1-5: ").strip()

    print("\n-----------------------------\n")

    if choice == "1":
        part_I()
    elif choice == "2":
        part_II()
    elif choice == "3":
        part_III()
    elif choice == "4":
        part_IV()
    elif choice == "5":
        part_V()
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()