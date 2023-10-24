#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let datas;
let movies = 0;
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    datas = JSON.parse(body);
    datas.results.forEach(function (result) {
      result.characters.forEach(function (character) {
        const split = character.split('/');
        if (split[split.length - 2] === '18') {
          movies++;
        }
      });
    });
    console.log(movies);
  }
});
