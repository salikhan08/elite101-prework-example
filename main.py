def main():
    print("=" * 50)
    print("Welcome to the Code2College Chatbot!")
    print("=" * 50)
    
    user_name = input("What's your name? ")
    print(f"Nice to meet you, {user_name}!")
    
    while True:
        try:
            user_age = int(input("How old are you? "))
            break
        except ValueError:
            print("Please enter a valid number for your age.")
    
    if user_age < 18:
        print("Wow, you're a young coder! That's awesome!")
    elif 18 <= user_age <= 25:
        print("Great age for learning software development!")
    else:
        print("It's never too late to learn programming!")
    
    # Main conversation menu
    while True:
        print("\n" + "=" * 30)
        print("HOW CAN I HELP YOU TODAY?")
        print("=" * 30)
        print("1. Learn about Python")
        print("2. Get coding tips")
        print("3. Explore internship opportunities")
        print("4. Exit chatbot")
        
        choice = input("\nPlease choose an option (1-4): ")
        
        if choice == "1":
            print("\nPython is a great programming language for beginners!")
            print("It's known for its simple syntax and wide range of applications.")
            print("You can use Python for web development, data analysis, AI, and more!")
            
        elif choice == "2":
            print("\nHere are some coding tips:")
            print("- Practice regularly")
            print("- Don't be afraid to make mistakes")
            print("- Read other people's code")
            print("- Build projects that interest you")
            
        elif choice == "3":
            print("\nInternship opportunities are great for gaining real-world experience!")
            print("Check with Code2College for upcoming internship opportunities.")
            print("Make sure your GitHub profile is up-to-date!")
            
        elif choice == "4":
            print(f"\nThanks for chatting, {user_name}!")
            print("Good luck with your coding journey!")
            print("=" * 50)
            break
            
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
        
        continue_chat = input("\nWould you like to ask something else? (yes/no): ").lower()
        if continue_chat not in ['yes', 'y']:
            print(f"\nGoodbye, {user_name}! Have a great day!")
            break

if __name__ == "__main__":
    main()