import tkinter as tk  # Import the main tkinter module
import tkinter.scrolledtext as tkst  # Import the scrolled text widget from tkinter

# Import custom modules
import track_library as lib  # Import the track library module which manages our music data
import font_manager as fonts  # Import the font manager module for consistent GUI appearance


def set_text(text_area, content):
    # This function updates the content of a text area widget
    text_area.delete("1.0", tk.END)  # Delete all existing content from line 1, character 0 to the end
    text_area.insert(1.0, content)  # Insert the new content starting at line 1, character 0


class TrackViewer():
    # This class creates and manages the Track Viewer GUI

    def __init__(self, window):
        # Constructor method - initializes the GUI elements

        # Configure the window size and title
        window.geometry("750x350")  # Set the window dimensions (width x height)
        window.title("View Tracks")  # Set the window title bar text
        window.configure(bg="light blue")  # Set the window background color

        # Create a button to list all tracks with an associated command
        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)  # Position button using grid layout

        # Create a label for track number entry
        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)  # Position label using grid layout

        # Create an entry field for track number input
        self.input_txt = tk.Entry(window, width=3)  # Width of 3 characters for track number
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)  # Position entry field using grid layout

        # Create a button to view a specific track with an associated command
        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)  # Position button using grid layout

        # Create a scrollable text area to display the list of tracks
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10,
                           pady=10)  # Position text area using grid layout

        # Create a text area to display detailed information about a specific track
        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)  # Position text area using grid layout

        # Create a label to display status messages
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10,
                             pady=10)  # Position label using grid layout

        # Automatically populate the track list when the window opens
        self.list_tracks_clicked()  # Call the method to display all tracks

    def view_tracks_clicked(self):
        # Event handler method for the View Track button

        key = self.input_txt.get()  # Get the track number from the entry field
        name = lib.get_name(key)  # Try to get the track name from the library

        if name is not None:  # If a track was found with this number
            # Retrieve more details about the track
            artist = lib.get_artist(key)  # Get the artist name
            rating = lib.get_rating(key)  # Get the track rating
            play_count = lib.get_play_count(key)  # Get the play count

            # Format all track details into a multi-line string
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"

            # Display the track details in the track text area
            set_text(self.track_txt, track_details)
        else:  # If no track was found with this number
            # Display an error message
            set_text(self.track_txt, f"Track {key} not found")

        # Update the status label to show the button was clicked
        self.status_lbl.configure(text="View Track button was clicked!")

    def list_tracks_clicked(self):
        # Event handler method for the List All Tracks button

        track_list = lib.list_all()  # Get the formatted list of all tracks
        set_text(self.list_txt, track_list)  # Display the track list in the list text area

        # Update the status label to show the button was clicked
        self.status_lbl.configure(text="List Tracks button was clicked!")


if __name__ == "__main__":  # Only runs when this file is run as a standalone
    window = tk.Tk()  # Create a TK object for the main window
    fonts.configure()  # Configure the fonts for consistent appearance
    TrackViewer(window)  # Create the TrackViewer GUI using the window
    window.mainloop()  # Run the window main loop, reacting to button presses, etc