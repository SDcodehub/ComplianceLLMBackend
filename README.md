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
# rename the sample_env_sample to .env file, this is required to load the api key
# GPT-4 model is recomended,  current prompts works with gpt4 model
# python 3.11.2
python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

# to start api end point
python main.py

# to send requests
curl -X POST -H "Content-Type: application/json" -d '{"url":"https://www.joinguava.com"}' http://localhost:5000/check-compliance
```

## Sample example
given the website `https://www.joinguava.com` and compliance rule as per `https://stripe.com/docs/treasury/marketing-treasury`

following are results - 
1. Point 1: The website refers to Guava as a \"digital banking and networking platform\" and a \"banking platform\". This is a violation of the compliance policy which prohibits the use of terms like \"banking\" and \"banking platform\" unless the entity is a state- or federally-chartered bank or credit union.
2. Point 2: The website encourages users to \"Create your business checking account for free\". This is a violation of the compliance policy which prohibits the use of the term \"bank account\" or any variations of it.
3. Point 3: The website refers to Guava as a \"banking platform\" again in the testimonial section. This is another violation of the compliance policy which prohibits the use of the term \"banking platform\".
4. Point 4: The website does not provide any information about FDIC insurance eligibility, which is a requirement of the compliance policy. The policy requires that the statement of FDIC insurance eligibility must always be paired with two disclosures.
5. Point 5: The website does not provide any information about yield, which is a requirement of the compliance policy. The policy requires that the yield percentage is prominently displayed in marketing materials and that customers are notified whenever the yield percentage has changed.s
