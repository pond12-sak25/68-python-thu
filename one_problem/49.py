def toggle_case(s: str) -> str:
    return "".join(ch.lower() if ch.isupper() else ch.upper() for ch in s)

# Example
print(toggle_case("Hello World!"))  # "hELLO wORLD!"
