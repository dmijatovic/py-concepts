
class Decimal:
  def __init__(self, number, decimals):
    self.number = number
    self.decimals = decimals

  def __repr__(self):
    return f"%.{self.decimals}f" % self.number


class Currency(Decimal):
  """
  Currency INHERITS from Decimal class
  """

  def __init__(self, number, decimals, pre="", post=""):
    # here we could manipulate numbers and decimals
    # NOTE! calling super()
    super().__init__(number, decimals)
    self.pre = pre
    self.post = post

  def __repr__(self):
    return f"{self.pre}{super().__repr__()}{self.post}"


print(Decimal(1.345645, 2))
print(Currency(1.345645, 2, "$"))
