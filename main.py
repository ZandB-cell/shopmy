# todo.py
# Қарапайым To-Do тізімі (Python 3)
# Қолдану: python todo.py

import json
from pathlib import Path

FILE = Path("todos.json")

def load_todos():
    if not FILE.exists():
        return []
    try:
        return json.loads(FILE.read_text(encoding="utf-8"))
    except Exception:
        return []

def save_todos(todos):
    FILE.write_text(json.dumps(todos, ensure_ascii=False, indent=2), encoding="utf-8")

def list_todos(todos):
    if not todos:
        print("Тізім бос.")
        return
    for i, t in enumerate(todos, 1):
        print(f"{i}. {t}")

def add_todo(todos, text):
    todos.append(text)
    save_todos(todos)
    print(f"Қосылды: «{text}»")

def remove_todo(todos, index):
    try:
        removed = todos.pop(index-1)
        save_todos(todos)
        print(f"Жойылды: «{removed}»")
    except IndexError:
        print("Қате: осындай нөмір жоқ.")

def clear_todos():
    save_todos([])
    print("Барлығы жойылды.")

def help_text():
    print("""Пәрмендер:
  add <текст>     - жаңа тапсырма қосу
  list            - барлық тапсырмаларды көрсету
  remove <нөмір>  - тапсырманы нөмір бойынша жою
  clear           - барлық тапсырмаларды жою
  help            - көмектi көрсету
  exit            - бағдарламадан шығу
""")

def main():
    todos = load_todos()
    print("Жай To-Do (командаларды көру үшін 'help' теріңіз)")
    while True:
        try:
            cmd = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nШығу...")
            break

        if not cmd:
            continue

        parts = cmd.split(maxsplit=1)
        action = parts[0].lower()

        if action == "add":
            if len(parts) < 2:
                print("Қолдану: add <текст>")
                continue
            add_todo(todos, parts[1])
        elif action == "list":
            list_todos(todos)
        elif action == "remove":
            if len(parts) < 2 or not parts[1].isdigit():
                print("Қолдану: remove <нөмір>")
                continue
            remove_todo(todos, int(parts[1]))
        elif action == "clear":
            confirm = input("Рас па? (y/N): ").strip().lower()
            if confirm == "y":
                clear_todos()
                todos = []
        elif action == "help":
            help_text()
        elif action == "exit":
            print("Шығу...")
            break
        else:
            print("Белгісіз пәрмен. 'help' деп көріңіз.")

if __name__ == "__main__":
    main()
