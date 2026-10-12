# tool: word_lengths
# description: List lengths of whitespace-separated words
# author: @Wkhanex
# example: word_lengths "hi there" -> "2,5"


def run(*args) -> str:
    """Return comma-separated word lengths, counting Unicode code points."""
    if len(args) != 1:
        raise ValueError("expected one string")
    return ",".join(str(len(word)) for word in args[0].split())
