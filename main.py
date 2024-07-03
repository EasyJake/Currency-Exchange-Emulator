class Currency:
  currencies = {
      'CHF': 0.930023,  # Swiss franc
      'CAD': 1.264553,  # Canadian dollar
      'GBP': 0.737414,  # British pound
      'JPY': 111.019919,  # Japanese yen
      'EUR': 0.862361,  # Euro
      'USD': 1.0  # US dollar
  }

  def __init__(self, value, unit="USD"):
      self.value = value
      self.unit = unit

  def changeTo(self, new_unit):
      """Transform the Currency object from 'self.unit' to 'new_unit'."""
      self.value = (self.value / Currency.currencies[self.unit]) * Currency.currencies[new_unit]
      self.unit = new_unit

  def __repr__(self):
      return f"{self.value:.2f} {self.unit}"

  def __str__(self):
      return self.__repr__()

  def __add__(self, other):
      if isinstance(other, Currency):
          if self.unit != other.unit:
              other_converted = other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]
              return Currency(self.value + other_converted, self.unit)
          return Currency(self.value + other.value, self.unit)
      elif isinstance(other, (int, float)):  # Treat int/float as USD
          return Currency(self.value + (other / Currency.currencies['USD'] * Currency.currencies[self.unit]), self.unit)
      return NotImplemented

  def __iadd__(self, other):
      result = self.__add__(other)
      if result is not NotImplemented:
          self.value, self.unit = result.value, result.unit
          return self
      return NotImplemented

  def __radd__(self, other):
      return self.__add__(other)

  def __sub__(self, other):
      return self.__add__(-other)

  def __isub__(self, other):
      result = self.__sub__(other)
      if result is not NotImplemented:
          self.value, self.unit = result.value, result.unit
          return self
      return NotImplemented

  def __rsub__(self, other):
      if isinstance(other, (int, float)):  # Treat int/float as USD
          return Currency((other / Currency.currencies['USD'] * Currency.currencies[self.unit]) - self.value, self.unit)
      return NotImplemented


# Test the functionality
v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)  # Should convert v2 to EUR and then add
print(v2 + v1)  # Should convert v1 to USD and then add
print(v1 + 3)  # Treats 3 as USD and adds to v1 as EUR
print(3 + v1)  # Treats 3 as USD and adds to v1 as EUR
print(v1 - 3)  # Treats 3 as USD and subtracts from v1 as EUR
print(30 - v2)  # Treats 30 as USD and subtracts v2 from it
