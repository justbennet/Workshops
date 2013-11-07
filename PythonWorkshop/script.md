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
	
	b. Explain 'namespace'.
	
	c. Why use `os.path.expanduser()`?  Wrote these on Mac, can still
	run on Windows with little or no change.
	
	d. Typing `os.getcwd()` just prints it, whereas `pwd = os.getcwd()` saves
	the value into `pwd`
	
	e. The file object, `data_file`
	
	f. The `readlines()` method -- expand on what is an object and a method

	g. `print` and `print "%s" & x` -- translates number into string:
	demonstrate.
	
	h. Strings and multiplication `"=" * 32`
	
	i. Strings are objects, too, even a literal like `"="`
	
	j. When the script is run, it prints out the list of the contents.
	Explain the list format:
	`['Well,\n', '\n', 'Hello there, world.\n']`
	List is surrounded by brackets; elements in list comma separated and
	quoted; EOL is treated like any other character.
 
0.  Iterable objects and `for` loop, using the file `read_file.py`

	a. `for l in f:` -- why use `for` instead of `readlines()`?  So you
	can do things to each line as it passes by, e.g., strip off the EOLs.
	Add a line to strip before appending.  NOTE -- Canopy adjusts your
	indent for you.  Can add a line, or you can
	`data.append(line.strip())`
	
	b. Note the colon and the indentation change -- indention has meaning!
	
	c. Lists are iterable, cf. the `data` list, and so are strings
	
	d. indexing of lists, strings, etc.  What is `data[0]`?  `data[1]`?
	`data[-1]`?  Print last line.  What will be the time on `data[-3]`?
	
	e. slices of lists and things, as in `data[-5:]` and `data[1:6]`; how
	many items in `data[1:6]`?  What happens when nothing before/after
	the colon?  Careful with `range()`, which uses a command and slice
	which uses a colon.
	
	f. `len(data)` and `len(data[0])`; show them the help for functions and
	methods.
	
	g. `for` with explicit limits using `range()`

	h. List comprehension; it's a shorthand version of a `for` loop

0.  Be neat....  If you `open()` a file, you should `close()` a file

0.  How to read a `.csv` file using `read_csv.py`

    a. Typically, you want items from a line of data as a list -- think
    variable.  It's a pain to extract them manually.  We have `.csv` files
    to make it easier.

	b. The file is opened as usual, then a `csv_reader` object is created,
	which iterates the same way a file object does.

	c. Note that the rows come out as lists, not strings.  Usually nicer
	for data.
	
	d. Because the elements are list, we have to use `data.append(row)`
	What happens if we use just `data = row`?  How about `data += row`?
	
	e. Completing the exercise
	`subset = [ line[0], line[6], line[14], line[-1] ]`
 
0.  how to write a `try: ... exception:` block, using the file `except1.py`

	a. What is an exception?

	b. Basic structure:  `try:` ... `except <type>:` ... `except:`
	
	c. Copy the line to get the file name and then read it.  Look at the
	error message.  See where the error (IOError) is listed?  That's
	what you put in your `except <E>:`
	
0.	Exception handler to break out of loops, using `exception2.py`

	a. `while` loop with an exception to `break` at KeyboardInterrupt

	b. An example is how to open a file using
	
        with open("myfile.txt") as f:
        for line in f:
            print line,

	Use `with ... as` and the file is closed automagically.
 
0.  How to grab a file from a URL, using the file `read_url1.py`

	a. import `urllib`
	
	b. put the URL in a string
	
	c. the URL is treated much like a file, it has an `open()` method, and a
	`read()` method
	
	d. What did we get?  A really long string (99887 characters)

0.	How to grab several files when part of the URL varies nicely, using
`read_url2.py`

	a. Strategy:  When developing something that loops, use a controlled
	subset, i.e., `range(0:2)` here.

    b. Note that `year` and `month` are numbers, so they have to be
    converted to strings to be used in the url.
	
0.  Show them a simple if statement using `url_read3.py`

	a. Each month comes with it's own column labels.  We want to only
	keep one set.  Use an `if`.  Note the `==` and that python takes
	care of you if you forget and use only one.
	
	b. Do they notice anything odd about the data?  What year is Jan and
	Dec data for...?  Check your data!

0.  Modified version to adjust the year for Dec in `read_url4.py`

    a. The if that's there works.  Would it be better to make it like this,
    so the URL is only written once (saving typos)?  It does the same thing.

        if month = 12:
            year = year - 1
        url = (site + "/climateData/bulkdata_e.html?format=csv&stationID=5415&Year="
            + str(year) + "&Month=" + str(month)
            + "&Day=14&timeframe=1&submit=Download+Data")

0.  Regular expressions, using `re_example.py`

    a. What are REs?  They are patterns that can be matched.
    
    b. You write the pattern and compile it into an RE object, which is
    then used to examine a string for a match.  `re.match()` starts at the
    beginning of the string and looks for a match.  `re.search()` looks
    everywhere in the string.
    
    c. Note that parentheses are used to create `group()` elements, which
    can then be extracted from the match object.  Must escape the `()` if
    you mean to match them.
    
    d. `\d{2}` means two numbers; `\w+` means one or more words; `\S+` means
    one or more things that don't contain spaces (needed because of hyphens
    and underscore characters).

0.  Dictionary, using  `re_example.py`

    a. What is a dictionary?  It's a list where the items are labelled so
    you can refer to them by name rather than position.
    
    b. Created with curly braces.
    
    c. Referred to with `dict_name[key_name] = value` where `key_name` can
    be a variable or a literal.  Key can be a number or a string.  Get
    keys back out with `dict_name.keys()`; check for existence of a key with
    `usage.has_key()`

	a. Get an error if you try to increment a nonexistent value, so we
	`try...except` to finesse that.
	
	b. Find the exception you're trying to catch by reading the default error
	produced when you try to modify a key that doesn't exist.
	`usage[feature] += 1` when `usage[feature]` doesn't yet exist.
	
	f. `usage.has_key('MATLAB')` is a boolean after `re_example.py` has run.

0.	A quick survey of pandas, using `bike_data.py`
 
