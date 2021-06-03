# CovidJabNL

1. Install the requirements.
2. Execute `python covid.py --year <year> --email <email>`

When the year that you insert is getting called for vaccination, the email that you input will receive an email.

### Deploy

You can deploy this in a VM, using a cronjob. Don't send the same request too frequent, since this might overload the website, and that's not the intention.
