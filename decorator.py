#decorator

def add_sprinkles(func):
    def wrapper(*args , **kwargs):
        print("You Add sprinkles 🎊🎊")
        func(*args , **kwargs)
    return wrapper

def fudge(func):
    def wrapper(*args, **kwargs):
        print("You Added Fudge 🍫🍫")
        func(*args , **kwargs)
    return wrapper

@add_sprinkles
@fudge
def ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍦")


ice_cream("Chocolate")