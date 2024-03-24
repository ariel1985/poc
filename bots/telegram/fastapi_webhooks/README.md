# poc for fastApi and telegram webhook

https://www.freecodecamp.org/news/how-to-build-and-deploy-python-telegram-bot-v20-webhooks/


```bash
cd project_name
python -m venv venv
source venv/bin/activate
touch .gitignore README.md main.py .env
```

TODO: populate files: gitignore README.md main.py


# Set up env

Use zrok to set static domain for telegram
This domain will be publicly available for every session of localhost:8000


 ```bash
 zrok release <previouse id>
 zrok reserve public localhost:8000 
 zrok share reserved <new id>
 ```

Run telegram api to set the new domain

api.... {telegram toke}/{newdomain}/webhook_name

Run python fastAPI

```bash
uvicorn main:app --reload
```
