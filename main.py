from instructions import show_instructions, show_shortcuts
from time_operations import get_current_time, convert_time

def menu():
    show_shortcuts()

    while True:
        choice = input("\n👉 Enter choice: ").lower()

        if choice == "1":
            get_current_time()
        elif choice == "2":
            convert_time()
        elif choice == "i":
            show_instructions()
        elif choice == "h":
            show_shortcuts()
        elif choice in ["3", "q"]:
            print("👋 Exiting BuddyZone!")
            break
        else:
            print("❌ Invalid option. Press 'h' for help.")


if __name__ == "__main__":
    show_instructions()
    menu()
