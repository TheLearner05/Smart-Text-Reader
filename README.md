# Smart-Text-Reader

Final Year Project for BE Biomedial Engineering

This Smart Text Reader mainly focused on blind students who are unable to read n study from books.

Main idea is that text from page of book is detected and recognized and later it is
converted into speech by textToSpeech. Then using rpi, this audio can be given as output
via headfone to blind students.

Steps in the project:

0)Detection of Page Infront of student 
to get proper contour all 4 corners of book must be visible.
1)Deskewing the page
2)Detection of Text Blocks, paragraphs, headings,etc
3)Deskewing the Text Blocks if required
4)Preprocess the image so that pytesseract will work accuractly
5)conversion of text from image into string using Pytesseract
6)Performing text to speech on extraxted text using gttps or pyttsx library
7)Giving this speech input to RaspberryPi
8)Giving the speech as output via headphone using RaspberryPi.

Hello

(Please add if something is missed or needs to be improved)
