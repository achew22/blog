The Backend
###########

:date: 2013-2-17 10:39
:tags: programming, GoSpotCheck
:category: programming
:parts: gospotcheck-architecture
:status: published

Writing any kind of mobile application for :abbr:`B2B (Busines To Business)`
requires some central command and control server. For GoSpotCheck, that is the
beaver, the hub and spoke of the SpotChecking system.

Beaver operates as a `grails <http://grails.org>`_ application that is constantly running, managed by
`Amazon EC2 <http://aws.amazon.com>`_. The service accesses the database and
essentially provides a very simple interface for client interaction. All
API requests came through in a JSON format and all responses were in kind.
The same beaver server also serves the GoSpotCheck homepage/admin panel which
prevented the pain that is
`CORS <http://en.wikipedia.org/wiki/Cross-origin_resource_sharing>`_ from
entering our lives.

All requests were atomic, no `PATCH <http://tools.ietf.org/html/rfc5789>`_, which allowed us an interesting opportunity to treat the backend not as a webserver but instead as a GoSpotCheck specific database.
It implemented methods and stored data that only we would find useful.
The fact that it was really persisted to a database deeper in the stack was inconsequential to us.
All we cared about was that the database was atomic, consistent, isolate, and durable.
A model that should be easy any newcomer from any CS program in the world to reason about.

This system was extremely decoupled which meant that when we experienced problems in any one system (less the core), the others continued to operate as if everything were normal.

Next time I will talk about the development of `the frontend <|filename|003_the_frontend.rst>`_ and some of the more interesting things we did with it.