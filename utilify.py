import difflib, time, sys, random, os
import contextlib
from typing import Any, Optional


class variable:
    """A toolkit for editing variables"""

    @staticmethod
    def Idelete(var: str, var_ind: int = -1) -> str:
        """
        Delete a specific letter by index

        var:
            the text
        var_ind:
            the index of the letter, defaulted by -1 (last letter)
            
        >>> variable.Idelete("aktm", 1) → 'atm'
        """
        return var.replace(var[var_ind], "", 1)

    @staticmethod
    def delete(var: str, letter: str, occurrences: int = 1) -> str:
        """
        Delete a letter by given occurrences

        var:
            the text
        letter:
            the targeted letter
        occurrences:
            the occurrences of deleting the letter, defaulted by 1
            
        >>> variable.delete("messssy", "s", 2) → 'messy'
        """
        return var.replace(letter, "", occurrences)

    @staticmethod
    def insert(char: str, var: str, var_ind: int = -1) -> str:
        """
        Add a specific letter at a specific index.

        char:
            the character
        var:
            the text
        var_ind:
            the index(placement) of the letter
        
        >>> variable.insert("d", "car", -1) → 'card'
        """
        return var[:var_ind] + char + var[var_ind:]

    @staticmethod
    def replace(var: str, var_ind: int, replacement: str) -> str:
        """Replace occurrences of a letter."""
        return var[:var_ind] + replacement + var[var_ind + 1:]

    @staticmethod
    def random_int(minimum: int, maximum: int) -> int:
        """Generates a random integer between two values"""
        return random.randint(minimum, maximum)


class strings:
    """String-related utilities."""

    @staticmethod
    def is_palindrome(word: str) -> bool:
        """Check if a word is palindrome."""
        return word == word[::-1]

    lower_letters: tuple[str, ...] = tuple(chr(i) for i in range(97, 123))
    upper_letters: tuple[str, ...] = tuple(chr(i).upper() for i in range(97, 123))
    ascii_symbols: tuple[str, ...] = tuple(chr(i) for i in range(33, 123) if not chr(i).isalnum())
    digits: tuple[int, ...] = tuple(range(10))

    @staticmethod
    def remove_letters(text: str, *letters: str) -> str:
        """
        Remove specific letters from a string.

        text:
            the text to filter
        *letters:
            unlimited amount of letters to delete

        >>> strings.remove_letters("wlatlchi", "i", "l") → 'watch'
        """
        filtered = [l for l in text if l not in letters]
        return ''.join(filtered)


def timer(func: Any) -> Any:
    """Returning functions' elapsing time"""

    def wrapper(*args: Any, **kwargs: Any) -> None:
        start = time.time()
        with open(os.devnull, "w") as devnull:
            with contextlib.redirect_stdout(devnull), contextlib.redirect_stderr(devnull):
                try:
                    func(*args, **kwargs)
                except Exception:
                    end = time.time()
                    print(f"{end - start:.4f}")
                    raise
        end = time.time()
        print(f"{end - start:.4f}")

    return wrapper


def auto_correct(word: str, dictionary: list[str], alter_value: Any) -> Any:
    """
    Auto-correct the given word to its nearest match in the given dictionary.

    word:
        the word to be corrected
    dictionary:
        list of available words to compare
    alter_value:
        value to return if no match was found

    >>> auto_correct("appel", ["apple", "apply", "maple"], "unknown") → 'apple'
    """
    matches = difflib.get_close_matches(word, dictionary, n=1, cutoff=0.7)
    return matches[0] if matches else alter_value


def are_close(string1: str, string2: str, threshold: float, minimum: float, get_ratio: bool = False) -> Optional[Any]:
    """
    Check how close two strings are.

    string1:
        the first string to compare
        
    string2:
        the second string to compare
        
    threshold:
        upper similarity threshold for "True"
        
    minimum:
        lower similarity threshold for "False"
        
    get_ratio:
        if True, returns percentage similarity instead of boolean

    >>> are_close("hello", "hell", 0.8, 0.5, False) → True
    >>> are_close("car", "dog", 0.8, 0.5, True) → '33%'
    """
    s = difflib.SequenceMatcher(None, string1, string2)
    rate: float = s.ratio()

    if not get_ratio:
        if minimum <= rate < threshold:
            return None
        elif rate >= threshold:
            return True
        elif rate <= minimum:
            return False
    else:
        return f"{int(rate * 100)}%"


def get_index(item: Any, data: Any) -> Optional[int]:
    """
    Get the index of an item in a tuple/list/variable.

    item:
        the item to search for
    data:
        the sequence to search in

    >>> get_index("five", ("one", "two", "three", "four", "five")) → 4
    """
    if isinstance(data, dict):
        raise TypeError("Can't get the index of a dict object")
    else:
        try:
            return data.index(item)
        except (ValueError, AttributeError):
            return None


def get_location(ind: int, data: Any) -> Optional[Any]:
    """
    Get the item at a given index.

    ind:
        index of the desired element
    data:
        the sequence to extract from

    >>> get_location(2, ('a', 'b', 'c', 'd')) → 'c'
    """
    if isinstance(data, dict):
        raise TypeError("Can't get a value from a dict object by index")
    else:
        try:
            for i in range(len(data)):
                if i == ind:
                    return data[i]
        except (ValueError, AttributeError):
            return None


def flash_text(phrase: str, delay: float = 0.5) -> None:
    """Write a text then delete (works mostly in Terminal & might fail in some environments)."""
    sys.stdout.write(phrase)
    sys.stdout.flush()
    time.sleep(delay)
    sys.stdout.write("\r" + " " * len(phrase) + "\r")


def flash_items(collection: Any, delay: float = 0.5) -> None:
    """Write each item in a collection and then delete it."""
    if isinstance(collection, dict):
        for key, value in collection.items():
            sys.stdout.write(f"{key}: {value}")
            sys.stdout.flush()
            time.sleep(delay)
            sys.stdout.write("\r" + " " * len(f"{key}: {value}") + "\r")

    elif isinstance(collection, (tuple, list)):
        for i, c in enumerate(collection):
            collection[i] = str(c)

        for item in collection:
            sys.stdout.write(item)
            sys.stdout.flush()
            time.sleep(delay)
            sys.stdout.write("\r" + " " * len(item) + "\r")


def Sprint(data: Any, delay: float = 0.5, ending: str = " ") -> None:
    """Print items in a list/tuple/dictionary slowly."""
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"{key}: {value}", flush=True, end=ending)
            time.sleep(delay)
    elif isinstance(data, (list, tuple)):
        for item in data:
            print(item, end=ending, flush=True)
            time.sleep(delay)



def getabbr(text: str) -> str | None:
    """
    Returns the abbreviation of the given text.
    
    Notes: 
    • any word that starts with a capital letter will be ingnored
    • any non-standard symbol will be ignored
    
    >>> print(getabbr("information And communication tech")) → 'ICT'
    """
    try:
        nt = ""
        for t in text.split():
            for ch in t[0]:
                if ch in strings.lower_letters:  # ignores non-standard symbols
                    nt += ch.upper()
                    break
        return nt
    except (AttributeError, TypeError, Exception, ValueError):
        return None
        


if __name__ == '__main__':
    print(strings.is_palindrome("wow"))  # True

    r = ("one", "two", "three", "four", "five", "six")
    print(get_index("five", r))  # 4
    print(get_location(3, r))    # four