varA = 20
varB = 200
typeStr = type("string")
result = ""

if type(varA) == typeStr or type(varB) == typeStr:
    result = "string involved"
elif varA > varB:
    result = "bigger"
elif varA == varB:
    result = "equal"
elif varA < varB:
    result = "smaller"
print(result)