async function sendMessage() {
  const input = document.getElementById("userInput");
  const chatbox = document.getElementById("chatbox");

  if (!input.value.trim()) return;

  let userMsg = document.createElement("div");
  userMsg.className = "message user";
  userMsg.innerText = input.value;
  chatbox.appendChild(userMsg);

  let response = await fetch("/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question: input.value })
  });

  let data = await response.json();

  let botMsg = document.createElement("div");
  botMsg.className = "message bot";
  botMsg.innerText = data.answer;
  chatbox.appendChild(botMsg);

  chatbox.scrollTop = chatbox.scrollHeight;
  input.value = "";
}

// Welcome message
window.onload = () => {
  const chatbox = document.getElementById("chatbox");
  let welcomeMsg = document.createElement("div");
  welcomeMsg.className = "message bot";
  welcomeMsg.innerText =
    "👋 Welcome beautiful! I’m your Makeup Assistant. Ask me about foundations, lipsticks, skincare routines, or beauty tips!";
  chatbox.appendChild(welcomeMsg);
};

// Rotating placeholder examples
const examples = [
  "Best foundation for oily skin?",
  "Top 3 nude lipsticks?",
  "What SPF sunscreen should I use?",
  "Best budget-friendly mascara?"
];

let idx = 0;
setInterval(() => {
  document.getElementById("userInput").placeholder = "Ask me: " + examples[idx];
  idx = (idx + 1) % examples.length;
}, 3000);
