def input_age(age):
    try:
        assert int(age) > 18
        print()
    except ValueError:
        return 'ValueError: Cannot convert into int'
    else:
        return 'Age is saved successfully'


if __name__ == "__main__":
    print(input_age(43))