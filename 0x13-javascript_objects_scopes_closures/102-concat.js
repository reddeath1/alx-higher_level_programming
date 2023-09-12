#!/usr/bin/node
const argv = process.argv;
const file = require('fs');
const fileA = argv[2];
const tA = file.readFileSync(fileA, 'utf8');
const fileB = argv[3];
const tB = file.readFileSync(fileB, 'utf8');
const fileC = argv[4];
file.writeFileSync(fileC, tA + tB);
