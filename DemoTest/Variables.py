# nonlocal
def outer():
    msg = "Testing"

    def inner():
        nonlocal msg

        msg = 'nonlocal'
        print("non local ", msg)

    inner()
    print("out side ", msg)


outer()