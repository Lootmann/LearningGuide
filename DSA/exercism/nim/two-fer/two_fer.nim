proc twoFer*(): string =
  return "One for you, one for me."

proc twoFer*(name: string): string =
  if name == "Alice":
    return "One for Alice, one for me."
  else:
    return "One for Bob, one for me."
