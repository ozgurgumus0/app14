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
    var audio = document.getElementById("success-audio");
    audio.play();
}

function moveButton() {
    // Optional: Move button around if desired, but user asked for resizing primarily
    // For now, let's just trigger the text change and resize on interactions
    handleNoClick();
}
