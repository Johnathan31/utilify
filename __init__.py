import difflib, time, sys, random, os, threading, base64
import contextlib
from typing import Any, Optional
from string import ascii_letters


def auto_correct(word: str, dictionary: list[Any] | tuple[Any], alter_value: Any = None) -> Any:
    """
    Auto-correct the given word to its nearest match in the given dictionary.
    
    arguments:
    word -- the word to be corrected
    dictionary -- list of available words to compare
    alter_value -- value to return if no match was found, returns None by default

    >>> auto_correct("appel", ["apple", "apply", "maple"], "unknown") → 'apple'
    """
    matches = difflib.get_close_matches(word, dictionary, n=1, cutoff=0.7)
    return matches[0] if matches else alter_value




def are_close(string1: str, string2: str, threshold: float, minimum: float, get_ratio: bool = False) -> Optional[Any]:
    """
    Check how close two strings are.
    
    arguments:
    string1 -- the first string to compare
        
    string2 -- the second string to compare
        
    threshold -- upper similarity threshold for "True"
        
    minimum -- lower similarity threshold for "False"
        
    get_ratio -- if True, returns percentage similarity instead of boolean, defaulted by False

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




def Index(item: Any, data: Any) -> Optional[int]:
    """
    Get the index of an item in a tuple/list/variable.
    
    arguments:
    item -- the item to search for
    data -- the sequence to search in

    >>> Index("five", ("one", "two", "three", "four", "five")) → 4
    """
    if isinstance(data, dict):
        raise TypeError("Can't get the index of a dict object")
    else:
        try:
            return data.index(item)
        except (ValueError, AttributeError):
            return None


def location(ind: int, data: Any) -> Optional[Any]:
    """
    Get the first occurrence of an item at a given index.
    
    arguments:
    ind -- index of the desired element
    data -- the sequence to extract from

    >>> location(2, ('a', 'b', 'c', 'd')) → 'c'
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




def countFreq(var: str, letters: Any) -> dict[str, int]:
    """
    Returns the frequency of the given letters in the given text.
    
    arguments:
    var -- The text to analyze.
    letters -- The letters to count. Can be a string, tuple, or list.
        
        
    >>> countFreq("independent", ("i", "e", "d")) → {'i': 1, 'e': 3, 'd': 2}
    """

    # Handle invalid inputs
    if not isinstance(var, (str, list, tuple)):
        raise TypeError("var parameter must be a str, list, or a tuple.")

    # Convert single string input to iterable
    if isinstance(letters, str):
        letters = [letters]

    # Count frequency
    result = {}
    for l in letters:
        if not isinstance(l, str) or len(l) == 0:
            continue  # ignore invalid entries
        result[l] = var.count(l)

    return result



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
    else:
    	return None



def Sprint(data: Any, delay: float = 0.5, end: str = " ") -> None:
    """Slow prints items in a list/tuple/dictionary."""
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"{key}: {value}", flush=True, end=end)
            time.sleep(delay)
    elif isinstance(data, (list, tuple, str)):
        for item in data:
            print(item, end=end, flush=True)
            time.sleep(delay)



def getabbr(text: str) -> str | None:
    """
    Returns the abbreviation of the given text.
    
    Notes: 
    • any word that starts with a capital letter will be ingnored
    • any non-standard symbol will be ignored
    
    >>> getabbr("information And communication tech") → 'ICT'
    """
    try:
        nt = ""
        for t in text.split():
            for ch in t[0]:
                if ch in ascii_letters:  # ignores non-standard symbols
                    nt += ch.upper()
                    break
        return nt
    except (AttributeError, TypeError, Exception, ValueError) as e:
        return e
        
            
                
                    
                        


class strings:
    """String-related utilities."""
    
    lower_letters: tuple[str, ...] = tuple(chr(i) for i in range(97, 123))
    
    upper_letters: tuple[str, ...] = tuple(chr(i).upper() for i in range(97, 123))
    
    ascii_symbols: tuple[str, ...] = tuple(chr(i) for i in range(33, 123) if not chr(i).isalnum())
    
    digits: tuple[int, ...] = tuple(range(10))

    @staticmethod
    def remove_letters(text: str, *letters: str) -> str:
        """
        Remove specific letters from a string.
        
        arguments:
        text -- the text to filter
        *letters -- unlimited amount of letters to delete

        >>> strings.remove_letters("wlatlchi", "i", "l") → 'watch'
        """
        filtered = [l for l in text if l not in letters]
        return ''.join(filtered)





