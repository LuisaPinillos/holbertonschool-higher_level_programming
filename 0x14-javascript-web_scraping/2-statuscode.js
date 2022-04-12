#!/usr/bin/node

// script that display the status code of a GET request.

var myUrl = process.argv[2];
const req = require('request');

req (myUrl, function (error, response) {
    if (error) {
     console.log(error);
    } else {
     console.log('code:', response.statusCode);
    }
   });
