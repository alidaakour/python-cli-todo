import json

DATA_FILE = "data.json"

def show_menu():
    print("\n1) Add item")
    print("2) List items")
    print("3) Remove item by index")
    print("4) Load from file")
    print("5) Save to file")
    print("6) Exit")

def save_items(items):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

def load_items():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("No data.json yet. Starting empty.")
        return []
    except json.JSONDecodeError:
        print("data.json is broken. Starting empty.")
        return []

items = load_items()

while True:
    show_menu()
    choice = input("Choose (1-6): ").strip()

    if choice == "1":
        text = input("Enter item text: ").strip()
        if text == "":
            print("Empty item not allowed.")
        else:
            items.append(text)
            print("Added.")

    elif choice == "2":
        if len(items) == 0:
            print("No items yet.")
        else:
            for i, item in enumerate(items):
                print(f"{i}) {item}")

    elif choice == "3":
        if len(items) == 0:
            print("Nothing to remove.")
            continue

        s = input("Enter index to remove: ").strip()
        if not s.isdigit():
            print("Index must be a number.")
            continue

        idx = int(s)
        if idx < 0 or idx >= len(items):
            print("Index out of range.")
            continue

        removed = items.pop(idx)
        print(f"Removed: {removed}")

    elif choice == "4":
        items = load_items()
        print(f"Loaded {len(items)} item(s).")

    elif choice == "5":
        save_items(items)
        print(f"Saved {len(items)} item(s).")

    elif choice == "6":
        print("Bye!")
        break

    else:
        print("Invalid choice.")
