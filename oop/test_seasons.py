from seasons import minutes_lived

def main():
    test_1()
    test_2()

def test_1():
    assert minutes_lived(2003,5,17) == "Eleven million, two hundred fifty-three thousand, six hundred minutes"
    assert minutes_lived(2000,2,1) == "Twelve million, nine hundred eighty-three thousand forty minutes"

def test_2():
    assert minutes_lived(23,1,2000) == "Invalid Date"

if __name__ == "__main__":
    main()
