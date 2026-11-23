"""Dad Joke Showdown entry.

Writes one dad joke to /output/entry.txt and prints it.
"""

JOKE = "I told my son to embrace his mistakes. He gave me a hug."


def main() -> None:
    joke = JOKE
    assert isinstance(joke, str) and 1 <= len(joke) <= 200, "joke must be 1-200 characters"
    assert joke.strip(), "joke must not be only whitespace"

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(joke)
    print(joke)


if __name__ == "__main__":
    main()
