### Regex to get the transaction details from email
(.+?):	(.+?)\n

### How to save the email payload
```python
# ! Remove before commit
        import json

        subject = None
        subjects = [header['value'] for header in email['payload']['headers'] if header['name'] == 'Subject']
        if subjects and len(subjects) > 0:
            subject = subjects[0]

        with open("resorces/payloads.txt", "a", encoding="utf-8") as file:
            email = {"subject":subject, "payload":payload}
            file.write(json.dumps(email)+",")
        # ! Remove before commit

```