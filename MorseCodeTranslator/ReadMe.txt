Morse code is a method of transmitting text information as a series of on-off tones, lights, or clicks that can be directly understood
by a skilled listener or observer without special equipment. It is named for Samuel F. B. Morse, an inventor of the telegraph.

Algorithm:
---------------
It is very simple .
Step1:You have to create a dictionary for each alphabet as the key and
      it's corresponding morse code as the value.
Step2:Then values of the keys can be accessed

Encryption
---------------
1.In encryption we extract each character (ignoring space)from a word
 and match it with its corresponding morse code in the dictionary.
2.Store the morse code in a string and each time we will add a space to
 our string and the next character's morse code.
3.While encoding text into morse code , we should add a space between
  every character and 2 spaces in between every word.
4.If the character is a space then add another space to the string .
  We repeat this process till we traverse the string .

Decryption:
--------------

1.In case of decryption, we start by adding a space at the end of the string
 to be decoded (this will be explained later).
2.Now we keep extracting characters from the string till we are not getting any space.
3.As soon as we get a space we look up the corresponding English language character to
the extracted sequence of characters (or our morse code) and add it to a variable which will store the result.
4.Remember keeping track of the space is the most important part of this decryption process.
 As soon as we get 2 consecutive spaces we will add another space to our variable containing the decoded string.
5.The last space at the end of the string will help us identify the last sequence of morse code characters
(since a space acts as a check for extracting characters and start decoding them).

GUI
---------
Here we used tkinter for the user interface and ease of use
