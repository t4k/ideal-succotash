# fmt: off
from gevent import monkey; monkey.patch_all()
# fmt: on

import arrow
import bottle
import rpyc
import sh


server = rpyc.connect("localhost", 18861)


@bottle.route("/")
def base_form():
    return """
        <form action="/" method="post">
            <input type="radio" id="foo" name="choice" value="foo" required>
            <label for="foo">foo</label>
            <input type="radio" id="bar" name="choice" value="bar" required>
            <label for="bar">bar</label>
            <button type="submit">View Stream</button>
        </form>
    """


@bottle.route("/", method="POST")
def base_post():
    choice = bottle.request.forms.get("choice")
    logtime = arrow.now().format("YYYYMMDDHHmmss")
    # asynchronously start process on server
    start = rpyc.async_(server.root.start)
    start(choice, logtime)
    return bottle.template("base_post", choice=choice, logtime=logtime)


@bottle.route("/stream/<choice>/<logtime>")
def stream(choice, logtime):
    # using server-sent events that work with javascript in feature_post.tpl
    bottle.response.content_type = "text/event-stream"
    bottle.response.cache_control = "no-cache"
    for line in sh.tail("-f", f"{choice}-{logtime}.log", _iter=True):
        # the event stream format starts with "data: " and ends with "\n\n"
        # https://web.archive.org/web/2/https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#event_stream_format
        yield f"data: {line}\n\n"


bottle.run(host="localhost", port=8080, server="gevent", reloader=True, debug=True)
