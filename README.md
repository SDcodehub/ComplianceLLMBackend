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
pip install ComplianceLLMBackend
```

```python
from ComplianceLLMBackend import ...
```

## Contributing

```bash
# clone the repo
git clone https://github.com/SDcodehub/ComplianceLLMBackend.git

# install the dev dependencies
make install

# run the tests
make test
```
