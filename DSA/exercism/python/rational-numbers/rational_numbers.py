class Rational:
    def __init__(self, numer: int, denom: int):
        self.numer, self.denom = self.red(numer, denom)

    def red(self, n: int, d: int):
        is_n_minus = n < 0
        is_d_minus = d < 0
        n, d = abs(n), abs(d)

        if n == 0:
            return 0, 1

        for i in range(max(n, d), 0, -1):
            if n % i == 0 and d % i == 0:
                n //= i
                d //= i

        if is_n_minus and not is_d_minus:
            return -n, d

        if not is_n_minus and is_d_minus:
            return -n, d

        return n, d

    def __eq__(self, other: "Rational") -> bool:
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self) -> str:
        return f"{self.numer}/{self.denom}"

    def __add__(self, other: "Rational") -> "Rational":
        numer = self.numer * other.denom + other.numer * self.denom
        denom = self.denom * other.denom
        numer, denom = self.red(numer, denom)
        return Rational(numer, denom)

    def __sub__(self, other: "Rational") -> "Rational":
        numer = self.numer * other.denom - other.numer * self.denom
        denom = self.denom * other.denom
        numer, denom = self.red(numer, denom)
        return Rational(numer, denom)

    def __mul__(self, other: "Rational") -> "Rational":
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        numer, denom = self.red(numer, denom)
        return Rational(numer, denom)

    def __truediv__(self, other: "Rational") -> "Rational":
        numer = self.numer * other.denom
        denom = self.denom * other.numer
        numer, denom = self.red(numer, denom)
        return Rational(numer, denom)

    def __abs__(self) -> "Rational":
        numer = abs(self.numer)
        denom = abs(self.denom)
        numer, denom = self.red(numer, denom)
        return Rational(numer, denom)

    def __pow__(self, power: int) -> "Rational":
        if power == 0:
            return Rational(1, 1)

        is_minus = power < 0
        power = abs(power)

        numer = self.numer**power
        denom = self.denom**power
        numer, denom = self.red(numer, denom)

        if is_minus:
            return Rational(denom, numer)
        else:
            return Rational(numer, denom)

    def __rpow__(self, base: int) -> float:
        numer, denom = self.numer, self.denom
        return base ** (numer / denom)
