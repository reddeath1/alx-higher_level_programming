#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let datas;
const dictionary = {};

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    datas = JSON.parse(body);
    datas.forEach(function (result) {
      if (result.completed === true) {
        const userid = result.userId;
        if (!(userid in dictionary)) {
          dictionary[userid] = 0;
        }
        dictionary[userid] += 1;
      }
    });
    console.log(dictionary);
  }
});
