# ADDITION OF TWO NUMBERS

def Addition(value1, value2):
    ans = value1 + value2
    return ans

def main():
    print("ADDITION FUNCTION")

    no1 = int(input("ENTER FIRST NUMBER:"))
    no2 = int(input("ENTER SECOND NUMBER:"))

    ret = Addition(no1, no2)

    print("ADDITION OF TWO NUMBERS IS:",ret)

if __name__ == "__main__":
    main()