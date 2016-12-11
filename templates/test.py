{% extends "layout.html" %}

{% block title %}
Experiment I
{%  endblock %}

{% block content %}
<html>
<head>
<script src="../static/js/brython.js"></script>
</head>
<body onload="brython()">
<script type="text/python">
from browser import document, alert

def echo(ev):
    alert(document["zone"].value)

document['mybutton'].bind('click',echo)
</script>
<button id="mybutton">click me</button>

</body>
</html>

{% endblock %}
