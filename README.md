**HANGMAN GAME**

Hangman is a well-known game where one player thinks of a word and the other player tries to guess it by suggesting letters with a fixed number of guesses. One player (in this case the program) presents a sequence of dashes representing each letter of the word, along with a character as a starting point.A word game in which one player has to guess a word that the other player has thought of, by guessing the letters in it. Every time they guess a wrong letter, part of a picture of a person being hanged is drawn, and if the picture is completed the person guessing has lost.
Assuming that a greedy algorithm does lead to getting the word in the fewest number of incorrect guesses, the optimal strategy would be to always pick the letter that has the highest frequency out of all possible words (i.e. similar to what you had with (# words with letter)/(# possible words) ), where the possible words are all the words in the word list that a) don't have any of the letters that were incorrect and b) have the letters in the positions that were correct. How fast the possible words can be updated depends on how much precomputation you're willing to do beforehand.

First, we will ask for the name of the user. We will take the user input using the input() method. After execution, the input() method takes the input from the user and returns a string.
Next, we will select a word and ask the user to start guessing the characters in the word.
We will also define the maximum number of attempts the user can take.
Now, we will use a while loop to repeatedly ask the user to guess the character until the attempts are exhausted.
Inside the while loop, if the user guesses the correct character. We will include it in the response. Otherwise, we will notify the user that they made a mistake.
If the user is able to guess all the characters of the word within the maximum number of attempts, they win the game.
If the user exhausts all their attempts before guessing the entire word, they lose.
The logic behind this game is one player thinks of a word and the other tries to guess it by suggesting the letters. The word to guess is represented by a row of dashes, giving the number of letters. If the guessing player suggests a letter which occurs in the word, the program writes it in all its correct positions.

**URL SHORTENER**

The pyshorteners module is used by developers to generate short URLs, while the Bitly API module generates short URLs and provides more robust functions like clicks per URL, locations of clicked URLs, customization of URLs, and more.URLs can be extremely long and not user-friendly. This is where a URL shortener can come in handy. A URL shortener reduces the number of characters in a URL, making it easier to read, remember, and share. By following this step-by-step project, you'll build a URL shortener with Python and FastAPI.A URL shortener is an app that converts a long URL into a short URL. The idea is to minimize the web page address into something that's easier to remember and track. Typically, it shortens the website's address and adds a random combination of letters and numbers.


