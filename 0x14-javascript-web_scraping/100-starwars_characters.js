#!/usr/bin/nod
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide a Movie ID as the first argument.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
    process.exit(1);
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  if (!characters || characters.length === 0) {
    console.log('No characters found for this movie.');
    process.exit(0);
  }

  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error fetching character:', charError);
      }

      if (charResponse.statusCode === 200) {
        const character = JSON.parse(charBody);
        console.log(character.name);
      } else {
        console.error('Error fetching character. Status code:', charResponse.statusCode);
      }
    });
  });
});
e
