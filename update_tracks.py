import tkinter as tk 
import track_library as lib  
import font_manager as fonts  


class TrackUpdater():
    
    def __init__(self, window):

        # Configure the window size and title
        window.geometry("500x300")  
        window.title("Update Tracks")  
        window.configure(bg="light blue")

        # Create a label for track number entry
        track_lbl = tk.Label(window, text="Enter Track Number")
        track_lbl.grid(row=0, column=0, padx=10, pady=10)  

        # Create an entry field for track number input
        self.track_txt = tk.Entry(window, width=3)  
        self.track_txt.grid(row=0, column=1, padx=10, pady=10)  

        # Create a label for rating entry
        rating_lbl = tk.Label(window, text="Enter New Rating (1-5)")
        rating_lbl.grid(row=1, column=0, padx=10, pady=10)  

        # Create an entry field for rating input
        self.rating_txt = tk.Entry(window, width=3)  
        self.rating_txt.grid(row=1, column=1, padx=10, pady=10)  

        # Create a button to update the track rating
        update_btn = tk.Button(window, text="Update Rating", command=self.update_rating_clicked)
        update_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Create a text area to display the track details
        self.result_txt = tk.Text(window, width=40, height=4, wrap="none")
        self.result_txt.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Create a label to display status messages
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def validate_track_number(self, track_num):

        # Check if track number is empty
        if not track_num:
            self.status_lbl.configure(text="Error: Track number cannot be empty")
            return False
            
        # Check if track number contains only digits
        if not track_num.isdigit():
            self.status_lbl.configure(text="Error: Track number must contain only digits")
            return False
            
        # Check if track number exists in the library
        if lib.get_name(track_num) is None:
            self.status_lbl.configure(text=f"Error: Track {track_num} not found in library")
            return False
            
        # All validation passed
        return True
        
    def validate_rating(self, rating_str):

        # Check if rating is empty
        if not rating_str:
            self.status_lbl.configure(text="Error: Rating cannot be empty")
            return False, None
        
        # Check if rating contains only digits
        if not rating_str.isdigit():
            self.status_lbl.configure(text="Error: Rating must be a number")
            return False, None
        
        # Convert rating string to integer
        rating_int = int(rating_str)

        # Check if rating is within valid range (1-5)
        if rating_int < 1 or rating_int > 5:
            self.status_lbl.configure(text="Error: Rating must be between 1 and 5")
            return False, None
        
        # Return valid rating as integer
        return True, rating_int
                                
    def update_rating_clicked(self):

        key = self.track_txt.get()  # Get the track number from the entry field
        rating_str = self.rating_txt.get()  # Get the rating string from the entry field
        
        # Validate the track number
        if not self.validate_track_number(key):
            self.result_txt.delete("1.0", tk.END)  # Clear result text area on error
            return  # Exit if validation failed
            
        # Validate the rating
        valid, rating = self.validate_rating(rating_str)
        if not valid:
            self.result_txt.delete("1.0", tk.END)  # Clear result text area on error
            return  # Exit if validation failed
            
        # Update the track rating in the library
        lib.set_rating(key, rating)
        
        # Get track details to display
        name = lib.get_name(key)  # Get track name
        play_count = lib.get_play_count(key)  # Get play count
        
        # Format track details
        track_details = f"Track: {name}\nNew Rating: {rating}\nPlay Count: {play_count}"
        
        # Update the result text area with track details
        self.result_txt.delete("1.0", tk.END)  # Clear existing content
        self.result_txt.insert("1.0", track_details)  # Insert new content
        
        # Update status message
        self.status_lbl.configure(text=f"Rating updated for track {key}")


if __name__ == "__main__":  # Only runs when this file is run as a standalone
    window = tk.Tk()  # Create a TK object for the main window
    fonts.configure()  # Configure the fonts for consistent appearance
    TrackUpdater(window)  # Create the TrackUpdater GUI using the window
    window.mainloop()  # Run the window main loop, reacting to button presses, etc