from typing import (
    Dict,
    List,
)


class Message:
    """
    A class to create and manage messages for chat conversations.

    Methods:
        system(content: str) -> None:
            Adds a system message with the specified content.

        user(content: str) -> None:
            Adds a user message with the specified content.

        assistant(content: str) -> None:
            Adds an assistant message with the specified content.

    Attributes:
        messages (List[Dict[str, str]]): A list of message dictionaries.
    """

    def __init__(self):
        self.messages = []

    def system(self, content: str) -> None:
        """
        Adds a system message with the specified content.

        Args:
            content (str): The content of the system message.

        Returns:
            None
        """
        self.messages.append({"role": "system", "content": f"""{str(content)}"""})

    def user(self, content: str) -> None:
        """
        Adds a user message with the specified content.

        Args:
            content (str): The content of the user message.

        Returns:
            None
        """
        self.messages.append({"role": "user", "content": f"""{str(content)}"""})

