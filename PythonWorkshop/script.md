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
	
	e. slices of lists and things, as in `data[-5:]` and `data[1:6]`; how
	many items in `data[1:6]`?
	
	f. `len(data)` and `len(data[0])`
	
	g. `for` with explicit limits using `range()`

	h. List comprehension; it's a shorthand version of a `for` loop

0.  Be neat....  If you `open()` a file, you should `close()` a file

0.  How to read a `.csv` file using `read_csv.py`

	a. The file is opened as usual, then a `csv_reader` object is created,
	which iterates the same way a file object does.

	b. Note that the rows come out as lists, not strings.  Usually nicer
	for data.
	
	c. Because the elements are list, we have to use `data.append(row)`
	What happens if we use just `data = row`?  How about `data += row`?
 
0.  how to write a `try: ... exception:` block, using the file `except1.py`

	a. What is an exception?

	b. Basic structure:  `try:` ... `except <type>:` ... `except:`
	
0.	Exception handler to break out of loops, using `exception2.py`

	a. `while` loop with an exception to `break` at KeyboardInterrupt

	b. An example is how to open a file using
	
        with open("myfile.txt") as f:
        for line in f:
            print line,

	Use `with ... as` and the file is closed automagically.
 
0.  How to grab a file from a URL, using the file `read_url.py`

	a. import `urllib`
	
	b. put the URL in a string
	
	c. the URL is treated much like a file, it has an `open()` method, and a
	`read()` method
	
	d. What did we get?  A really long string (99887 characters)

0.	How to grab several files when part of the URL varies nicely, using
`read_url2.py`

	a. Strategy:  When developing something that loops, use a controlled
	subset, i.e., `range(0:2)` here.
	
0.  Show them a simple if statement using `url_read3.py`

	a. Each month comes with it's own column labels.  We want to only
	keep one set.  Use an `if`.  Note the `==` and that python takes
	care of you if you forget and use only one.
	
	b. Do they notice anything odd about the data?  What year is Jan and
	Dec data for...?  Check your data!

0.  Regular expressions, using `re_example.py`

0.  Dictionary, using  `re_example.py`

	a. Get an error if you try to increment a nonexistent value, so we
	`try...except` to finesse that.
	
	b. Find the exception your trying to catch by reading the default error.

0.	A quick survey of pandas, using `bike_data.py`

0.  Some additional string methods, e.g., `str.split()`, `str.trim()`,
`str.join()`, using `read_url1.py`
 
