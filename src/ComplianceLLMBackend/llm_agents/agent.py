class AgentConversation:
    def __init__(self, app_name, model, app_desc, logger, code_file_path):
    self.app_name = app_name
    self.model = model
    self.app_desc = app_desc
    self.logger = logger
    self.system_formatter = self.setup_system_formatter()
    self.openai_api_key = check_api_key('OPENAI_API_KEY')
    self.chat_bot = self.setup_chat_bot()
    self.company_prompt = "Welcome to SmartAgents"
    self.intermediate_vars = IntermediateVars()
    print(self.intermediate_vars)
    self.code_file_path = code_file_path