class variable:
    """A toolkit for editing variables"""

    @staticmethod
    def deleteInd(var: str, var_ind: int = -1) -> str:
        """
        Delete a specific letter by index

        var -- the text
        var_ind -- the index of the letter, defaulted by -1 (last letter)
            
        >>> variable.Idelete("aktm", 1) → 'atm'
        """
        if var_ind < 0:
        	var_ind += len(var)
        return var[:var_ind] + var[var_ind+1:]


    @staticmethod
    def delete(var: str, letter: str, occurrences: int = 1) -> str:
        """
        Delete a letter by given occurrences
        
        arguments:
        var -- the text
        letter -- the targeted letter
        occurrences -- the occurrences of deleting the letter, defaulted by 1
            
        >>> variable.delete("messssy", "s", 2) → 'messy'
        """
        return var.replace(letter, "", occurrences)

    @staticmethod
    def insert(char: str, var: str, var_ind: int = -1) -> str:
        """
        Add a specific letter at a specific index.
        
        arguments:
        char -- the character
        var -- the text
        var_ind -- the index(placement) of the letter
        
        >>> variable.insert("d", "car", -1) → 'card'
        """
        return var[:var_ind] + char + var[var_ind:]

    @staticmethod
    def replace(var: str, var_ind: int, replacement: str) -> str:
        """
        Replace a letter by index.
        
        arguments:
        var -- the text
        var_ind -- the index of targeted letter
        replacement -- the replacer letter
        
        >>> variable.replace("burn", 1, "o") → 'born'
        """
        return var[:var_ind] + replacement + var[var_ind + 1:]

    @staticmethod
    def random_int(minimum: int, maximum: int) -> int:
        """Generates a random integer between two values"""
        return random.randint(minimum, maximum)




# Decorators:


def timer(func: Any) -> Any:
    """A decorator returning functions' elapsing time
    • Note: any function with this decorator won't return the code in the function, only the time taken.
    
    >>>
    	@timer
    	def timed():
    		for i in range(999999):
    			print(i)
    	
    	timed() → 6.5043
    """

    def wrapper(*args: Any, **kwargs: Any) -> None:
        start = time.time()
        with open(os.devnull, "w") as devnull:
            with contextlib.redirect_stdout(devnull), contextlib.redirect_stderr(devnull):
                try:
                    func(*args, **kwargs)
                except Exception:
                    end = time.perf_counter()
                    print(f"{end - start:.4f}")
                    raise
        end = time.perf_counter()
        print(f"{end - start:.4f}")

    return wrapper



def run_once(func: Any) -> Any | None:
    """A decorator preventing calling a function more than once
    >>>
    	@run_once
    	def temp():
    		print("Hello world")
    		
    	temp() → 'Hello world'
    	temp() → Exception: Function 'temp' can only run once.
    """
    called = False
    result = None
    def wrapper(*args, **kwargs):
        nonlocal called, result
        if not called:
            result = func(*args, **kwargs)
            called = True
        else:
            raise Exception(f"Function '{func.__name__}' can only run once.")
        return result
    return wrapper



def delayed(seconds: int) -> Any | None:
    """Delays the function when called for the given time."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            func(*args, **kwargs)
        return wrapper
    return decorator
    
    

def encrypted(func: Any) -> Any | None:
    """Encrypts the function to the base64 cipher.
    
    >>>
    	@encrypted
    	def example():
    		print("Hello world")
    	
    	example() → 'SGVsbG8gd29ybGQ='
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        try:
        	encoded = base64.b64encode(result.encode()).decode()
        except AttributeError:
        	return None
        return encoded
    return wrapper
 
     get_ratio -- if True, returns percentage similarity instead of boolean, defaulted by False

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




def Index(item: Any, data: Any) -> Optional[int]:
    """
    Get the index of an item in a tuple/list/variable.
    
    arguments:
    item -- the item to search for
    data -- the sequence to search in

    >>> get_index("five", ("one", "two", "three", "four", "five")) → 4
    """
    if isinstance(data, dict):
        raise TypeError("Can't get the index of a dict object")
    else:
        try:
            return data.index(item)
        except (ValueError, AttributeError):
            return None


