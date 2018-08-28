google2fact
_____________________

What is it for?

    It's a little part of selenium macros / test what keep a google 2 auth based
on back ups codes.

So you need just to get your backup codes - and you can automate routine step
with selenium


How does it work::

    gif

Prerequisites::

    selenium

Tested with versions::

    selenium==3.14.0

    chromedriver 2.41 for mac
    (https://chromedriver.storage.googleapis.com/index.html?path=2.41/)

It's a set of python scripts provided to work with google2fact auth

For correct script's work you need to set environment variables::

    export GMAIL=your@gmail.com
    export GMAIL_PASSWORD=your_password
    export GMAIL_CODES=path_to_your_file_with_codes.txt

You can add them to ~/.bash_profile to avoid manually setting this variables

If you don't like this way - just open google2fact.py and change this::

    user_mail = getenv('GMAIL')
    password = getenv('GMAIL_PASSWORD')

to your password and account

And inside read_codes.py::

    codes_file = os.path.join(tmp_path, os.environ("GMAIL_CODES"))


To use::

  from google2fact import google2fact

  google2fact.get_auth(driver)

# driver - it's A selenium driver object, what usually initialised with::

    browser = webdriver.Chrome(executable_path="path/to/your/chromedriver")


Backup codes file
_________________


Get Backup codes for your account with 2-Step Verification:

https://myaccount.google.com/u/1/signinoptions/two-step-verification:

    Backup codes --> SHOW CODE --> DOWNLOAD

If no codes exist - click GET NEW CODES and when --> DOWNLOAD

Put you file Backup-codes-{youraccount}.txt in 'tmp' dir
