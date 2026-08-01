name = input("Jak masz na imię? ")
age = int(input("Ile masz lat? "))

centuries = age // 100
decades = age // 10
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60


print(f"{name}, żyjesz około:")
print(f"{centuries} wieków")
print(f"{decades} dekad")
print(f"{days} dni")
print(f"{hours} godzin")
print(f"{minutes} minut")
print(f"{seconds} sekund")
