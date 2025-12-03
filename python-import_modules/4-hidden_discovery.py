#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for name in sorted(n for n in names if not n.startswith("__")):
        print(name)
