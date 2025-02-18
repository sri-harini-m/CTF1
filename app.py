from flask import Flask, request, render_template_string, send_file, redirect, url_for
import os

app = Flask(__name__)

# Folder to store flag files (this is just for storage purposes, the flags are not submitted by users)
FLAG_FOLDER = "flags"
if not os.path.exists(FLAG_FOLDER):
    os.makedirs(FLAG_FOLDER)

# Challenge Data (replace these methods with actual challenges)
challenges = {
    1: {"title": "Nmap Scan", "description": "Scan the server for open ports using Nmap. The flag is hidden in a server port.", "flag_file": "flag_1.txt"},
    2: {"title": "SYN Scan", "description": "Perform an advanced SYN scan on the target server and fingerprint its OS. The flag is hidden in an HTTP header.", "flag_file": "flag_2.txt"},
    3: {"title": "Shodan Scan", "description": "Find an IoT device using Shodan. The flag is hidden in the device's metadata.", "flag_file": "flag_3.txt"},
    4: {"title": "SQL Injection", "description": "Exploit SQL injection in a login form. The flag is stored in a database and accessible via SQL injection.", "flag_file": "flag_4.txt"},
    5: {"title": "XSS Attack", "description": "Inject a malicious JavaScript payload into a form. The flag will appear once you successfully execute XSS.", "flag_file": "flag_5.txt"},
    6: {"title": "Local File Inclusion", "description": "Exploit LFI to access the `/etc/passwd` file. The flag is hidden in the file.", "flag_file": "flag_6.txt"}
}

# Home page
@app.route('/')
def home():
    return render_template_string('''
    <h1>CTF Game</h1>
    <p>Welcome to the Capture The Flag (CTF) game!</p>
    <p>Select a challenge:</p>
    <ul>
        {% for challenge_id, challenge in challenges.items() %}
            <li><a href="{{ url_for('challenge', challenge_id=challenge_id) }}">{{ challenge['title'] }}</a></li>
        {% endfor %}
    </ul>
    ''', challenges=challenges)

# Challenge page
@app.route('/challenge/<int:challenge_id>', methods=['GET'])
def challenge(challenge_id):
    challenge = challenges.get(challenge_id)
    if not challenge:
        return redirect(url_for('home'))

    # Serve the flag as a downloadable file when the user finds it through the challenge method
    flag_file = os.path.join(FLAG_FOLDER, challenge['flag_file'])
    
    # Render the correct page based on the challenge type
    if challenge_id == 1:  # Nmap Scan: Hidden in a server port (simulated with a file)
        return render_template_string('''
        <h1>{{ challenge['title'] }}</h1>
        <p>{{ challenge['description'] }}</p>
        <p>Try scanning open ports to discover hidden flags.</p>
        <a href="{{ url_for('download_flag', challenge_id=challenge_id) }}">Download the flag</a>
        ''', challenge=challenge, challenge_id=challenge_id)

    elif challenge_id == 2:  # SYN Scan: Hidden in HTTP header (simulated with a file)
        return render_template_string('''
        <h1>{{ challenge['title'] }}</h1>
        <p>{{ challenge['description'] }}</p>
        <p>Perform a SYN scan and inspect HTTP headers to find hidden flags.</p>
        <a href="{{ url_for('download_flag', challenge_id=challenge_id) }}">Download the flag</a>
        ''', challenge=challenge, challenge_id=challenge_id)

    elif challenge_id == 3:  # Shodan Scan: Hidden in IoT device metadata
        return render_template_string('''
        <h1>{{ challenge['title'] }}</h1>
        <p>{{ challenge['description'] }}</p>
        <p>Use Shodan to scan for IoT devices and find metadata that contains the flag.</p>
        <a href="{{ url_for('download_flag', challenge_id=challenge_id) }}">Download the flag</a>
        ''', challenge=challenge, challenge_id=challenge_id)

    elif challenge_id == 4:  # SQL Injection: Flag in database
        return render_template_string('''
        <h1>{{ challenge['title'] }}</h1>
        <p>{{ challenge['description'] }}</p>
        <p>Try performing SQL injection on the login form to extract a flag from the database.</p>
        <a href="{{ url_for('download_flag', challenge_id=challenge_id) }}">Download the flag</a>
        ''', challenge=challenge, challenge_id=challenge_id)

    elif challenge_id == 5:  # XSS Attack: Flag shows up after successful XSS
        return render_template_string('''
        <h1>{{ challenge['title'] }}</h1>
        <p>{{ challenge['description'] }}</p>
        <p>Inject a malicious script that reveals the hidden flag.</p>
        <a href="{{ url_for('download_flag', challenge_id=challenge_id) }}">Download the flag</a>
        ''', challenge=challenge, challenge_id=challenge_id)

    elif challenge_id == 6:  # LFI: Flag hidden in /etc/passwd file
        return render_template_string('''
        <h1>{{ challenge['title'] }}</h1>
        <p>{{ challenge['description'] }}</p>
        <p>Perform a Local File Inclusion (LFI) attack to access the flag hidden in system files.</p>
        <a href="{{ url_for('download_flag', challenge_id=challenge_id) }}">Download the flag</a>
        ''', challenge=challenge, challenge_id=challenge_id)

# Route to download the flag file
@app.route('/download_flag/<int:challenge_id>')
def download_flag(challenge_id):
    challenge = challenges.get(challenge_id)
    if not challenge:
        return redirect(url_for('home'))

    # Serve the flag file corresponding to the challenge
    flag_file = os.path.join(FLAG_FOLDER, challenge['flag_file'])
    if os.path.exists(flag_file):
        return send_file(flag_file, as_attachment=True, download_name="flag.txt")
    else:
        return "Flag file not found. Challenge might not be completed yet."

if __name__ == '__main__':
    app.run(debug=True)
