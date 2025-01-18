
# RasaBot - Setup Rasa on Local Server & Run

## About This Project
This repository provides a complete guide to setting up and running Rasa on a local server. You'll learn how to:
- Set up a Python virtual environment
- Install and train Rasa
- Integrate with Laravel or other applications
- Test intents and responses
- Run your Rasa bot with Docker Compose

## Prerequisites
- Python 3.10
- Docker and Docker Compose installed
- Basic knowledge of terminal commands

---

## 🚀 Getting Started

Clone this repository to get started with the RasaBot setup:
```bash
git clone https://github.com/mejba13/RasaBot-LocalServer-Setup.git
cd RasaBot-LocalServer-Setup
```
### Create the Python Virtual Environment (Workspace)

1. **Create a new environment with the correct Python version**
   ```bash
   brew install python@3.10
   python3.10 --version
   python3.10 -m venv rasa_env
   ```

2. **Activate the environment**
   ```bash
   source rasa_env/bin/activate
   ```

3. **Install Rasa**
   ```bash
   pip install rasa
   ```

4. **Verify Rasa Installation**
   ```bash
   rasa --version
   ```

5. **Initialize a New Rasa Project**
   ```bash
   rasa init --no-prompt
   ```

6. **Train Your Rasa Model**
   ```bash
   rasa train
   ```

---

## Run Rasa Bot

### Run Rasa for Testing
```bash
rasa shell
```
## Test the intents with inputs like:
- Hi
- What is your return policy?
- How long does delivery take?
- I have an issue with payment.

### Run Rasa Actions Server
```bash
rasa run actions
```

### Test the HTTP API
Start your Rasa server with the HTTP API enabled:
```bash
rasa run --enable-api
```

Start your Rasa server with API and Cross-Origin Resource Sharing (CORS) enabled:
```bash
rasa run --enable-api --cors "*"
```

The Rasa server will be available at:
```text
http://localhost:5005
```

---

## Docker Integration

### Build and Run the Docker Containers
To run the Rasa bot and action server using Docker Compose:
```bash
docker compose up --build -d
```

---

## 🎯 Testing Intents and Stories
After running the server, you can test the chatbot by sending messages through the shell or API calls to validate responses and intents.

---

![Rasa Server Setup](https://s3.us-east-1.amazonaws.com/mejba.me/AI/only-rasa-server.png)


## 🔗 Let's Connect  

- **Instagram**: [engr_mejba_ahmed](https://www.instagram.com/engr_mejba_ahmed/)  
- **TikTok**: [engr_mejba_ahmed](https://www.tiktok.com/@engr_mejba_ahmed)  
- **YouTube**: [Engr Mejba Ahmed](https://www.youtube.com/channel/UCfLIuNxRfXT7HmvvB9Ld0SA)  
- **Twitter**: [@mejba_92](https://x.com/mejba_92)  
- **LinkedIn**: [Engr Mejba Ahmed](https://www.linkedin.com/in/engr-mejba-ahmed-795ab3165/)  
- **Facebook**: [Engr Mejba Ahmed](https://www.facebook.com/engrmejbaahmed/)  
- **Reddit**: [engrmejbaahmed](https://www.reddit.com/user/engrmejbaahmed/)  
- **Pinterest**: [engrmejbaahmed](https://www.pinterest.com/engrmejbaahmed/)  
- **GitLab**: [engr-mejba-ahmed](https://gitlab.com/engr-mejba-ahmed)  
- **LeetCode**: [engrmejbaahmed](https://leetcode.com/u/engrmejbaahmed/)  
- **HackerOne**: [Engr Mejba Ahmed](https://hackerone.com/engrmejbaahmed?type=user)  
- **HackerRank**: [Dashboard](https://www.hackerrank.com/dashboard)  
- **Bugcrowd**: [EngrMejbaAhmed](https://bugcrowd.com/EngrMejbaAhmed)  
- **Medium**: [Engr Mejba Ahmed](https://medium.com/@engr-mejba-ahmed)  
- **TryHackMe**: [EngrMejbaAhmed](https://tryhackme.com/r/p/EngrMejbaAhmed)  
- **Codewars**: [mejba13](https://www.codewars.com/users/mejba13)  
- **GitHub**: [mejba13](https://github.com/mejba13)  
- **PentesterLab**: [lucid_hacker_721](https://pentesterlab.com/profile/lucid_hacker_721)  
- **DEV.to**: [Engr Mejba Ahmed](https://dev.to/engrmejbaahmed)  
- **Quora**: [Engr Mejba Ahmed](https://www.quora.com/profile/Engr-Mejba-Ahmed)  

---

## License
This project is licensed under the MIT License.
