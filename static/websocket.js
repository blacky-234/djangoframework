console.log("loading js file confirmations");

let ws = new WebSocket("ws://127.0.0.1:8000/ws/echo");

ws.onopen = () => {
    console.log("WebSocket connected");
    ws.send("hello");   // send only after connection is open
};

ws.onmessage = (e) => {
    console.log("Received:", e.data);
};

ws.onerror = (e) => {
    console.error("WebSocket error:", e);
};

ws.onclose = () => {
    console.log("WebSocket closed");
};
