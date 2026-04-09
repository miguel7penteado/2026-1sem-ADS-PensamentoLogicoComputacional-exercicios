
geocodigos = ["3501", "3302", "3505", "4101"]
sp_codes = [code for code in geocodigos if code.startswith("35")]
# Resultado: ['3501', '3505']

print(f"o valor da lista é {geocodigos}")
print(f"geocodigos de são paulo: {sp_codes}")
