Rock Paper Scissors
###################

:date: 2013-4-8 16:33
:status: published
:tldr: TL;DR; Computers are better than you at even simple games. Watch it whoop you at rock paper scissors.


Want to play a game?

.. html::

    <div class="project text-center" id="rps-div">Loading...</div>
    <script>aza.lab_experiment((true ? "http://rps.labs.andrewzallen.com/rps.js" : "http://localhost:5000/rps.js"), $("#rps-div"), function() {rps.main($("#rps-div"))})</script>

This is a very simple implementation of a Rock Paper Scissors (RPS) game.

Weighing in at 157 lines of JavaScript and 179 lines of Python, the application tracks previous users play patterns to create a probability distribution of your next throw.
Given this probability distribution, the game takes a weighted guess at your next throw and then throws whatever will beat that.

All source is available at my `github <https://github.com/achew22/rps>`_.