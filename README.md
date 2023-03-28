# MUSICBOX
#### Video Demo:  <URL HERE>
#### Description:

MUSICBOX is a program that utilises the Spotify API to generate musical artist recommendations for the user based on artists that they already enjoy and then compiles the top 10 songs from those artists into a playlist that the user can then add to their spotify account. They can also choose a custom name for the playlist prior to generation.

WALKTHROUGH

The user inputs three artists that they already like and chooses to generate either 5, 10 or 15 receommendations from those three artists. This generation is performed through spotify's 'find related artists' API call which returns a number of related artists from each of the three inputted artists. The program then randomly chooses 5, 10 or 15 of these artists, making sure each one is unique, and displays them in a grid on the next page, along with a photo of the artist, the name and a link to their spotify page. 

Each artist recommendation has a checkbox beneath their photo and name. The user can select the artists that they like the look of and the program will use the Spotify API to gather each artist's top 10 most popular songs. These songs will then be compiled into a playlist. The user can then enter a custom name for the playlist and if they wish to add the playlist to their spotify account then they can press that button and do so. The playlist will then be added to the user's account, where they can play the songs and explore new music that is similar to the music they already enjoy.

##### File Walkthrough

app.py is the main file that holds the routes and main logic. It has two functions, one that calls index.html (the front page) and one that calls results.html (the page that displays the music recommendations). The logic on this page determines what is done with the input recieved via the forms. It relies heavily on calling python functions from main.py, where the majority of the real background work is done. It also utilises sessions to pass data between routes.

main.py is the main logic file. It holds all of the background code needed to call the Spotify API and manipulate the data into something that can be displayed on the front end. There are a number of functions within it. get_artist_id takes the name of an artist, checks if that artist is in the Spotify database, and if it is, returns that artist's artist ID. get_related_artists finds the related artists of an artist and returns their name, link and image. get_all_related_artists calls get_related_artists on every inputted artist and builds a dictionary of the first ten related artist from all three inputted artists. It then calls select_random_artists to return a random assortment of artists from that list, totalling the number of recommendations requested by the user. select_random_artists uses the random module to return a dictionary of random recommendations from the list of every related artist. It also checks that there are no duplicates within the list, so that the user is getting x number of unique recommendations every time.

There are also html and css files used to style the front end, display the recommendations and hold the forms needed to gather the primary user input.

##### Design Choices

This program was implemented with Python, Flask, Spotipy, and a number of other modules including dotenv allowing the secret API code to not be accessible to the public. Spotipy was used to accelerate the development process as the Spotify API documentation is unclear and connecting to the API directly is notoriously difficult. Spotipy reduces that effort to a single line of code, allowing the access token to be recieved and used easily. 
