<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>ESPwatch – ESP32 Multipurpose Watch</title>

  <style>
    :root {
      --bg: #0e0e11;
      --fg: #eaeaf0;
      --muted: #a0a0b5;
      --accent: #5eead4;
      --card: #16161c;
    }

    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--bg);
      color: var(--fg);
      line-height: 1.6;
    }

    header {
      padding: 4rem 1rem;
      text-align: center;
    }

    header h1 {
      font-size: 3rem;
      margin-bottom: 0.5rem;
    }

    header p {
      color: var(--muted);
      max-width: 700px;
      margin: auto;
    }

    section {
      max-width: 1100px;
      margin: 3rem auto;
      padding: 0 1rem;
    }

    h2 {
      border-left: 4px solid var(--accent);
      padding-left: 0.75rem;
      margin-bottom: 1rem;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1.5rem;
    }

    .card {
      background: var(--card);
      padding: 1rem;
      border-radius: 12px;
    }

    img {
      width: 100%;
      border-radius: 12px;
    }

    ul {
      padding-left: 1.2rem;
    }

    a {
      color: var(--accent);
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }

    .center {
      text-align: center;
    }

    footer {
      text-align: center;
      padding: 2rem;
      color: var(--muted);
      font-size: 0.9rem;
    }

    code {
      background: #111;
      padding: 0.2rem 0.4rem;
      border-radius: 6px;
      font-size: 0.9rem;
    }
  </style>
</head>

<body>

<header>
  <h1>⌚ ESPwatch</h1>
  <p>
    ESP32-based multipurpose smartwatch built using MicroPython and Arduino.
    Designed for hackers, tinkerers, and people who enjoy wearing their bugs.
  </p>
</header>

<section>
  <h2>📸 Project Gallery</h2>
  <div class="grid">
    <img src="https://github.com/USER-RGB-PIXEL/ESPwatch/assets/86851518/71ef2801-0e9e-4aeb-8b74-5bc94339871b" alt="ESPwatch Front">
    <img src="https://github.com/USER-RGB-PIXEL/ESPwatch/assets/86851518/8525a8b6-e796-4c18-84c9-0ba624c28dfe" alt="LED Test">
    <img src="https://github.com/USER-RGB-PIXEL/ESPwatch/assets/86851518/42b7b930-0d1d-4ac1-b4ad-8b39d1930629" alt="ESPwatch Video Frame">
  </div>
</section>

<section>
  <h2>✨ Features</h2>
  <div class="card">
    <ul>
      <li>ESP32-based wearable platform</li>
      <li>MicroPython & Arduino compatible</li>
      <li>OLED display (I2C)</li>
      <li>Speaker output</li>
      <li>Vibration motor support</li>
      <li>Flash LED (white)</li>
      <li>Internal status LED (blue)</li>
      <li>Two-button input</li>
      <li>OTA updates via WebREPL</li>
    </ul>
  </div>
</section>

<section>
  <h2>🧰 Hardware Requirements</h2>
  <div class="card">
    <ul>
      <li>ESP32 board</li>
      <li>OLED display (I2C)</li>
      <li>Speaker</li>
      <li>Vibration motor or red LED</li>
      <li>White LED (flash)</li>
      <li>Blue LED (status)</li>
      <li>2 × push buttons</li>
    </ul>
  </div>
</section>

<section>
  <h2>🔌 Wiring</h2>
  <img src="https://github.com/USER-RGB-PIXEL/ESPwatch/assets/86851518/e79bfaf6-6c7b-4d2c-9c13-f40e807ebcbe" alt="Wiring Diagram">
  <p class="center">
    <a href="https://wokwi.com/projects/384799949503869953" target="_blank">
      View Wokwi Simulation
    </a>
  </p>
</section>

<section>
  <h2>🚀 Installation (MicroPython)</h2>
  <div class="card">
    <ol>
      <li>Flash MicroPython firmware to the ESP32</li>
      <li>Copy all project files to the device using Thonny</li>
      <li>Edit GPIO pins and WiFi credentials in <code>main.py</code></li>
    </ol>
    <p>
      Default OTA AP credentials:<br/>
      <code>SSID: webrepl</code><br/>
      <code>Password: 731235</code>
    </p>
  </div>
</section>

<section>
  <h2>🔄 Arduino Version</h2>
  <div class="card">
    <p>
      An Arduino (C++) port is not currently available.
      If you are interested in contributing or porting this project,
      feel free to reach out.
    </p>
  </div>
</section>

<section class="center">
  <h2>🔗 Contact</h2>
  <a href="https://www.reddit.com/user/Anxpy1" target="_blank">
    <img src="https://www.pngitem.com/pimgs/m/121-1217716_reddit-logo-png-transparent-png.png"
         alt="Reddit"
         style="width:180px;">
  </a>
</section>

<footer>
  ESPwatch · Built for experimentation · No smart ecosystems were harmed
</footer>

</body>
</html>
