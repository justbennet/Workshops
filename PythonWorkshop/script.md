# Python workshop topic outline

## Topics

0.  Opening Canopy and a little bit about how to move around, using the file
	`print_hello.py`

    a. What are the Editor, Package manager
    
    b. Edit window, python shell window
    
    c. Syntax coloring, and why it can be a help

    d. Indention and meaning in python, automatic in the editor and the shell
 
	e. If the python shell prompt doesn't come back, it's still working.
		
0.  Modules, using the file `print_hello.py`
	a. `import os` and show them `os.getcwd()`, `os.chdir()`, `os.path.join()`,
	and `os.path.expanduser()`
	
	b. Typing `os.getcwd()` just prints it, whereas `pwd = os.getcwd()` saves
	the value into `pwd`
 
0.  Objects and methods, using the file `read_file.py`

	a. The file object, `f`
	
	b. The `readlines()` method

0.  Iterable objects and `for` loop, using the file `read_file.py`

	a. `for l in f:`
	
	b. Note the colon and the indentation change
	
	c. Lists are iterable, cf the `data` list, and so are strings
	
	d. indexing of lists, strings, etc.  What is `data[0]`?  `data[1]`?
	`data[-1]`?
	
	e. slices of lists and things, as in `data[-5:]` and `data[1:6]`
	
	f. `len(data)` and `len(data[0])`

0.  Being neat....  If you `open()` a file, you should `close()` a file

0.  How to read a `.csv` file using `read_csv.py` (note that rows
come out as lists).
 
0.  how to write a `try: ... exception:` block, using the file `except1.py`

	a. What is an exception?

	b. Basic structure:  `try:` ... `except <type>:` ... `except:`

	c. Python is full, and I do mean full (look for it on the web), of niceness.
	An example is how to open a file using
	
        with open("myfile.txt") as f:
        for line in f:
            print line,

	(which is in `exception2.py`) The nice part of that is that the file is
	closed automagically.

0.  show them `for` loops using the file `read_file.py`

    a. `for` with something that knows how to iterate (`for line in file:`)
    
    b. `for` with explicit limits using `range()`
    
    c. show a list comprehension; rewrite that as a `for` as an exercise
 
0.  how to grab a file from a URL, using the file `read_url.py`

	a. import `urllib`
	
	b. put the URL in a string
	
	c. the URL is treated much like a file, it has an `open()` method, and a
	`read()` method
	
	d. What did we get?  A really long string (99887 characters)
	
0.  tell them about lists and strings and show some methods, e.g.,
`str.split()`, `str.trim()`, `str.join()`, using `read_url.py`
 
0.  show them a simple if statement using `url_read3.p`
 
0.  tell them about dictionaries and show an example of one

