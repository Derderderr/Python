import string
import secrets

class PasswordGenerator:
    CHAR_POOLS = {
        "lowercase": string.ascii_lowercase,
        "uppercase": string.ascii_uppercase,
        "digits": string.digits,
        "punctuation": string.punctuation,
    }

    @classmethod
    def build_sequence(cls, conditions: dict) -> str:
        sequence = "".join(
            chars for key, chars in cls.CHAR_POOLS.items() if conditions.get(key, False)
        )

        if not sequence:
            raise ValueError("At least one character set must be enabled.")

        return sequence

    @staticmethod
    def generate(sequence: str, length: int = 8) -> str:
        return "".join(secrets.choice(sequence) for _ in range(length))


class Interface:
    has_characters = {
        "lowercase": True,
        "uppercase": True,
        "digits": True,
        "punctuation": True,
    }

    @classmethod
    def toggle(cls, key: str):
        if key not in cls.has_characters:
            print("Invalid option.")
            return

        cls.has_characters[key] = not cls.has_characters[key]
        print(f"{key} → {cls.has_characters[key]}")

    @classmethod
    def show(cls):
        for k, v in cls.has_characters.items():
            print(f"{k}: {v}")

    def generate_password(self, length: int):
        try:
            sequence = PasswordGenerator.build_sequence(self.has_characters)
            password = PasswordGenerator.generate(sequence, length)
            print(f"\nGenerated: {password}")
        except ValueError as e:
            print(f"Error: {e}")


def format_menu(options):
    return "\n".join(options)


class App:
    def handle_input(self, user_input: str):
        if user_input.isdigit():
            Interface().generate_password(int(user_input))
        else:
            Interface.toggle(user_input)

        print("\n")

    def run(self):
        menu = f"""Welcome to PassGen
Enter a number → generate password

Toggle character sets:
{format_menu(Interface.has_characters.keys())}
        """

        print(menu)

        while True:
            user_input = input("> ").strip()
            self.handle_input(user_input)




if __name__ == "__main__":
    App().run()
