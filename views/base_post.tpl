<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>base_post</title>
    <script>
      document.addEventListener("DOMContentLoaded", function() {
        // https://web.archive.org/web/2/https://developer.mozilla.org/en-US/docs/Web/API/EventSource
        const eventSource = new EventSource("/stream/{{choice}}/{{logtime}}");
        const eventList = document.getElementById("log");
        eventSource.addEventListener("message", function(e) {
          var newElement = document.createElement("p");
          newElement.innerText = e.data;
          eventList.appendChild(newElement);
        });
      });
    </script>
  </head>
  <body>
    <div id="log"></div>
    <p><a href="/">return to form</a></p>
  </body>
</html>
