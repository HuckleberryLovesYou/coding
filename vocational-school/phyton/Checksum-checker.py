while 1 == 1:
    checksum1 = str(input("Please enter your first checksum in here:\n\n"))
    if checksum1_speichern == "Ja":
        counter = 1
        while counter == 1:
            checksum2 = str(input("Please enter your second checksum in here:\n\n"))
            if checksum1 == checksum2:
                print("Die Checksums sind identisch\n\n\n\n\n")
                counter = 0
            else:
                print("Die Checksums sind **!NICHT GLEICH!**\nVersuche es erneut. Deine erste Checksum wurde gespeichert.")