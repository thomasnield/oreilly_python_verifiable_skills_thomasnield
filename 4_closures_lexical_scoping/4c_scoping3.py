x = "global"  # Global scope

def outer():
    x = "enclosing"  # Enclosing scope
    def inner():
        x = "local"  # Local scope
        print(x)     # Resolves to local: "local"
    inner()
    print(x)         # Resolves to enclosing: "enclosing"

outer()
print(x)             # Resolves to global: "global"

# Built-in example
print(len("built-in"))  # 'len' is built-in