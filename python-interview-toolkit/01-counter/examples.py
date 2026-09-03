"""Small, runnable examples for collections.Counter."""

from collections import Counter


def main() -> None:
    letters = Counter("mississippi")
    print("frequencies:", letters)
    print("count of s:", letters["s"])
    print("missing key:", letters["z"])
    print("top two:", letters.most_common(2))

    inventory = Counter(apples=3, oranges=1)
    inventory.update(["apples", "pears"])
    inventory.subtract({"oranges": 2})
    print("inventory (negative counts remain):", inventory)
    print("available items:", sorted(inventory.elements()))

    requested = Counter("aabc")
    available = Counter("aaabbcd")
    print("shared multiset:", requested & available)
    print("unmet requests:", requested - available)
    print("can fulfill request:", not (requested - available))


if __name__ == "__main__":
    main()
