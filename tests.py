from functions import multiply

def tester():
    ans = multiply(2, 5)
    exp = 10
    assert ans == exp, "Test-1 failed."

    ans = multiply(4, 6)
    exp = 24
    assert ans == exp, "Test-2 failed."

    ans = multiply(9, 9)
    exp = 81
    assert ans == exp, "Test-3 failed."


if __name__ == "__main__":
    tester()
