from pygame import mixer
import sqlite3

feedback_list = []

def add_song(database, conn):
	file_location = raw_input("What is the file path for the song you want to add? ")
	song_name = raw_input("What is the name of the song? ")
	composer = raw_input("Who is the composer of the song? ")
	
	database.execute("INSERT INTO songs VALUES ( ?, ?, ? )", (song_name.lower(), composer.lower(), file_location))
	conn.commit()
	print(song_name + " successfully inserted")

def quiz(database):
	global feedback_list
	num_correct = 0
	mixer.init()
	
	database.execute("SELECT * FROM songs")
	all_rows = database.fetchall()
	
	for song_info in all_rows:
		mixer.music.load(song_info[2])
		mixer.music.play()
		response = raw_input("Press s to stop playback, press any other key to move onto the quiz. ")

		if(response == 's'):
			mixer.music.stop()

		composer_name_raw = raw_input("Who composed this song? ")
		song_name_raw = raw_input("What is the name of this song? ")

		composer_name = composer_name_raw.lower()
		song_name = song_name_raw.lower()

		if(composer_name == song_info[1] and song_name == song_info[0]):
			print("Success! The name of the song is " + song_info[0] + " and the composer is " + song_info[1])
			num_correct = num_correct + 1
			feedback = ""
		elif(composer_name != song_info[1] and song_name == song_info[0]):
			print("Your answer of composer " + composer_name + " is incorrect. The answer is "+song_info[1] + ". Your answer of song " + song_info[0]+\
" is correct.")
			feedback = "Remembering that " + song_info[1] + " composed " + song_info[0]
		elif(composer_name == song_info[1] and song_name != song_info[0]):
			print("Your answer of composer " + composer_name+" is correct. Your answer of song " + song_info[0]+" is incorrect. The correct answer is "\
+ song_info[0]+".")
			feedback = "Remembering that " + song_info[1] + " composed " + song_info[0]
		else:
			print("Your answer of composer " + composer_name+ "is incorrect. The correct answer is " + song_info[1] + ". Your answer of song name "+ \
song_name[0] + " is incorrect. The correct answer is " + song_info[0]+ ".")
			feedback = "Remembering that " + song_info[1] + " composed " + song_info[0]
		
		if(feedback != ""):
			feedback_list.append(feedback)
		mixer.music.stop()

	print("SCORE: " + str(num_correct) + "/" + str(len(all_rows)))
	if(len(feedback_list) > 0):
		print("Work on:")
		for feedback_str in feedback_list:
			print("\t" + feedback_str) 

def main():
	conn = sqlite3.connect('song_database.sqlite')	
	database = conn.cursor()
	conn.execute('CREATE TABLE IF NOT EXISTS songs (song_name text, composer_name text, file_location text)')
	ans = raw_input("Press s to add a song, press f to quiz, or press q to quit. ")
	while(ans != 'q'):
		if(ans == 's'):
			add_song(database,conn)
		elif (ans == 'f'):
			quiz(database)
		else:
			print("Please enter a valid input")

		ans = raw_input("Press s to add a song, press f to quiz, or press q to quit. ")

	database.close()

if __name__ == "__main__": main()
