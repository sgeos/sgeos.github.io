---
layout: post
comments: true
title:  "A Shell Script for Working with Phoenix JSON APIs"
date:   2016-03-19 00:55:41 +0000
categories: phoenix elixir sh
---
I started writing another post, but wound up writing a non-trivial script for
working with Phoenix JSON APIs.
That script is covered in this post.
It is written for the FreeBSD Bourne shell, but it should be compatible with **bash**.
This post also serves as a **getopts** example.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-03-19 00:55:41 +0000
$ mix hex.info
Hex:    0.11.3
Elixir: 1.2.3
OTP:    18.2.4
* snip *
$ mix phoenix.new -v
Phoenix v1.1.4
{% endhighlight %}

## Instructions

Create a new Phoenix project.

{% highlight sh %}
mix phoenix.new phoenix_service --no-brunch
cd phoenix_service
mix ecto.create
{% endhighlight %}

This example will use a JSON memo service.

{% highlight sh %}
mix phoenix.gen.json Memo memos title:string body:string
{% endhighlight %}

Revise the **web/router.ex** file.
The "/api" scope needs to be uncommented and the "/memos" route needs to be added.

**web/router.ex file**
{% highlight elixer %}
defmodule PhoenixService.Router do
  use PhoenixService.Web, :router

  pipeline :browser do
    plug :accepts, ["html"]
    plug :fetch_session
    plug :fetch_flash
    plug :protect_from_forgery
    plug :put_secure_browser_headers
  end

  pipeline :api do
    plug :accepts, ["json"]
  end

  scope "/", PhoenixService do
    pipe_through :browser # Use the default browser stack
  
    get "/", PageController, :index
  end

  scope "/api", PhoenixService do
    pipe_through :api

    resources "/memos", MemoController, except: [:new, :edit]
  end
end
{% endhighlight %}

Run the migration.

{% highlight sh %}
mix ecto.migrate
{% endhighlight %}

Tests should pass.

{% highlight sh %}
mix test
{% endhighlight %}

# Running the Sample Project

Start the server.

{% highlight sh %}
mix phoenix.server
{% endhighlight %}

The following **curl** commands can be used to interact with the JSON API.

{% highlight sh %}
# POST new
curl -H 'Content-Type: application/json' -X POST -d '{"memo": {"title": "New Title", "body": "This is the new memo body."}}' http://localhost:4000/api/memos
# PATCH id 1
curl -H 'Content-Type: application/json' -X PATCH -d '{"memo": {"title": "Patched Title"}}' http://localhost:4000/api/memos/1
curl -H 'Content-Type: application/json' -X PATCH -d '{"memo": {"body": "Patched memo body."}}' http://localhost:4000/api/memos/1
# PUT id 1
curl -H 'Content-Type: application/json' -X PUT -d '{"memo": {"title": "Updated Title", "body": "Updated memo body."}}' http://localhost:4000/api/memos/1
# GET all
curl -H 'Content-Type: application/json' http://localhost:4000/api/memos
# GET id 1
curl -H 'Content-Type: application/json' http://localhost:4000/api/memos/1
# DELETE id 1
curl -H 'Content-Type: application/json' -X DELETE http://localhost:4000/api/memos/1
{% endhighlight %}

A script is easier to use if you need to make more than a couple of **curl** calls.
It can also be extended to support authentication and everything else your API may need.

Create a script to GET, POST, PATCH, PUT and DELETE memos.
Note that a Bourne Shell tutorial can be found [here][sh-tutorial].

**memo_api.sh**
{% highlight sh %}
#!/bin/sh

reset() {
  HOST=http://localhost:4000
  SCOPE=api
  ROUTE=memos
  METHOD="GET"
  HEADERS="Content-Type: application/json"
  ID=""
  TITLE=""
  BODY=""
}

usage() {
  reset
  echo "Usage:  ${0} [options]"
  echo "Options:"
  echo "  -o HOST : set URL host, defaults to \"${HOST}\""
  echo "  -s SCOPE : set URL scope, defaults to \"${SCOPE}\""
  echo "  -r ROUTE : set URL route, defaults to \"${ROUTE}\""
  echo "  -X METHOD : set HTTP method, defaults to \"${METHOD}\""
  echo "  -H HEADERS : set HTTP headers, defaults to \"${HEADERS}\""
  echo "  -i ID : set memo id, defaults to \"${ID}\""
  echo "  -t TITLE : set memo title, defaults to \"${TITLE}\""
  echo "  -b BODY : set memo body, defaults to \"${BODY}\""
  echo "  -h : display this help"
  echo "Examples:"
  echo "  ${0} -X GET"
  echo "  ${0} -X GET -i 7"
  echo "  ${0} -X POST -t \"Memo Title\" -b \"Memo body here.\""
  echo "  ${0} -X PATCH -t \"Patched title.\" -i 7"
  echo "  ${0} -X PATCH -b \"Patched body.\" -i 7"
  echo "  ${0} -X PUT -t \"New Title\" -b \"New body.\" -i 7"
  echo "  ${0} -X DELETE -i 7"
  exit ${1}
}

