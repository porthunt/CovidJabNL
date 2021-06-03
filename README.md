# CovidJabNL

1. Install the requirements.
2. Execute `./covid.py --year <year> --dest-email <email> --source-email <email>`

When the year that you insert is getting called for vaccination, the email that you input will receive an email. AWS SES needs validated emails, so the source email should also be validated. If your account is not on sandbox mode, sending to whatever email works.

### Deploy

You can deploy this in a VM, using a cronjob. Don't send the same request too frequent, since this might overload the website, and that's not the intention.
