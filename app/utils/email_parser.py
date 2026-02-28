import email
from email.header import decode_header
import base64

def parse_email(raw_email: str) -> dict:
    msg = email.message_from_string(raw_email)
    parsed = {
        "headers": dict(msg.items()),
        "body": "",
        "attachments": []
    }
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                parsed["body"] = part.get_payload(decode=True).decode()
            elif part.get_filename():
                attachment = {
                    "filename": part.get_filename(),
                    "content": base64.b64decode(part.get_payload())
                }
                parsed["attachments"].append(attachment)
    else:
        parsed["body"] = msg.get_payload(decode=True).decode()
    return parsed