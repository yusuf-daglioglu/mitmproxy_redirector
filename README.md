# mitmproxy redirector
With this script you can redirect only specific HTTP and Web-socket requests of your web browser to your local (or any other) web applications.

# Why do I need this? I can already change "hosts" file.
You can also edit "hosts" file of your OS. But:
- manipulation "hosts" file requires admin privileges.
- using "hosts" file you can only change "domain" part of URL. You can not do below example with "hosts" file:

   > http://api-gateway.mydomain.com/service2 (you don't want redirect the service2)

   > http://api-gateway.mydomain.com/service1 (you want to redirect service1 to localhost)

- If you have multiple browsers or browser-profiles with that script you can redirect only 1 browser instance. With "hosts" file you can only redirect whole system to same direction. For example: you may want to check "service1" both remote and localhost environment at the same time from different web browsers (or web browser profiles).

# Requirements
- This script can be run only with user privileges.
- Mitmproxy has standalone executable for all OSes. You don't have to install it.

## Usage

- ### Certificate

Add $HOME/.mitmproxy/mitmproxy-ca-cert.cert file to web browser (only current browser profile is enough). This certificate file is creating after the first run of mitmproxy.

For Firefox:
- Settings
- View Certificates
- Authorities
- Import
- Choose $HOME/.mitmproxy/mitmproxy-ca-cert.cert file only.

OS based certificate formats exist. Read this: https://docs.mitmproxy.org/stable/concepts-certificates/#the-mitmproxy-certificate-authority

- ### Defining the proxy to web browser

Add proxy for http and https: localhost:44700

- ### Run mitmproxy

Linux

> ./mitmweb -s mitm-redirect-url.py --listen-port 44700

MS Windows

> mitmweb.exe -s mitm-redirect-url.py --listen-port 44700

- ### Ignore CORS (Optional)

Optionally you can ignore CORS for your current browser profile. You can use below extension for Firefox:

https://addons.mozilla.org/en-US/firefox/addon/cors-everywhere/
