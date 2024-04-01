import tkinter as tk
from tkinter import ttk
from tkinter import END, filedialog, messagebox, colorchooser
import pygame
import os
import time

def second():

    global current_time, current_song, songs, MUSIC_END, paused
    # Functions for the Buttons 
    # ---------------------------------------------------------------------------------------------------------------------

    def fast_reverse():
        print('Reversed 5 seconds')
        global current_song, paused, current_time

        fast_reverse_time = 5
        playing_time = pygame.mixer.music.get_pos()/1000
        time = float(playing_time-fast_reverse_time)

        # pygame.mixer.music.rewind()

        # pygame.mixer.music.set_pos(float(playing_time+fast_reverse_time))
        pygame.mixer.music.play(0, current_time+time)
        current_time += time

        print(playing_time)
        print(fast_reverse_time)
        print(time)
        print(current_time)

    def previous_music():
        
        global current_song, paused

        try:
            songlist.selection_clear(0, END)
            songlist.selection_set(songs.index(current_song)-1)
            current_song = songs[songlist.curselection()[0]]
            play_music()

        except Exception:
            pass

    def pause_music():
        
        global current_song, paused

        if not paused:
            pygame.mixer.music.pause()
            paused = True

        else:
            pygame.mixer.music.unpause()
            paused = False

    def play_music():
        
        global current_song, paused, current_time
        current_song = songs[songlist.curselection()[0]]


        if not paused: # If not paused(false) == True, it will run
            pygame.mixer.music.load(os.path.join(new_window.directory, current_song))
            pygame.mixer.music.play()
            current_time = 0.0
            # Testing code
            queue_music()
            # Testing code

        else:
            # pygame.mixer.music.load(os.path.join(new_window.directory, current_song))
            # pygame.mixer.music.play(-1)
            pygame.mixer.music.unpause()
            paused = False
            queue_music()

    def play_music_special():
        
        global current_song, paused
        current_song = songs[songlist.curselection()[0]]


        if not paused: # If not paused(false) == True, it will run
            pygame.mixer.music.load(os.path.join(new_window.directory, current_song))
            pygame.mixer.music.play()

        else:
            pygame.mixer.music.load(os.path.join(new_window.directory, current_song))
            pygame.mixer.music.play()
            pygame.mixer.music.unpause()
            paused = False

    def next_music():

        global current_song, paused

        index = songs.index(current_song)

        try:
            if index < len(songs) - 1:
                songlist.selection_clear(0, END)
                songlist.selection_set(songs.index(current_song)+1)
                current_song = songs[songlist.curselection()[0]]
                play_music()

            elif index == len(songs) - 1:
                songlist.selection_clear(0, END)
                songlist.selection_set(0)
                current_song = songs[songlist.curselection()[0]]
                play_music()

        except Exception:
            pass

    def fast_forward():
        print('Forwarded 5 seconds')
        global current_song, paused, current_time

        


        fast_forward_time = 5
        playing_time = pygame.mixer.music.get_pos()/1000
        time = float(playing_time+fast_forward_time)

        # pygame.mixer.music.rewind()

        # pygame.mixer.music.set_pos(float(playing_time+fast_forward_time))
        pygame.mixer.music.play(0, current_time+time)
        current_time += time

        print(playing_time)
        print(fast_forward_time)
        print(time)
        print(current_time)
        
    #     print(paused)
    #  ---------------------------------------------------------------------------------------------------------------------



    # Functions for Music Menu
    # ---------------------------------------------------------------------------------------------------------------------

    def add_music():
        
        global current_song

        new_window.directory = filedialog.askdirectory()

        for song in os.listdir(new_window.directory):
            name, ext = os.path.splitext(song)

            if ext == '.mp3':
                songs.append(song)


        for song in songs:
            songlist.insert("end",song)

        songlist.config(height=songlist.size())
        

        songlist.selection_set(0)
        current_song = songs[songlist.curselection()[0]]

    def delete_music():

        global current_song, paused, current_time
        index = songs.index(current_song)

        try: 
            
            if index < len(songs) - 1:
                # Update the current_song because about to get deleted
                current_song = songs[songlist.curselection()[0]+1] # current_song = songs[songlist.curselection()[0]], current_song = songs[songs.index(current_song)+1]
                
                # Deleting data for the old song
                songs.pop(songlist.curselection()[0]) #del
                songlist.delete(songlist.curselection()[0]) #del

                # Setting the new selection
                songlist.selection_clear(0, END)
                songlist.selection_set(songs.index(current_song))

                songlist.config(height=songlist.size())
                current_time = 0.0
                # new_window.update()
                play_music_special()
                
            elif index == len(songs) - 1:
                # Update the current_song because about to get deleted
                current_song = songs[0] 
                
                # Deleting data for the old song
                songs.pop(songlist.curselection()[0]) #del
                songlist.delete(songlist.curselection()[0]) #del

                # Setting the new selection
                songlist.selection_clear(0, END)
                songlist.selection_set(songs.index(current_song))

                songlist.config(height=songlist.size())
                current_time = 0.0
                # new_window.update()
                play_music_special()

            
        # except Exception:
        #     print('You have selected nothing to delete')

        finally:
            print(f'Song Index(Songs): {songs.index(current_song)}')
            print(f'Current Song: {current_song}')
            print(f'List of Songs: {songs}')

    # Functions for Edit Menu
        


    def change_font_colour():
        font_colour = colorchooser.askcolor()
        font_colour = font_colour[1]
        songlist.config(fg=font_colour)

    def change_playlist_colour():
        playlist_colour = colorchooser.askcolor()
        playlist_colour = playlist_colour[1]
        songlist.config(bg=playlist_colour)

    def change_background_colour():
        background_colour = colorchooser.askcolor()
        background_colour = background_colour[1]
        new_window.config(bg=background_colour)

    def reset_colours():
        songlist.config(fg='black')
        songlist.config(bg='#f7ffde')
        new_window.config(bg='#f0f0f0')

    # Functions for Help Menu

    def about():
        messagebox.showinfo(title='About',message='Just do it')

    def how_to_use():
        messagebox.showinfo(title='How to use',message='spacebar and k to play and pause respectively')
    # ---------------------------------------------------------------------------------------------------------------------




    # Other functions
    def adjust_volume(value):
        pygame.mixer.music.set_volume(int(value)/100)
        print(f'Volume: {int(value)/100}')
        print(f'Volume: {value}')

    def queue_music():

        global current_song, songs, MUSIC_END
        
        print('Running')
        # tk.Tk.update_idletasks(new_window)
        # tk.Tk.update(new_window)

        for event in pygame.event.get():

            if event.type == MUSIC_END:
                print('Song ended') # Check to see that it runs this if statement
                
                if current_song in songs:
                    
                    index = songs.index(current_song)
                    
                    if index < len(songs) - 1:
                        
                        song = songs[index + 1]
                        print(f'Current Song: {song}')

                        pygame.mixer.music.load(os.path.join(new_window.directory, song))
                        pygame.mixer.music.play()
                        
                        songlist.select_clear(0,END)
                        songlist.selection_set(songs.index(song))

                        current_song = song
                        current_time = 0.0
                    elif index == len(songs) - 1:

                        song = songs[0]
                        print(f'Current Song: {song}')

                        pygame.mixer.music.load(os.path.join(new_window.directory, song))
                        pygame.mixer.music.play()
                        
                        songlist.select_clear(0,END)
                        songlist.selection_set(songs.index(song))

                        current_song = song
                        current_time = 0.0

                    else:
                        print("No next song. End of the list.")
                        
                else:
                    print("Current song not found in the list.")

            else:
                print('Bruh')

        new_window.after(1000, queue_music)


    # def current_time():
    #     first_song = current_song

    #     if first_song == current_song

    new_window = tk.Tk()
    new_window.title("🎵 Music Player 🎵")
    new_window.geometry("500x300")

    pygame.init()
    pygame.mixer.init()
    MUSIC_END  = pygame.USEREVENT
    pygame.mixer.music.set_endevent(MUSIC_END)

    # Making the menus and some random code inbetween
    # ---------------------------------------------------------------------------------------------------------------------

    menubar = tk.Menu(new_window)
    new_window.config(menu=menubar)
    # new_window.resizable(False,False)

    songs = []
    current_song = ''
    paused = False
    current_time = 0.0

    music_menu = tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label='Music',menu=music_menu)
    music_menu.add_command(label='Add Music',command=add_music)
    music_menu.add_command(label='Delete',command=delete_music)

    edit_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Edit',menu=edit_menu)
    edit_menu.add_command(label='New',command=second)
    edit_menu.add_command(label='Font Colour',command=change_font_colour)
    edit_menu.add_command(label='Playlist Colour',command=change_playlist_colour)
    edit_menu.add_command(label='Background Colour',command=change_background_colour)
    edit_menu.add_command(label='Reset Colours',command=reset_colours)

    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Help',menu=help_menu)
    help_menu.add_command(label='About',command=about)
    help_menu.add_command(label='How to use',command=how_to_use)

    # ---------------------------------------------------------------------------------------------------------------------


    songlist = tk.Listbox(new_window,
                        bg='#f7ffde',
                        fg='black',
                        font=('Constantia',12),
                        width=60)
    songlist.pack()


    # Making and putting the buttons
    # ---------------------------------------------------------------------------------------------------------------------

    volume_scale = tk.Scale(new_window, from_=100, to=0, tickinterval=10, length=200, orient='horizontal', command=adjust_volume)
    volume_scale.pack()
    volume_scale.set(volume_scale['from']/2)

    button_frame = tk.Frame(new_window)
    button_frame.pack()

    back_button = tk.Button(button_frame, text='⏪', font=('Arial',20), borderwidth=0, command=fast_reverse) # <|<| ⏪
    left_button = tk.Button(button_frame, text='⬅️', font=('Arial',20), borderwidth=0, command=previous_music) # <-- ⬅️
    pause_button = tk.Button(button_frame, text='⏸️', font=('Arial',20), borderwidth=0, command=pause_music) # || ⏸️
    play_button = tk.Button(button_frame, text='▶️', font=('Arial',20), borderwidth=0, command=play_music) # |> ▶️
    right_button = tk.Button(button_frame, text='➡️', font=('Arial',20), borderwidth=0, command=next_music) # --> ➡️
    forward_button = tk.Button(button_frame, text='⏩', font=('Arial',20), borderwidth=0, command=fast_forward) # |>|> ⏩

    back_button.grid(row=0, column=0)
    left_button.grid(row=0, column=1)
    pause_button.grid(row=0, column=2)
    play_button.grid(row=0, column=3)
    right_button.grid(row=0, column=4)
    forward_button.grid(row=0, column=5)

    # --------------------------------------------------------------------------------------------------------------------


    # Keyboard bindings
    # --------------------------------------------------------------------------------------------------------------------

    def pause_music_shortcut(event):
        
        global current_song, paused

        if not paused:
            pygame.mixer.music.pause()
            paused = True

        else:
            pygame.mixer.music.unpause()
            paused = False

    def play_music_shortcut(event):
        
        global current_song, paused
        current_song = songs[songlist.curselection()[0]]


        if not paused: # If not paused(false) == True, it will run
            pygame.mixer.music.load(os.path.join(new_window.directory, current_song))
            pygame.mixer.music.play()

            # Testing code
            queue_music()
            # Testing code

        else:
            # pygame.mixer.music.load(os.path.join(new_window.directory, current_song))
            # pygame.mixer.music.play(-1)
            pygame.mixer.music.unpause()
            paused = False
            queue_music()


    # new_window.bind('<Left>',previous_music)
    # new_window.bind('<Right>',next_music)
    new_window.bind('<space>',play_music_shortcut)
    new_window.bind('<k>',pause_music_shortcut)
