import mysql.connector
import yaml

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Default password is null
    database="rasabot"
)

cursor = db.cursor()

# Fetch intents and examples
cursor.execute("SELECT name, examples FROM intents")
intents = cursor.fetchall()

nlu_data = {"version": "2.0", "nlu": []}
for intent in intents:
    nlu_data["nlu"].append({
        "intent": intent[0],
        "examples": intent[1]
    })

with open("data/nlu.yml", "w") as nlu_file:
    yaml.dump(nlu_data, nlu_file, default_flow_style=False)

# Fetch responses
cursor.execute("SELECT name, response FROM responses")
responses = cursor.fetchall()

domain_data = {
    "version": "2.0",
    "intents": [intent[0] for intent in intents],
    "responses": {}
}

for response in responses:
    domain_data["responses"][response[0]] = [{"text": response[1]}]

with open("domain.yml", "w") as domain_file:
    yaml.dump(domain_data, domain_file, default_flow_style=False)

# Fetch stories
cursor.execute("SELECT name, steps FROM stories")
stories = cursor.fetchall()

stories_data = {"stories": []}
for story in stories:
    stories_data["stories"].append({
        "story": story[0],
        "steps": yaml.safe_load(story[1])
    })

with open("data/stories.yml", "w") as stories_file:
    yaml.dump(stories_data, stories_file, default_flow_style=False)

print("YAML files generated successfully!")

# Close the database connection
cursor.close()
db.close()
