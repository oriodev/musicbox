# MUSICBOX
#### Video Demo:  https://youtu.be/jgt6p1JETts

#### Description:

MUSICBOX is a python program that utilises Flask and the Spotify API to generate a playlist of music recommendations based on artists that the user already enjoys. It compiles the top 10 songs from each recommended artist into a playlist that the user can add to their Spotify account. They can also choose a custom name for the playlist prior to generation.

##### WALKTHROUGH

The user inputs three artists that they already like and chooses to generate either 5, 10 or 15 receommendations based on those three artists. This generation is performed through spotify's 'find related artists' API call which returns a number of related artists from each of the three inputted artists. The program then randomly chooses 5, 10 or 15 of these artists, making sure each one is unique, and displays them in a grid on the next page, along with a photo of the artist, the name and a link to their spotify page. 

Each artist recommendation has a checkbox beneath their photo. The user can select the artists that they like the look of and the program will use the Spotify API to gather each artist's top 10 most popular songs. These songs will then be compiled into a playlist. The user can then enter a custom name for the playlist and if they wish to add the playlist to their Spotify account then they can press that button and do so. The playlist will then be added to the user's account, where they can play the songs and explore new music that is similar to the music they already enjoy.

##### FILE WALKTHROUGH

app.py is the main file that holds the routes and main logic. It has four functions, one that calls index.html (the front page), one that calls results.html (the page that displays the music recommendations), one that calls playlist.html (the page that takes the playlist name and playlist generation button) and one that calls confirmation.html (the page that confirms the playlist has been generated and displays the playlist cover and name). The logic on this page determines what is done with the input recieved via the forms. It relies heavily on calling python functions from main.py, where the majority of the real background work is done. It also utilises sessions to pass data between routes.

main.py is the main logic file. It holds all of the background code needed to call the Spotify API and manipulate the data into something that can be displayed on the front end. There are a number of functions within it. get_artist_id takes the name of an artist, checks if that artist is in the Spotify database, and if it is, returns that artist's artist ID. get_related_artists finds the related artists of an artist and returns their name, link and image. get_all_related_artists calls get_related_artists on every inputted artist and builds a dictionary of the first ten related artist from all three inputted artists. It then calls select_random_artists to return a random assortment of artists from that list, totalling the number of recommendations requested by the user. select_random_artists uses the random module to return a dictionary of random recommendations from the list of every related artist. It also checks that there are no duplicates within the list, so that the user is getting x number of unique recommendations every time. There are also four functions in this file that generate the new playlist, adds songs to the playlist, and returns the playlist cover after it's creation. These functions are significantly more straightforward and largely just consist of API calls. 

There are also html and css files used to style the front end, display the recommendations and hold the forms needed to gather the primary user input.

##### DESIGN CHOICES

This program was implemented with Python, Flask, Spotipy, and a number of other modules including dotenv allowing the secret API code to not be accessible to the public. Spotipy was used to accelerate the development process as the Spotify API documentation is unclear and connecting to the API directly is notoriously difficult. Spotipy reduces that effort to a single line of code, allowing the access token and user authentication to be recieved and used easily.

##### USE

To use the program, the user will need a spotify account. They will need to create a .env file and enter a client_id, client_secret, redirect_uri and username there. Once this is done the rest of the program should run smoothly.
