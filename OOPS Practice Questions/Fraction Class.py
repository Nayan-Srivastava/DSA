class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()  # Simplify the fraction upon initialization

    def _find_gcd(self, a, b):
        # Your code to find GCD goes here
        while b:
            a, b = b, a % b
        return a

    def _simplify(self):
        # Your code to simplify the fraction goes here
        gcd = self._find_gcd(abs(self.numerator), abs(self.denominator))
        self.numerator //= gcd
        self.denominator //= gcd
        # Ensure the denominator is positive
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def add(self, other):
        # Your code to add fractions goes here
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)
    def subtract(self, other):
        # Your code to subtract fractions goes here
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def multiply(self, other):
        # Your code to multiply fractions goes here
        return Fraction(self.numerator * other.numerator,
                        self.denominator * other.denominator)

    def divide(self, other):
        # Your code to divide fractions goes here
        if other.numerator == 0:
            raise ValueError("Cannot divide by a fraction with zero numerator")
        return Fraction(self.numerator * other.denominator,
                        self.denominator * other.numerator)

    def __eq__(self, other):
        # Your code to compare fractions goes here
        return (self.numerator == other.numerator and
                self.denominator == other.denominator)

    def __str__(self):
        # Your code for string representation goes here
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        # Your code for detailed representation goes here
        return f"Fraction({self.numerator}, {self.denominator})"