def location(ind: int, data: Any) -> Optional[Any]:
    """
    Get the first occurrence of an item at a given index.
    
    arguments:
    ind -- index of the desired element
    data -- the sequence to extract from

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




def countFreq(var: str, letters: Any) -> dict[str, int]:
    """
    Returns the frequency of the given letters in the given text.
    
    arguments:
    var -- The text to analyze.
    letters -- The letters to count. Can be a string, tuple, or list.
        
        
    >>> countFreq("independent", ("i", "e", "d")) → {'i': 1, 'e': 3, 'd': 2}
    """

    # Handle invalid inputs
    if not isinstance(var, (str, list, tuple)):
        raise TypeError("var parameter must be a str, list, or a tuple.")

    # Convert single string input to iterable
    if isinstance(letters, str):
        letters = [letters]

    # Count frequency
    result = {}
    for l in letters:
        if not isinstance(l, str) or len(l) == 0:
            continue  # ignore invalid entries
        result[l] = var.count(l)

    return result



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
    else:
    	return None



def Sprint(data: Any, delay: float = 0.5, end: str = " ") -> None:
    """Slow prints items in a list/tuple/dictionary."""
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"{key}: {value}", flush=True, end=end)
            time.sleep(delay)
    elif isinstance(data, (list, tuple, str)):
        for item in data:
            print(item, end=end, flush=True)
            time.sleep(delay)



def getabbr(text: str) -> str | None:
    """
    Returns the abbreviation of the given text.
    
    Notes: 
    • any word that starts with a capital letter will be ingnored
    • any non-standard symbol will be ignored
    
    >>> getabbr("information And communication tech") → 'ICT'
    """
    try:
        nt = ""
        for t in text.split():
            for ch in t[0]:
                if ch in strings.lower_letters:  # ignores non-standard symbols
                    nt += ch.upper()
                    break
        return nt
    except (AttributeError, TypeError, Exception, ValueError) as e:
        return e
        
            
                
                    
                        


class strings:
    """String-related utilities."""
    
    lower_letters: tuple[str, ...] = tuple(chr(i) for i in range(97, 123))
    
    upper_letters: tuple[str, ...] = tuple(chr(i).upper() for i in range(97, 123))
    
    ascii_symbols: tuple[str, ...] = tuple(chr(i) for i in range(33, 123) if not chr(i).isalnum())
    
    digits: tuple[int, ...] = tuple(range(10))

    @staticmethod
    def remove_letters(text: str, *letters: str) -> str:
        """
        Remove specific letters from a string.
        
        arguments:
        text -- the text to filter
        *letters -- unlimited amount of letters to delete

        >>> strings.remove_letters("wlatlchi", "i", "l") → 'watch'
        """
        filtered = [l for l in text if l not in letters]
        return ''.join(filtered)





class variable:
    """A toolkit for editing variables"""

    @staticmethod
    def deleteInd(var: str, var_ind: int = -1) -> str:
        """
        Delete a specific letter by index

        var -- the text
        var_ind -- the index of the letter, defaulted by -1 (last letter)
            
        >>> variable.Idelete("aktm", 1) → 'atm'
        """
        if var_ind < 0:
        	var_ind += len(var)
        return var[:var_ind] + var[var_ind+1:]


    @staticmethod
    def delete(var: str, letter: str, occurrences: int = 1) -> str:
        """
        Delete a letter by given occurrences
        
        arguments:
        var -- the text
        letter -- the targeted letter
        occurrences -- the occurrences of deleting the letter, defaulted by 1
            
        >>> variable.delete("messssy", "s", 2) → 'messy'
        """
        return var.replace(letter, "", occurrences)

    @staticmethod
    def insert(char: str, var: str, var_ind: int = -1) -> str:
        """
        Add a specific letter at a specific index.
        
        arguments:
        char -- the character
        var -- the text
        var_ind -- the index(placement) of the letter
        
        >>> variable.insert("d", "car", -1) → 'card'
        """
        return var[:var_ind] + char + var[var_ind:]

    @staticmethod
    def replace(var: str, var_ind: int, replacement: str) -> str:
        """
        Replace a letter by index.
        
        arguments:
        var -- the text
        var_ind -- the index of targeted letter
        replacement -- the replacer letter
        
        >>> variable.replace("burn", 1, "o") → 'born'
        """
        return var[:var_ind] + replacement + var[var_ind + 1:]

    @staticmethod
    def random_int(minimum: int, maximum: int) -> int:
        """Generates a random integer between two values"""
        return random.randint(minimum, maximum)




# Decorators:


def timer(func: Any) -> Any:
    """A decorator returning functions' elapsing time
    • Note: any function with this decorator won't return the code in the function, only the time taken.
    
    >>>
    	@timer
    	def timed():
    		for i in range(999999):
    			print(i)
    	
    	timed() → 6.5043
    """

    def wrapper(*args: Any, **kwargs: Any) -> None:
        start = time.time()
        with open(os.devnull, "w") as devnull:
            with contextlib.redirect_stdout(devnull), contextlib.redirect_stderr(devnull):
                try:
                    func(*args, **kwargs)
                except Exception:
                    end = time.perf_counter()
                    print(f"{end - start:.4f}")
                    raise
        end = time.perf_counter()
        print(f"{end - start:.4f}")

    return wrapper



def run_once(func: Any) -> Any | None:
    """A decorator preventing calling a function more than once
    >>>
    	@run_once
    	def temp():
    		print("Hello world")
    		
    	temp() → 'Hello world'
    	temp() → Exception: Function 'temp' can only run once.
    """
    called = False
    result = None
    def wrapper(*args, **kwargs):
        nonlocal called, result
        if not called:
            result = func(*args, **kwargs)
            called = True
        else:
            raise Exception(f"Function '{func.__name__}' can only run once.")
        return result
    return wrapper



def delayed(seconds: int) -> Any | None:
    """Delays the function when called for the given time."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            func(*args, **kwargs)
        return wrapper
    return decorator
    
    

def encrypted(func: Any) -> Any | None:
    """Encrypts the function to the base64 cipher.
    
    >>>
    	@encrypted
    	def example():
    		print("Hello world")
    	
    	example() → 'SGVsbG8gd29ybGQ='
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        try:
        	encoded = base64.b64encode(result.encode()).decode()
        except AttributeError:
        	return None
        return encoded
    return wrapper
 
 
