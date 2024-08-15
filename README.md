# YouTube Handle Extractor

This Python script extracts YouTube handles from a list of YouTube channel URLs. It handles various URL formats such as `@handles`, `usernames`, `channel IDs`, and more. The script scrapes the page when necessary to retrieve the correct YouTube handle.

## Features

- Extracts YouTube handles from multiple URL formats.
- Automatically scrapes the YouTube page if the handle is not directly available in the URL.
- Returns a comma-separated list of YouTube handles.

## Requirements

To run this script, you'll need to install the necessary Python packages listed in the `requirements.txt` file.

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Installing Dependencies

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/youtube-handle-extractor.git
    cd youtube-handle-extractor
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Modify the URL List:**
   
   Update the `channel_urls` variable in the script with your own list of YouTube channel URLs. The URLs should be comma-separated.

      Example:
   ```python
   channel_urls = "https://www.youtube.com/@handle,https://www.youtube.com/user/username,https://www.youtube.com/c/username,https://www.youtube.com/channel/UC_CHANNEL_ID"


3. **Run the Script:**

    After setting up your URLs, run the script:

    ```bash
    python youtube_handle_extractor.py
    ```

4. **View the Results:**

    The script will output a comma-separated list of YouTube handles extracted from the provided URLs.

    Example output:
    ```
    handle1,handle2,handle3
    ```

## Logging

The script uses Python's built-in logging to provide detailed information about the process. If a handle cannot be found for a URL, a message will be printed to the console.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
