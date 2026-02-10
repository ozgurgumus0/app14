
import streamlit as st
import base64
import os

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def get_img_with_href(local_img_path, context_type="image/jpeg"):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    return f'data:image/{img_format};base64,{bin_str}'

st.set_page_config(layout="wide", page_title="Be My Valentine?")

# Load assets
css_content = """
body {
    background-color: #fce4ec;
    font-family: 'Indie Flower', cursive;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    margin: 0;
    overflow-x: hidden;
    flex-direction: column;
}

.container {
    text-align: center;
    width: 90%;
    max-width: 800px;
    padding: 20px;
}

.header_text {
    color: #e91e63;
    font-size: 2.5rem;
    margin: 20px 0;
}

.gallery {
    display: flex;
    justify-content: center;
    gap: 15px;
    margin-bottom: 20px;
    flex-wrap: wrap;
}

.gallery img {
    width: 120px;
    height: 120px;
    object-fit: cover;
    border-radius: 10px;
    border: 4px solid white;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s;
}

.gallery img:nth-child(odd) {
    transform: rotate(3deg);
}

.gallery img:nth-child(even) {
    transform: rotate(-3deg);
}

.gallery img:hover {
    transform: scale(1.1) rotate(0deg);
    z-index: 10;
}

.gif_container img {
    max-width: 300px;
    width: 100%;
    height: auto;
    border-radius: 15px;
    margin-bottom: 30px;
}

.buttons {
    display: flex;
    justify-content: center;
    gap: 20px;
    flex-wrap: wrap;
    align-items: center;
}

.btn {
    background-color: #ff4081;
    color: white;
    border: none;
    padding: 15px 30px;
    font-size: 1.5rem;
    border-radius: 50px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-family: 'Indie Flower', cursive;
    white-space: nowrap;
}

.btn:hover {
    background-color: #f50057;
    transform: scale(1.05);
}

#noButton {
    background-color: #b0bec5;
    position: relative;
    transition: 0.2s;
}

#noButton:hover {
    background-color: #90a4ae;
}

@media (max-width: 600px) {
    .header_text {
        font-size: 1.8rem;
    }

    .gallery img {
        width: 80px;
        height: 80px;
    }

    .btn {
        padding: 10px 20px;
        font-size: 1.2rem;
    }
}
"""

js_content = """
const messages = [
    "Are you sure?",
    "Really sure??",
    "Are you positive?",
    "Pookie please...",
    "Just think about it!",
    "If you say no, I will be really sad...",
    "I will be very very very sad...",
    "Ok fine, I will stop asking...",
    "Just kidding, say yes please! ❤️"
];

let messageIndex = 0;

function handleNoClick() {
    const noBtn = document.getElementById('noButton');
    const yesBtn = document.getElementById('yesButton');
    noBtn.innerText = messages[messageIndex];
    messageIndex = (messageIndex + 1) % messages.length;
    const currentSize = parseFloat(window.getComputedStyle(yesBtn).fontSize);
    yesBtn.style.fontSize = `${currentSize * 1.5}px`;

    // Decrease No button size
    const currentNoSize = parseFloat(window.getComputedStyle(noBtn).fontSize);
    noBtn.style.fontSize = `${Math.max(currentNoSize * 0.8, 0)}px`; // Prevent negative size
}

function nextPage() {
    document.getElementById('asking-state').style.display = 'none';
    document.getElementById('success-state').style.display = 'block';
    confetti();
    setInterval(confetti, 2000); // Keep firing confetti
    
    // Play audio
    const audio = document.getElementById("success-audio");
    audio.play().catch(e => console.log("Audio play failed (user interaction needed usually): " + e));
}

function moveButton() {
    handleNoClick();
}
"""

# HTML Template with Placeholders
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Be My Valentine?</title>
    <style>
        {css_content}
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Indie+Flower&display=swap" rel="stylesheet">
</head>
<body>
    <div class="container">
        <div id="asking-state">
            <div class="gallery">
                <img src="{img1}" alt="Us 1">
                <img src="{img2}" alt="Us 2">
                <img src="{img3}" alt="Us 3">
                <img src="{img4}" alt="Us 4">
                <img src="{img5}" alt="Us 5">
            </div>
            <h1 class="header_text">Will you be my Valentine Akbota Oralkhanova aka Tatlış?</h1>
            <div class="gif_container">
                <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXNueHYzODkxcXB3cDB2OWcxZ3l0YTc5ZWYzOHlmb3B4c2tvZ3I1dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/cLS1cfxvGOPVpf9g3y/giphy.gif" alt="Cute bears">
            </div>
            <div class="buttons">
                <button class="btn" id="yesButton" onclick="nextPage()">Yes</button>
                <button class="btn" id="noButton" onmouseover="moveButton()" onclick="moveButton()">No</button>
            </div>
        </div>
        <div id="success-state" style="display: none;">
            <h1 class="header_text">Yaay! You will receive your gift in February 14</h1>
            <div class="gif_container">
                <img src="{success_gif}" alt="Dancing Rat">
            </div>
            <audio id="success-audio" src="{audio_src}"></audio>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <script>
        {js_content}
    </script>
</body>
</html>
"""

# Images
img1 = get_img_with_href("WhatsApp Image 2026-02-10 at 17.22.51.jpeg")
img2 = get_img_with_href("WhatsApp Image 2026-02-10 at 17.23.32.jpeg")
img3 = get_img_with_href("WhatsApp Image 2026-02-10 at 17.24.56.jpeg")
img4 = get_img_with_href("WhatsApp Image 2026-02-10 at 17.25.17.jpeg")
img5 = get_img_with_href("WhatsApp Image 2026-02-10 at 17.25.42.jpeg")
success_gif = get_img_with_href("dancing-rat-fixed.gif") 

# Audio
audio_str = get_base64_of_bin_file("Christmas Rat Dance.mp3")
audio_src = f"data:audio/mp3;base64,{audio_str}"

# Render
full_html = html_template.format(
    css_content=css_content,
    js_content=js_content,
    img1=img1,
    img2=img2,
    img3=img3,
    img4=img4,
    img5=img5,
    success_gif=success_gif,
    audio_src=audio_src
)

st.components.v1.html(full_html, height=1000, scrolling=True)
