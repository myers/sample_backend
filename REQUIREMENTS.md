# Back End Take Home Exercise

## Overview

Implement a small api for interacting with a callback based third-party
service.

## Requirements


Implement an application that can be used as an intermediary for a
third-party service.  The third party service accepts a document request
payload which includes a callback url and will respond to that url when the
document is ready, which may be up to 10 business days later.  Your
application is expected to have four endpoints.  These may be implemented as
a stateful service, or multiple stateless services/functions connected to a
store.  The state must be stored somewhere (if in memory, please note how to
store at rest).  Each should respond to an http request and follow the REST
conventions for methods.  The endpoints should meet the following
requirements: 


### POST a request 

* POST /request
* BODY: Object { "body": String } 
* RETURNS String 

This should accept a JSON body consisting of a one key, "body", which is a
string.  Doing this should initiate a request to the third-party service. 
It will also create a unique identifier for this request we can later
reference.  The request to the third party service should be a stubbed out,
to call `http://example.com/request" with the following payload:

* BODY `Object: { "body": {body}, "callback": "/callback/{id}" }`

Comments or other indicators on how you would actually call this service are
recommended, as well as any additional concerns around error
handling/logging.

### POST callback 

* POST /callback/{id} 
* BODY String 
* RETURNS 204

This URL should be sent in the original request. Afterward, the service will
send an initial POST with the text string `STARTED` to indicate it's they
received the request.


### PUT callback 

* PUT /callback/{id}
* BODY `Object { "status": String, "detail": String }`
* RETURNS 204

At some later date, it will PUT status updates to this callback URL, each
which will have a json object with the keys of `status` and `detail`.  The
status will be one of `PROCESSED`, `COMPLETED` or `ERROR`.  The detail will
be a text string.


### GET status

* GET /status/{id}
* RETURNS `Object { "status": String, "detail": String, "body": String }`

Finally, given the unique ID, we should be able to get the status of the
request from our application.  It will give us the status, detail and
original body, as well as timestamps for when it was created and when the
latest update occurred.  

