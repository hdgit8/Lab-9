class PasswordManager:
    def __init__(self):
        self.password = None

    def encoder(self, password):
        encoded = []
        for digit in password:
            encoded_digit = str((int(digit) + 3) % 10)
            encoded.append(encoded_digit)
        return ''.join(encoded)

    def decoder(self, encoded):
        decoded = []
        for digit in encoded:
            decoded_digit = str((int(digit) - 3) % 10)
            decoded.append(decoded_digit)
        return ''.join(decoded)

if __name__ == "__main__":
    password_manager = PasswordManager()

    while True:
        print("""Menu
-------------
1. Encode
2. Decode
3. Quit
              """)

        option = input("Please enter an option: ")

        if option == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = password_manager.encoder(password)
            print("Your password has been encoded and stored!\n")

        elif option == '2':
            decoded_password = password_manager.decoder(encoded_password)
            print("The encoded password is", encoded_password, "and the original password is", decoded_password,".\n")

        elif option == '3':
            break
