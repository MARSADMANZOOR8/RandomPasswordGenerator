def main():
    print("Welcome to the Pypassword Generator!")
    print("how man letter do you want in your password?")
    Letters = int(input())
    print("how man symbol do you want in your password?")
    Symbols = int(input())      
    print("how man number do you want in your password?")
    Numbers = int(input())      
    import random
    import string       
    password_letters = ''.join(random.choices(string.ascii_letters, k=Letters))
    password_symbols = ''.join(random.choices(string.punctuation, k=Symbols))   
    password_numbers = ''.join(random.choices(string.digits, k=Numbers))
    password = password_letters + password_symbols + password_numbers
    password_list = list(password)
    random.shuffle(password_list)
    final_password = ''.join(password_list)
    print("Your password is: " + final_password)    
if __name__ == "__main__":
    main()