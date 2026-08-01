#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (!err) {
    const todos = JSON.parse(body);
    const result = {};
    todos.forEach((todo) => {
      if (todo.completed) {
        const id = todo.userId;
        result[id] = result[id] ? result[id] + 1 : 1;
      }
    });
    console.log(result);
  }
});
