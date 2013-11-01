Example 1
====

`print_hello.py`
----

This simple file introduces a lot of things we'll use over and over. 
We're introducing getting data in and out of files early because it will
simplify creating examples to test your code much easier.  If you can
read values from a file, you can test over and over and not have to
worry about making typos at a prompt.  And, since you're here because
you want to do something with data, this is how you'll get your data
into your program.  Why wait?

The `#` character marks the beginning of a comment, which extends to the
end of the line, and they are ignored by python.  See the comment after
`os.getcwd()`.

Many helpful things live in modules, and we take advantage of them when
we can

The `import os` command makes the functions inside the os module
available as `os.function_name()` -- for example `os.chdir()` changes to
the folder whose name appears inside the parentheses. Sometimes that can
be a function, or a function of a function.

It can be very convenient to be able to read things from the
environment, like home directory, username, etc.  Less important,
perhaps, on Windows.

Variables get created when you need them, as when we create `home_dir`
and `filename`

Python is full of objects.  When we open a file, a file object gets
created.  When we created `filename`, we created a string object.  An
object is a data container that has functions appropriate for that kind
of data.  The functions that are tied to an object are called _methods_.

The file object, `data_file`, has a method called `readlines()`, that
does what you'd think -- it reads the lines from the file.  The file
object has another method called `close()` that closes a file if it's
open.  An object is basically a variable -- `data_file` and `home_dir`
are both what are called _instances_ of an object, one a file object,
the other a string object.  To use a method, attach the method name to
the instance (variable name), as in `data_file.close()`.

You will want to print things, and that is done with the `print`
command. You can print literal text (as with the header), but you can
also print the values of variables.  The `print` command is pretty good
about knowing how to print different kinds of things.

On the line where we print the header, the `%s` is a placeholder for a
string, and it goes inside the quotes.  Then there is a `%` after the
formatting string (the stuff in the quotes) followed by either a single
object (in this case a string variable, `filename`) or a list of objects
which would appear inside either `()` or `[]`.  For example,

    print "Birthdate:  %d/%d/$d\n" % (day, month, year)

would print a birthdate separated by slashes, where `day`, `month`, and
`year` are numeric variables that contain the values to be printed.  The
first variable in the list goes into the first placeholder spot, the
second into the second, etc.

What's that `print "=" * 34` thing?  Python may change the meaning of
operators, like `+` and `*`, depending on the context in which they're
used. This is called _operator overloading_ by fancy people.  For
strings, multiplication means "repeat", so `"=" * 34` means repeat the
`=` 34 times.  Similarly,

    phrase = 'One word " + "or more"

"adds" two strings together to make a longer string (note, the space
between "word" and "or" has to be included inside one set of those
quotes).
