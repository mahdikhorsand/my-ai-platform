const output = document.getElementById("output");

function register() {
    const name = document.getElementById("name").value;
    const contact = document.getElementById("contact").value;

    fetch("http://127.0.0.1:8000/auth/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, contact })
    })
    .then(res => res.json())
    .then(data => output.textContent = JSON.stringify(data, null, 2));
}

function topup() {
    const amount = parseFloat(document.getElementById("amount").value);
    const apikey = document.getElementById("apikey").value;

    fetch("http://127.0.0.1:8000/wallet/topup", {
        method: "POST",
        headers: { "Content-Type": "application/json", "x-tenant-apikey": apikey },
        body: JSON.stringify({ amount })
    })
    .then(res => res.json())
    .then(data => output.textContent = JSON.stringify(data, null, 2));
}

function ask() {
    const prompt = document.getElementById("prompt").value;
    const apikey = document.getElementById("apikey").value;

    fetch("http://127.0.0.1:8000/api/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json", "x-tenant-apikey": apikey },
        body: JSON.stringify({ user_id: "1", prompt })
    })
    .then(res => res.json())
    .then(data => output.textContent = JSON.stringify(data, null, 2));
}
