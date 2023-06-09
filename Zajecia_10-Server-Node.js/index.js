
// import { Operation } from './module.mjs';
const Operation = require('./module');

const myArgs = process.argv.slice(2);

const operation = new Operation(parseInt(myArgs[0]), parseInt(myArgs[1]));
console.log(operation.sum())

