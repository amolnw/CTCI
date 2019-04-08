from arrays.HashTableUsingArray import HashTableUsingArray


def test_hash_table_using_arrays():
    hta = HashTableUsingArray(10)
    for i in range(99):
        hta.insert(i)

    print(hta)


def main():
    test_hash_table_using_arrays()


if __name__ == "__main__":
    main()