reset
while getopts "o:s:r:X:H:i:t:b:h" opt
do
  case "${opt}" in
    o) HOST="${OPTARG}" ;;
    s) SCOPE="${OPTARG}" ;;
    r) ROUTE="${OPTARG}" ;;
    X) METHOD="${OPTARG}" ;;
    H) HEADERS="${OPTARG}" ;;
    i) ID="${OPTARG}" ;;
    t) TITLE="${OPTARG}" ;;
    b) BODY="${OPTARG}" ;;
    h) usage 1 ;;
    \?) usage 2 ;;
  esac
done
shift $(expr ${OPTIND} - 1)

case "${METHOD}" in
  GET)
    curl -H "${HEADERS}" -X ${METHOD} "${HOST}/${SCOPE}/${ROUTE}${ID:+"/${ID}"}"
    ;;
  POST)
    PAYLOAD='{"memo": {"title": "'"${TITLE:-(no title)}"'", "body": "'"${BODY:-(no body)}"'"}}'
    curl -H "${HEADERS}" -X ${METHOD} -d "${PAYLOAD}" "${HOST}/${SCOPE}/${ROUTE}" 
    ;;
  PUT)
    PAYLOAD='{"memo": {"title": "'"${TITLE:-(no title)}"'", "body": "'"${BODY:-(no body)}"'"}}'
    curl -H "${HEADERS}" -X ${METHOD} -d "${PAYLOAD}" "${HOST}/${SCOPE}/${ROUTE}/${ID:?'No ID specified.'}" 
    ;;
  PATCH)
    # if defined replace individual fields with
    # JSON fragments followed by a comma and space
    TITLE=${TITLE:+"\"title\": \"${TITLE}\", "}
    BODY=${BODY:+"\"body\": \"${BODY}\", "}
    # strip trailing comma and space
    PAYLOAD="$(echo "${TITLE}${BODY}" | sed 's/, $//g')"
    # complete JSON payload
    PAYLOAD="{\"memo\": {${PAYLOAD}}}"
    curl -H "${HEADERS}" -X ${METHOD} -d "${PAYLOAD}" "${HOST}/${SCOPE}/${ROUTE}/${ID:?'No ID specified.'}" 
    ;;
  DELETE)
    curl -H "${HEADERS}" -X ${METHOD} "${HOST}/${SCOPE}/${ROUTE}/${ID:?'No ID specified.'}"
    ;;
  *)
    usage 2
    ;;
esac
echo ""
{% endhighlight %}

The reset function resets the variables to their initial state.
It is called before parsing command line arguments and displaying the usage.

The usage function displays usage, options and examples.
It also terminates the script.

The **getopts** loop parses command line arguments into variables.

The case statement at the end uses the HTTP method to select a **curl** call.

- The GET method works with or without an id.
- The POST method creates a payload and posts it.
- PUT is like post except the verb is different and it requires an id.
- PATCH is the most complicated.
  It builds a payload and strips the trailing comma.
  Then it sends the payload to a URL with an id.
- DELETE requires an id.

The script can be used as follows.
Note that trying to delete a memo that does not exist will fail with a wall of HTML.

{% highlight sh %}
chmod +x memo_api.sh
./memo_api.sh -X POST -t "Memo Title" -b "Memo body here."
./memo_api.sh -X GET -i 1
./memo_api.sh -X POST -t "Another Memo" -b "This memo's body."
./memo_api.sh -X PATCH -t "Patched title." -i 2
./memo_api.sh -X PATCH -b "Patched body." -i 1
./memo_api.sh -X PUT -t "New Title" -b "New body." -i 2
./memo_api.sh -X GET
./memo_api.sh -X DELETE -i 1
{% endhighlight %}

This script could be customized to work with other APIs.

## References:
- [sh, Handling Command Line Arguments][sh-getopts]
- [sh, the Bourne Shell][sh-tutorial]
- [sh, Turning multiple lines into one line with comma separated][sh-comma]
- [sh, Bourne Shell: Counting Character Occurrence in a Unicode Text File][sh-count]
- [Phoenix, Deployment][phoenix-deployment]
- [Phoenix, Building a JSON API With Phoenix][phoenix-json]
- [Phoenix, Building a versioned REST API with Phoenix Framework][phoenix-versioned-rest]
- [Elixir as a Service on FreeBSD][elixir-service]
- [REST API PATCH or PUT][rest-patch-put]

[sh-getopts]: http://www.shelldorado.com/goodcoding/cmdargs.html
[sh-tutorial]: http://www.grymoire.com/Unix/Sh.html
[sh-comma]: http://stackoverflow.com/questions/15758814/turning-multiple-lines-into-one-line-with-comma-separated-perl-sed-awk
[sh-count]: https://sgeos.github.io/sh/2016/02/23/bourne-shell-counting-character-occurrence-in-unicode-text-file.html
[phoenix-deployment]: http://www.phoenixframework.org/docs/deployment
[phoenix-json]: http://learnwithjeff.com/blog/2015/10/03/building-a-json-api-with-phoenix/
[phoenix-versioned-rest]: https://renatomoya.github.io/2015/05/09/Building-a-versioned-REST-API-with-Phoenix-Framework.html
[elixir-service]: https://sgeos.github.io/elixir/erlang/2016/01/16/elixir-as-a-service_on_freebsd.html
[postgresql-install]: https://jasonk2600.wordpress.com/2010/01/11/installing-postgresql-on-freebsd/
[rest-patch-put]: http://stackoverflow.com/questions/24241893/rest-api-patch-or-put

