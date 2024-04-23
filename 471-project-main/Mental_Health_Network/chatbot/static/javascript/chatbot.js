function sendMessage() {
    let userInput = document.getElementById("user-input");
    let chatBox = document.getElementById("chat-box");
    
    // Display user message
    let userDiv = document.createElement("div");
    userDiv.textContent = "You: " + userInput.value;
    chatBox.appendChild(userDiv);

    // Send message to Django view
    fetch(`/chatbot/chat/?message=${userInput.value}`)
        .then(response => response.json())
        .then(data => {
            let botDiv = document.createElement("div");
            botDiv.textContent = "Mini: " + data.response;
            chatBox.appendChild(botDiv);
        })
        .catch(error => console.error('Error:', error));

    // Clear input field
    userInput.value = "";
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to bottom
}
