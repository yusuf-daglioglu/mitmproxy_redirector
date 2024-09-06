from mitmproxy import http

print('custom redirect add on: init')

routers = []
routers.append(("ws://user999:8080", "127.0.0.1", 8080))
routers.append(("http://user999:8080", "127.0.0.1", 8080))

print('custom redirect add on: redirect config urls:')
print(routers)

def request(flow: http.HTTPFlow) -> None:
    currentUrl = flow.request.url
    if routers is not None:
        for urlStartWithStr, redirectToDomainUrl, redirectToPort in routers:

            # trace logs:
            print("currentUrl:" + currentUrl)
            print("urlStartWithStr:" + urlStartWithStr)
            print("redirectToDomainUrl:" + redirectToDomainUrl)
            print(currentUrl.startswith(urlStartWithStr))

            if currentUrl.startswith(urlStartWithStr) == True: # and currentUrl.startswith("http") == True:
                print('custom redirect add on: redirected: ' + currentUrl + " >>> " + redirectToDomainUrl)

                flow.request.host = redirectToDomainUrl
                flow.request.port = redirectToPort
                # if you need to change other parts of URL, check this:
                # https://github.com/mitmproxy/mitmproxy/blob/9d47d3b1ecaed6db1d143a56973e931140ad1949/netlib/http/request.py#L186

                flow.request.headers["Host"] = redirectToDomainUrl + ":" + str(redirectToPort)
                flow.request.headers["Origin"] = "http://" + redirectToDomainUrl + ":" + str(redirectToPort)

# other sources and examples:
# https://github.com/KevCui/mitm-scripts/blob/master/mitm-redirect-url.py
# https://docs.mitmproxy.org/stable/overview-features/#map-remote
# https://docs.mitmproxy.org/stable/addons-examples/#http-redirect-requests
