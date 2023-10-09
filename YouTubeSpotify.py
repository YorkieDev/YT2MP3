#Importing various libraries and pre-reqs
from tkinter import * 
from tkinter import ttk
from pytube import YouTube
from tkinter.messagebox import showinfo, showerror, askokcancel
import threading
import os

# the function for closing the application
def close_window():
    #if askokcancel is true, close the window.
    if askokcancel(title='Close', message='Do You Want To Close The MP3 Downloader?'):
        #This destroys the window
        window.destroy()


# the function to download the mp3 audio
def download_audio():
    # the try statement to excute the download the video code
    # getting video url from entry
    mp3_link = url_entry.get()
    # checking if the entry and combobox is empty
    if mp3_link == '':
        # display error message when url entry is empty
        showerror(title='Error', message='Please enter the YouTube URL')
    # else let's download the audio file  
    else:
        # this try statement will run if the mp3 url is filled
        try:
            # this function will track the audio file download progress
            def on_progress(stream, chunk, bytes_remaining):
                # the total size of the audio
                total_size = stream.filesize
                # this function will get the size of the audio file
                def get_formatted_size(total_size, factor=1024, suffix='B'):
                    # looping through the units
                    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
                        if total_size < factor:
                            return f"{total_size:.2f}{unit}{suffix}"
                        total_size /= factor
                    # returning the formatted audio file size
                    return f"{total_size:.2f}Y{suffix}"
                    
                # getting the formatted audio file size calling the function
                formatted_size = get_formatted_size(total_size)
                # the size downloaded after the start
                bytes_downloaded = total_size - bytes_remaining
                # the percentage downloaded after the start
                percentage_completed = round(bytes_downloaded / total_size * 100)
                # updating the progress bar value
                progress_bar['value'] = percentage_completed
                # updating the empty label with the percentage value
                progress_label.config(text=str(percentage_completed) + '%, File size:' + formatted_size)
                # updating the main window of the app
                window.update()
                
            # creating the YouTube object and passing the the on_progress function
            audio = YouTube(mp3_link, on_progress_callback=on_progress)     
            # extracting and downloading the audio file 
            output = audio.streams.get_audio_only().download()
            # this splits the audio file, the base and the extension
            base, ext = os.path.splitext(output)
		    # this converts the audio file to mp3 file
            new_file = base + '.mp3'
		    # this renames the mp3 file
            os.rename(output, new_file)
            # popup for dispalying the mp3 downlaoded success message
            showinfo(title='Download Complete', message='Your MP3 has been downloaded, enjoy!!!')
            # ressetting the progress bar and the progress label
            progress_label.config(text='')
            progress_bar['value'] = 0           
        # the except will run when an expected error occurs during downloading
        except:
            showerror(title='Download Error', message='An error occurred while trying to ' \
                    'download the MP3\nThe following could ' \
                    'be the causes:\n->Invalid link\n->No internet connection\n'\
                     'Make sure you have stable internet connection and the MP3 link is valid')
                # ressetting the progress bar and the progress label
            progress_label.config(text='')
            progress_bar['value'] = 0

def downloadThread():
    t1 = threading.Thread(target=download_audio)
    t1.start() 

#Creates the window using the Tk() Function
window = Tk()

# Bind close_window function to window close event
window.protocol('WM_DELETE_WINDOW', close_window)

#Creates the title for the app
window.title('YouTube to MP3 Downloader')

#The Icon for the app, this replaces the default tkinter icon
window.iconbitmap(r'C:\Users\IainY\Documents\Python Scripts\ico.ico')

#dimensions and position of the window
window.geometry('500x400+430+180')

#makes the window non-resizable
window.resizable(height=FALSE, width=FALSE)

#creates the canvas for holding all the widgets
canvas = Canvas(window, width=500, height=400)
canvas.pack()


# style for the label 
label_style = ttk.Style()
label_style.configure('TLabel', foreground='#000000', font=('OCR A Extended', 15))
# style for the entry
entry_style = ttk.Style()
entry_style.configure('TEntry', font=('Dotum', 15))
# style for the button
button_style = ttk.Style()
button_style.configure('TButton', foreground='#000000', font='DotumChe')


#Loading the mp3 loader
logo = PhotoImage(file=r'C:\Users\IainY\Documents\Python Scripts\mp3logo.png')

#Creates the dimensions for the logo
logo = logo.subsample(2,2)

#Adding the logo to the canvas
canvas.create_image(180, 80, image=logo)

#Adding the downloader label next to the image
mp3_label = ttk.Label(window, text='Downloader', style='TLabel')
canvas.create_window(360,160, window=mp3_label)

#Creating a TTK Label
url_label = ttk.Label(window, text='Enter YouTube Link:', style='TLabel')

#Creating a TTK entry
url_entry = ttk.Entry(window, width=72, style='TEntry')

#adding the label to the canvas
canvas.create_window(115, 200,window=url_label)

#adding the entry to the canvas
canvas.create_window(250, 230, window=url_entry)

#creating the empty label for the progress bar
progress_label = Label(window, text='')

#adding the label to the canvas
canvas.create_window(240,280, window=progress_label)

#creating a progress bar to measure progress
progress_bar = ttk.Progressbar(window, orient=HORIZONTAL, length=450, mode='determinate')

#adding the progress bar to the canvas
canvas.create_window(250, 300, window=progress_bar)

#Creating the download button
download_button = ttk.Button(window, text='Start Download', style='TButton', command=downloadThread)

#adding the button to the canvas
canvas.create_window(240, 330, window=download_button)

#This runs the app
window.mainloop()