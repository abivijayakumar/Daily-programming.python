def build_string_simple(n);
parts = []
for i in range(1, n + 1):
parts .append(f"Item {i}")
return ','.join(parts)
result = build_string_simple(5)
print(result)
