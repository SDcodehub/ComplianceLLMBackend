# ComplianceLLMBackend

The task is to build an API that does the following:

* Take a webpage as the input and it has to check the content in the page against a compliance policy
* Return the findings (non-compliant results) in the response

As an example, we take

Stripe's public compliance policy: https://stripe.com/docs/treasury/marketing-treasury
Lets test it against https://www.joinguava.com/

The task is to build a simple API in any language that checks the webpage copy against the policy and report the findings. 
You can use OpenAI or any open-source LLMs for this purpose

## Quick start

```bash
# for linux
git clone https://github.com/SDcodehub/ComplianceLLMBackend.git

git checkout dev

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

# to start api end point
python main.py

# to send requests
curl -X POST -H "Content-Type: application/json" -d '{"url":"https://www.joinguava.com"}' http://localhost:5000/check-compliance
```
