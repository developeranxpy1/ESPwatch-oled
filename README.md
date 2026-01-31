<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>ESPwatch – ESP32 Multipurpose Watch</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <style>
    :root {
      --bg: #0e0e11;
      --card: #16161c;
      --fg: #eaeaf0;
      --muted: #9aa0b5;
      --accent: #5eead4;
      --border: #26262e;
    }

    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
      background: radial-gradient(1200px 600px at top, #15151c, var(--bg));
      color: var(--fg);
      line-height: 1.6;
    }

    header {
      padding: 5rem 1rem 3rem;
      text-align: center;
    }

    header h1 {
      font-size: clamp(2.5rem, 5vw, 3.5rem);
      margin-bottom: 0.75rem;
      letter-spacing: -0.02em;
    }

    header p {
      max-width: 720px;
      margin: auto;
      color: var(--muted);
      font-size: 1.05rem;
    }

    section {
      max-width: 1100px;
      margin: 3rem auto;
      padding: 0 1rem;
    }

    h2 {
      font-size: 1.6rem;
      margin-bottom: 1.25rem;
      border-left: 4px solid var(--accent);
      padding-left: 0.75rem;
    }

    .card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 1.25rem;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1.25rem;
    }

    .img-frame {
      background: #0b0b0f;
      border-radius: 14px;
      overflow: hidden;
      aspect-ratio: 4 / 3;
      border: 1px solid var(--border);
    }

    .img-frame img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    ul {
      padding-left: 1.2rem;
      margin: 0;
    }

    li {
      margin-bottom: 0.4rem;
    }

    a {
      color: var(--accent);
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }

    code {
      background: #0b0b0f;
      padding: 0.25rem 0.45rem;
      border-radius: 6px;
      font-size: 0.9rem;
      border: 1px solid var(--border);
    }

    .center {
      text-align: center;
    }

    footer {
      padding: 2.5rem 1rem;
      text-align: center;
      color: var(--muted);
      font-size: 0.9rem;
      border-top: 1px solid var(--border);
      margin-top: 4rem;
    }

    .button {
      display: inline-block;
      margin-top: 0.75rem;
      padding: 0.55rem 1.1rem;
      border-radius: 999px;
      background: var(--accent);
      color: #000;
      font-weight: 600;
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
    <div class="img-frame">
      <img src="https://github.com/USER-RGB-PIXEL/ESPwatch/assets/86851518/71ef2801-0e9e-4aeb-8b74-5bc94339871b">
    </div>
    <div class="img-frame">
      <img src="https://github.com/USER-RGB-PIXEL/ESPwatch/assets/86851518/8525a8b6-e796-4c18-84c9-0ba624c28dfe">
    </div>
    <div class="img-frame">
      <img src="https://github.com/USER-RGB-PIXEL/ESPwatch/assets/86851518/42b7b930-0d1d-4ac1-b4ad-8b39d1930629">
    </div>
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
  <div class="img-frame">
    <img src="https://github.com/USER-RGB-PIXEL/ESPwatch/assets/86851518/e79bfaf6-6c7b-4d2c-9c13-f40e807ebcbe">
  </div>
  <div class="center">
    <a class="button" href="https://wokwi.com/projects/384799949503869953" target="_blank">
      View Wokwi Simulation
    </a>
  </div>
</section>

<section>
  <h2>🚀 Installation (MicroPython)</h2>
  <div class="card">
    <ol>
      <li>Flash MicroPython firmware to the ESP32</li>
      <li>Upload project files using Thonny</li>
      <li>Edit GPIO pins and WiFi credentials in <code>main.py</code></li>
    </ol>
    <p>
      Default OTA AP credentials:<br>
      <code>SSID: webrepl</code><br>
      <code>Password: 731235</code>
    </p>
  </div>
</section>

<section>
  <h2>🔄 Arduino Version</h2>
  <div class="card">
    <p>
      An Arduino (C++) implementation is not yet available.
      Contributions or ports are welcome.
    </p>
  </div>
</section>

<section class="center">
  <h2>🔗 Contact</h2>
  <a href="https://www.reddit.com/user/Anxpy1" target="_blank">
    <img src="https://www.pngitem.com/pimgs/m/121-1217716_reddit-logo-png-transparent-png.png"
         style="width:180px">
  </a>
</section>

<footer>
  ESPwatch · Built for experimentation · Hardware first, vibes later
</footer>

</body>
</html>
