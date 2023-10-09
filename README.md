# YouTube to MP3 Downloader

## Overview

This project is a YouTube to MP3 downloader built with Python and Tkinter. It allows users to download the audio content of a YouTube video in MP3 format directly to their machine.


## Features

- Download MP3 audio from a YouTube URL.
- Provides a graphical user interface via Tkinter.
- Real-time progress tracking during download.
- Checks for valid YouTube URL input.
- Multithreading support for responsive UI during download.
  
## Requirements

- Python 3.x
- Tkinter
- pytube
- threading
- os

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/youtube-to-mp3-downloader.git
    ```

2. Navigate to the project directory and install the required Python packages:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:

    ```
    python main.py
    ```

2. Enter a valid YouTube URL in the provided field.

3. Click the 'Start Download' button to begin the download.

## Troubleshooting

In case of an invalid URL or network issues, an error dialog will appear with information about the potential causes of the problem.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
