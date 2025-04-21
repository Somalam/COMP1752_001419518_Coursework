import tkinter as tk
import track_library as lib
import font_manager as fonts


class TrackListCreator():

    def __init__(self, window):

        # Configure the window size and title
        window.geometry("750x600")
        window.title("Create Track List")
        window.configure(bg="light blue")

        # Initialize empty playlist list
        self.playlist = []

        # Create a label for search
        search_lbl = tk.Label(window, text="Search By Name Or Artist")
        search_lbl.grid(row=0, column=0, padx=10, pady=10)

        # Create an entry field for search input
        self.search_txt = tk.Entry(window, width=20)
        self.search_txt.grid(row=0, column=1, padx=10, pady=10)

        # Create a button to search tracks
        search_btn = tk.Button(window, text="Search", command=self.search_tracks)
        search_btn.grid(row=0, column=2, padx=10, pady=10)

        # Create a text widget to display search results
        self.search_txt_widget = tk.Text(window, width=48, height=5)
        self.search_txt_widget.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Create a label for track number entry
        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=2, column=0, padx=10, pady=10)

        # Create an entry field for track number input
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=2, column=1, padx=10, pady=10)

        # Create a button to add a track to the playlist
        add_track_btn = tk.Button(window, text="Add Track", command=self.add_track_clicked)
        add_track_btn.grid(row=2, column=2, padx=10, pady=10)

        # Create a button to play the playlist
        play_btn = tk.Button(window, text="Play Playlist", command=self.play_clicked)
        play_btn.grid(row=3, column=0, padx=10, pady=10)

        # Create a button to reset the playlist
        reset_btn = tk.Button(window, text="Reset Playlist", command=self.reset_clicked)
        reset_btn.grid(row=3, column=1, padx=10, pady=10)

        # Create a text area to display the playlist contents
        self.playlist_txt = tk.Text(window, width=48, height=12, wrap="none")
        self.playlist_txt.grid(row=4, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Create a label to display status
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=5, column=0, columnspan=3, sticky="W", padx=10, pady=10)

    def search_tracks(self):
        # Clear search results
        self.search_txt_widget.delete("1.0", tk.END)

        # Get search query
        query = self.search_txt.get().strip().lower()

        # If query is empty, show status
        if not query:
            self.status_lbl.configure(text=f"No tracks found matching '{query}'")
            return

        # Search for tracks matching query
        matches_found = False
        for key, item in lib.library.items():
            # Search by track number, name, or artist
            if (query in key.lower() or
                    query in item.name.lower() or
                    query in item.artist.lower()):
                self.search_txt_widget.insert(tk.END, f"{key}: {item.name} - {item.artist}\n")
                matches_found = True

        # Update status based on search results
        if not matches_found:
            self.status_lbl.configure(text=f"No tracks found matching '{query}'")
        else:
            self.status_lbl.configure(text=f"Found matching tracks")

    def validate_track_number(self, track_number):

        # Check if track number is empty
        if not track_number:
            self.status_lbl.configure(text="Error: Track number cannot be empty")
            return False

        # Check if track number contains only digits
        if not track_number.isdigit():
            self.status_lbl.configure(text="Error: Track number must contain only digits")
            return False

        # Check if track number exists in the library
        if lib.get_name(track_number) is None:
            self.status_lbl.configure(text=f"Error: Track {track_number} not found in library")
            return False

        # All validation passed
        return True

    def add_track_clicked(self):
        key = self.input_txt.get()  # Get the track number from the entry field

        # Validate the track number before adding to playlist
        if not self.validate_track_number(key):
            return  # Exit if validation failed

        # Add the track number to the playlist
        self.playlist.append(key)
        # Update the playlist display
        self.update_playlist_display()
        # Update status message
        self.status_lbl.configure(text=f"Track {key} added to playlist!")

    def update_playlist_display(self):
        playlist_content = ""  # Initialize empty string for playlist content

        # Loop through each track in the playlist
        for key in self.playlist:
            name = lib.get_name(key)  # Get track name
            artist = lib.get_artist(key)  # Get artist name
            # Add formatted track info to playlist content
            playlist_content += f"{key} {name} - {artist}\n "

        # Update the playlist text area with the new content
        self.playlist_txt.delete("1.0", tk.END)  # Clear existing content
        self.playlist_txt.insert("1.0", playlist_content)  # Insert new content

    def play_clicked(self):
        # Check if playlist is empty
        if not self.playlist:
            self.status_lbl.configure(text="Playlist is empty!")
            return  # Exit if playlist is empty

        # Loop through each track in the playlist
        for key in self.playlist:
            # Increment the play count for the track in the library
            lib.increment_play_count(key)

        # Update status message
        self.status_lbl.configure(text="Playlist played successfully!")

    def reset_clicked(self):
        # Clear the playlist
        self.playlist = []
        # Clear the playlist text area
        self.playlist_txt.delete("1.0", tk.END)
        # Update status message
        self.status_lbl.configure(text="Playlist has been reset!")


if __name__ == "__main__":  # Only runs when this file is run as a standalone
    window = tk.Tk()  # Create a TK object for the main window
    fonts.configure()  # Configure the fonts for consistent appearance
    TrackListCreator(window)  # Create the TrackListCreator GUI using the window
    window.mainloop()  # Run the window main loop, reacting to button presses, etc