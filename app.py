# app.py
import time
import random
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Sample sentences for log generation
SAMPLE_SENTENCES = [
    "The quick brown foyyyyyyyyyyyyyyyyyyyyyy jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold.",
    "Actions speak louder than words.",
    "The only thing we have to fear is fear itself.",
    "Ask not what your country can do for you.",
    "I think, therefore I am.",
    "The pen is mightier than the sword.",
    "When in Rome, do as the Romans do."
] * 5  # Repeat to get 50 sentences

def generate_log_event():
    """Generate a single log event with 50 sentences"""
    timestamp = datetime.now().isoformat()
    sentences = random.choices(SAMPLE_SENTENCES, k=50)
    message = " ".join(sentences)
    return f"{timestamp} | EVENT | {message}"

def main():
    """Main function to generate logs at 10 events per second"""
    logger.info("Starting log generator...")
    while True:
        for _ in range(10):  # Generate 10 events per second
            log_message = generate_log_event()
            logger.info(log_message)
        time.sleep(1)  # Wait 1 second between batches

if __name__ == "__main__":
    main()
