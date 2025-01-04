import hashlib
import pyfiglet
from termcolor import colored

text = colored('Password Cracking Tool!', 'red', attrs=['reverse', 'blink'])
print(text)
ascii_banner = pyfiglet.figlet_format("Password Cracking T00L !!")
print(ascii_banner)


def convert_text_to_sha1(text):
        digest = hashlib.sha1(
            text.encode()
        ).hexdigest()

        return digest

def main():
    user_sha1 = input(" Enter the SHA1 for Cracking : ")
    cleaned_user_sha1 = user_sha1.strip().lower()

    with open('password.txt') as f:
        for line in f:
            password = line.strip()
            converted_sha1 = convert_text_to_sha1(password)

            if cleaned_user_sha1 == converted_sha1:
                print(f"Password Found :  {password}")
                return


        print(("Could Not Found the Password "))

if __name__ == '__main__':
    main()
