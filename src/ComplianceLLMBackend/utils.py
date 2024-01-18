import getpass
import json
import os


def load_config(file_path):
    try:
        with open(file_path, 'r') as config_file:
            config_data = json.load(config_file)
        return config_data
    except FileNotFoundError:
        print(f"Error: Config file not found at {file_path}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in config file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def load_files(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"The file at path {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def check_api_key(api_key_var_name: str = 'OPENAI_API_KEY') -> str:
    """
    Check if an API key is available in the environment variable or prompt the user to enter it.

    Args:
        api_key_var_name (str): The name of the API key environment variable.

    Returns:
        str: The API key.
    """
    # Check if the API key environment variable is set
    api_key = os.getenv('OPEN_AI_KEY')

    if api_key is None:
        # If not set, raise an error
        raise ValueError(f"{api_key_var_name} API key not found in environment variables.")

    return api_key