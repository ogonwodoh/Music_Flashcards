# Music_Flashcards
A quiz application for testing mastery of associating sound to a composer and song name

This application was made to study for the listening quizzes in MUSIX1001, An Introduction to Music at Columbia. The application is essentially a sound-enabled flashcard.

REQUIREMENTS:
	Have Python 2.7 installed. Instructions can be found <a href="https://www.python.org/downloads/"> here </a>.
	Have pygame for Python 2 installed. Instructions can be found <a href="https://www.pygame.org/wiki/GettingStarted"> here </a>.

To run the appplication type into your terminal: <pre> <code> python main.py </pre> </code>

There program will prompt you for one of three things:
  1) You can enter s so that you can add songs to your flashcard set. This creates a sqlite database entry for the song information (composer, song name, and file location of the mp3 file).
  2) You can enter f so that you can be quizzed on the songs in your flashcard set.
  3) You can press q to quit the program.
