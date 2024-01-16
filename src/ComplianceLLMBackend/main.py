import os

import requests
from dotenv import load_dotenv
from flask import (
    Flask,
    jsonify,
    request,
)
from llm_agents.message import Message
from llm_agents.openai_chat_bot import OpenAIChatBot
from llm_agents.openai_models import (
    ModelType,
    model_type,
)
from utils import (
    check_api_key,
    load_config,
    load_files,
)
from web_scraper import extract_compliance_information

# Initialize Flask app
app = Flask(__name__)

# Load the config file
config_data = load_config("./configs/config.json")
llm_config = load_config("./configs/llmconfig.json")
message_config = load_config("./configs/messages.json")

# Set the configuration settings
app.config.update(config_data)
app.config.update(llm_config)
app.config.update(message_config)

# Load environment variables
load_dotenv()

api_key = check_api_key()

model_choices = [model.value for model in ModelType]

if app.config['model_name'] in model_choices:
    # Model type is in the list
    model = app.config['model_name']
else:
    # Model type is not in the list, default to 'gpt3.5'
    model = ModelType.GPT_3_5_TURBO.value

def create_llm_agent():
    return OpenAIChatBot(
            model=model,
            api_key=api_key,
            chat_config=app.config['model_params']
        )



@app.route('/check-compliance', methods=['POST'])
def check_compliance():
    try:
        url = request.get_json().get('url', '')

        compliance_policy_path = os.path.join(app.config['data_folder_path'], app.config['compliance_file'])

        if not os.path.exists(compliance_policy_path):       
            extract_compliance_information(app.config['compliance_url'], compliance_policy_path) 

        target_file_path = os.path.join(app.config['data_folder_path'], app.config['target_file'])

        if not os.path.exists(target_file_path):
            extract_compliance_information(url, target_file_path)

        compliance_policy = load_files(compliance_policy_path)
        target_web_content = load_files(target_file_path)

        print(f"{app.config['system_message']=}")
        print(f"{app.config['user_message']=}")
        system_message = app.config['system_message'].format(compliance_policy=compliance_policy)

        user_message = app.config['user_message'].format(target_web_content=target_web_content)

        message = Message()
        message.system(system_message)
        message.user(user_message)

        llm_chat_agent = create_llm_agent()

        result = llm_chat_agent.send_messages_and_get_response(messages = message.messages)

        if result is None:
            return jsonify({"error": "Failed to check compliance"}), 500

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)