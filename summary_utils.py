import torch
import torch
torch.classes.__path__ = []
import os
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"
os.environ["PYTORCH_FORCE_DISABLE_MPS"] = "1"
from transformers import pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def generate_summary(text):
    if not text or len(text.split()) < 20:
        return "Oops! This book doesn't have enough description to generate a summary."
    if len(text) > 700:
        text = text[:700]
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']

