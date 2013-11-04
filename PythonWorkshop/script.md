# Python workshop topic outline

## Topics

0.  Opening Canopy and a little bit about how to move around, using the file
	`print_hello.py`

    a. Editor, Package manager
    
    b. Edit window, python shell window
    
    c. Syntax coloring

    d. Indention and meaning
 
0.  Modules; `import os` and show them `os.getcwd()`, `os.chdir()`,
`os.path.join()`, and `os.environ[]`, using the file `print_hello.py`
 
0.  Objects (file object, string object) and methods, using the
file `read_hello.py` and the file object and `f.readlines()` method.

0.  Being neat....  If you `open()` a file, you should `close()` a file
 
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
 
0.  tell them about dictionaries and show an example of one
 

0.  show them a simple if statement
 
0.  how to open a csv and a gzip file
 


0.  Opening a text file and reading with `f.readline()`, `readlines()`,
and with `for l in f:`.