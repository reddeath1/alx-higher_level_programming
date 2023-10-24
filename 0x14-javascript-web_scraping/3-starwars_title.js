#!/usr/bin/node
const request = require('request');
const movieID = parseInt(process.argv[2]);
const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;
let datas;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    datas = JSON.parse(body);
    console.log(datas.title);
  }
});
