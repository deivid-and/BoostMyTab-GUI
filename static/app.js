document.addEventListener("DOMContentLoaded", function () {
    const socket = io();
  
    socket.on("connect", () => console.log("Connected to server"));
    socket.on("disconnect", () => console.log("Disconnected from server"));
  
    socket.on("device_list", (data) => {
      const connectedDevicesDiv = document.getElementById("connectedDevices");
      connectedDevicesDiv.innerHTML = "";
      const message = document.createElement("p");
      message.textContent = data.output;
      connectedDevicesDiv.appendChild(message);
    });
  
    function postAction(url) {
      showLoader(true);
      console.log(`Sending POST request to: ${url}`);
      fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Cache-Control": "no-cache, no-store, must-revalidate",
          Pragma: "no-cache",
          Expires: "0",
        },
      })
        .then((response) => response.json())
        .then((data) => {
          showLoader(false);
          console.log("Response received:", data);
          displayOutput(data);
        })
        .catch((error) => {
          showLoader(false);
          console.error("Error:", error);
          displayError("An error occurred while executing the script.");
        });
    }
  
    function displayOutput(data) {
      const outputDiv = document.getElementById("output");
      const message = document.createElement("pre");
      message.className = data.status === "success" ? "success" : "error";
      message.textContent = data.output;
      outputDiv.appendChild(message);
    }
  
    function displayError(messageText) {
      const outputDiv = document.getElementById("output");
      const message = document.createElement("p");
      message.className = "error";
      message.textContent = messageText;
      outputDiv.appendChild(message);
    }
  
    function showLoader(show) {
      const loader = document.getElementById("loader");
      loader.style.display = show ? "block" : "none";
    }
  
    document.querySelectorAll("button[data-action]").forEach((button) => {
      button.addEventListener("click", () => postAction(button.getAttribute("data-action")));
    });
  
    document.getElementById("clearMessages").addEventListener("click", () => {
      document.getElementById("output").innerHTML = "";
    });
  
    function fetchConnectedDevices() {
      fetch("/list_devices", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => response.json())
        .then((data) => updateDeviceStatus(data))
        .catch((error) => console.error("Error fetching connected devices:", error));
    }
  
    function updateDeviceStatus(data) {
      const deviceStatusDiv = document.getElementById("device-status");
      const statusIcon = deviceStatusDiv.querySelector(".status-icon");
      const statusText = deviceStatusDiv.querySelector(".status-text");
  
      if (data.output.includes("device") && data.output.trim().split("\n").length > 1) {
        deviceStatusDiv.classList.add("connected");
        statusIcon.textContent = "✅";
        statusText.textContent = `Device Connected: ${data.output.split("\n")[1].trim()}`;
      } else {
        deviceStatusDiv.classList.remove("connected");
        statusIcon.textContent = "❌";
        statusText.textContent = "No Device Connected";
      }
    }
  
    setInterval(fetchConnectedDevices, 2000);
    fetchConnectedDevices();
  
    const modal = document.getElementById("helpModal");
    const helpButton = document.getElementById("helpButton");
    const closeModal = document.getElementsByClassName("close")[0];
  
    helpButton.onclick = () => modal.style.display = "block";
    closeModal.onclick = () => modal.style.display = "none";
  
    window.onclick = (event) => {
      if (event.target === modal) {
        modal.style.display = "none";
      }
    };
  });
  