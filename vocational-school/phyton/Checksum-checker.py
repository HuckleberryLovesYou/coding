while True:
    save_first_checksum = None
    while not (save_first_checksum == "y" or save_first_checksum == "n"):
        save_first_checksum: str = input("save first checksum?[y/n]:\t")
    checksum1: str = input("Please enter your first checksum in here:\n\n")
    checksum1_counter = 1
    if save_first_checksum.lower() == "y":
        counter = 1
        while counter == 1:
            checksum2: str = input("Please enter your second checksum in here:\n\n")
            if checksum1 == checksum2:
                print("Die Checksums sind identisch\n\n\n\n\n")
                counter = 0
            else:
                print("Die Checksums sind **!NICHT GLEICH!**\nVersuche es erneut. Deine erste Checksum wurde gespeichert.")
    else:
        if checksum1_counter == 1:
            checksum2: str = input("Please enter your second checksum in here:\n\n")
            if checksum1 == checksum2:
                print("Die Checksums sind identisch\n\n\n\n\n")
                counter = 0
            else:
                print("Die Checksums sind **!NICHT GLEICH!**\n")
            checksum1_counter = 0
        else:
            checksum1 = str(input("Please enter your first checksum in here:\n\n"))
            checksum2 = str(input("Please enter your second checksum in here:\n\n"))
            if checksum1 == checksum2:
                print("Die Checksums sind identisch\n\n\n\n\n")
                counter = 0
            else:
                print("Die Checksums sind **!NICHT GLEICH!**\nVersuche es erneut.")