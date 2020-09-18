#!/usr/bin/env python3

#
# Here are some examples to use varaiables, strings, and comments.
#
def main():
    # Here I will show an example of a variable and an example of how to use it:
    num1 = 1
    num2 = 2
    print(num1 + num2)
    # Output: 3

    # Here I will show an example of a string and an example of how to use it:
    str1 = "Python"
    str2 = "Programming"
    str3 = "is"
    str4 = "cool!"
    print('{} {} {} {}'.format(str1, str2, str3, str4))
    # Output: Python Programming is cool!
     
    # Here I will show examples of comments:

    # This itself is a comment. Python ignores these but, these are to
    # understamd the code better. As you can see this is also a multistring
    # comment.

    """
    This is another way to make a comment.

    """


if __name__ == "__main__":
    main()
