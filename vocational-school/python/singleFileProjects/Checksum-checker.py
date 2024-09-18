def is_same(checksum1, checksum2) -> bool:
    evaluation: bool = checksum1 == checksum2
    if evaluation:
        print("The checksums are identical.")
    else:
        print("The checksums are **NOT** identical.")
    return evaluation

def main() -> None:
    while True:
        checksum_1: str = input("Enter first checksum: ")

        save_first_checksum: str = ""
        while not (save_first_checksum == "y" or save_first_checksum == "n"):
            save_first_checksum = input("save first checksum?[y/n]: ").lower()

        if save_first_checksum == "y":
            while True:
                checksum_2: str = input("Enter second checksum: ")
                if is_same(checksum_1, checksum_2):
                    break
        else:
            checksum_2: str = input("Enter second checksum: ")
            is_same(checksum_1, checksum_2)


if __name__ == "__main__":
    main()