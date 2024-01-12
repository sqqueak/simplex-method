class Equation:
  def __init__(self, a, x, sign, b):
    self.a = a
    self.x = x
    self.sign = sign
    self.b = b

  def __str__(self):
    s = []
    for ai, xi in zip(self.a, self.x):

      if ai >= 0:
        s.append(" + ")
      else:
        s.append(" - ")
      
      if abs(ai) != 1:
        s.append(f'{abs(ai)}{xi}')
      else:
        s.append(xi)

    if self.sign != None and self.b != None:
      s.append(f' {self.sign} {self.b}')

    if (t := ''.join(s))[1] == "+":
      return t[3:]
    return f'-{t[3:]}'


def get_equation_from_string(s):
  # getting ax, b, and sign
  ax = []
  b = None
  sign = None

  buf = []
  for i, ch in enumerate(s):
    if ch == " ":
      continue

    elif ch in {"+", "-", "=", "<", ">"}:
      if not sign:
        if ch == "<":
          if s[i+1] == "=":
            sign = "<="
          else:
            sign = "<"
        elif ch == ">":
          if s[i+1] == "=":
            sign = ">="
          else:
            sign = ">"
        elif ch == "=":
          sign = "="

      if buf:
        if (w := ''.join(buf)).isdigit():
          b = int(w)
        else:
          ax.append(w)

        buf = []
        if ch == "-":
          buf.append("-")
      
    else:
      buf.append(ch)
  
  if (w := ''.join(buf)).isdigit():
    b = int(w)
  else:
    ax.append(w)
  buf = []

  # splitting ax into a and x
  a = []
  x = []
  for term in ax:
    buf = []
    for i, ch in enumerate(term):
      if ch.isdigit() or ch == "-":
        buf.append(ch)
      else:
        if not buf:
          a.append(1)
        elif len(buf) == 1 and buf[0] == "-":
          a.append(-1)
        else:
          a.append(int(''.join(buf)))
        x.append(term[i:])

  return Equation(a, x, sign, b)
           

class LinearProgram:
  def __init__(self, cost, constraints, variables):
    self.cost = cost
    self.constraints = constraints
    self.variables = variables

  def __str__(self):
    s = []
    s.append(f'MIN. {self.cost}')
    for x in self.constraints:
      s.append(x)
    for x in self.variables:
      s.append(x)
    return '\n'.join([str(x) for x in s])
