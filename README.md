# Youtube-Video-Website-Summarizer
LangChain: Summarize Text From YouTube or Website
Overview
This Streamlit app leverages LangChain and the ChatGroq model to provide an AI-powered summary of text content from YouTube videos and websites. You can input a URL, and the app will extract and summarize the content using a custom prompt template.

Features


Summarize YouTube Video Transcripts: Fetches the transcript of a YouTube video and provides a concise summary.

Summarize Website Content: Extracts and summarizes the main text content from a given website.

Groq API Integration: Uses the Groq API with the ChatGroq model to process and summarize content effectively.

Install dependencies: Make sure you have Python 3.8+ installed, then use the following command to install required libraries:


![WhatsApp Image 2024-11-15 at 18 00 07_afaac308](https://github.com/user-attachments/assets/1713b9c7-923d-4d60-a2fa-c81bacd81bab)




Code Explanation

Libraries Used:

Streamlit: Used for building the web interface.

Requests and BeautifulSoup: Used for web scraping to extract content from websites.

LangChain and ChatGroq: For building and running the language model to summarize the content.

YouTube Transcript API: Extracts transcripts from YouTube videos.
![WhatsApp Image 2024-11-11 at 19 21 59_8df125d3](https://github.com/user-attachments/assets/d1201aa8-8f60-457c-a5e6-6f0c3e019d32)


Key Functions

fetch_website_content(url): Fetches and extracts text from a website.

run() method of the LangChain chain: Processes the input document and returns a summary.
![WhatsApp Image 2024-11-11 at 19 19 12_97bbb626](https://github.com/user-attachments/assets/09467f59-2dc7-4da0-824e-2ee4a770ae49)


Example Workflow

Open the app in your browser.

Provide the Groq API Key and input a valid YouTube or website URL.

Click "Summarize the Content from YT or Website" to receive the summarized text.

Troubleshooting

Invalid API Key: Ensure that the Groq API Key is correct and active.

URL Issues: The app supports URLs with the youtube.com, youtu.be, and general website links.

Transcript Availability: Not all YouTube videos have transcripts, especially if they are in certain languages or have no captions enabled.


Contributing
Feel free to fork this project, make improvements, and submit pull requests. For any issues or feature requests, please open an issue on GitHub.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgements
LangChain and ChatGroq for powerful language model capabilities.
YouTube Transcript API for extracting video transcripts.
