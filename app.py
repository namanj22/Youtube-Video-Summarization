import validators
import requests
from bs4 import BeautifulSoup
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain.schema import Document
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound

## Streamlit APP
st.set_page_config(
    page_title="LangChain: Summarize Text From YT or Website", page_icon="🦜"
)
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader("Summarize URL")

## Get the Groq API Key and URL (YouTube or website) to be summarized
with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value="", type="password")

generic_url = st.text_input("URL", label_visibility="collapsed")

## Groq Model
llm = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=groq_api_key)

prompt_template = """
Provide a summary of the following content in 300 words.
Do not repeat the content and ensure the summary does not exceed 600 words.
Use points and arguments, and when summarizing website content, include examples where applicable.
Content:{text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

# Function to fetch website content
def fetch_website_content(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        # Extract text content from common HTML tags
        text = " ".join([p.get_text() for p in soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6"])])
        return text.strip()
    except Exception as e:
        st.error(f"Error fetching website content: {e}")
        return None

if st.button("Summarize the Content from YT or Website"):
    ## Validate inputs
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL. It can be a YouTube video URL or website URL")
    else:
        try:
            with st.spinner("Waiting..."):
                # Load data from YouTube or Website
                if "youtube.com" in generic_url or "youtu.be" in generic_url:
                    try:
                        # Extract video ID from URL and attempt to fetch the transcript in multiple languages
                        video_id = generic_url.split("v=")[-1].split("&")[0]
                        transcript = None
                        # Attempt to fetch in preferred languages
                        for language_code in ['en', 'en-IN', 'hi']:
                            try:
                                transcript = YouTubeTranscriptApi.get_transcript(video_id=video_id, languages=[language_code])
                                break
                            except NoTranscriptFound:
                                continue
                        if not transcript:
                            st.error("Transcript not available in preferred languages.")
                            st.stop()
                        # Combine transcript text
                        text = " ".join([entry['text'] for entry in transcript])
                    except Exception as yt_exception:
                        st.error(f"Error fetching YouTube transcript: {yt_exception}")
                        st.stop()
                else:
                    # Fetch website content using custom fetch function
                    text = fetch_website_content(generic_url)
                    if not text:
                        st.stop()
                
                docs = [Document(page_content=text)]

                # Summarize the entire content without chunking
                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                summary = chain.run([docs[0]])

                st.success(summary.strip())
        except Exception as e:
            st.error(f"An error occurred: {e}")
