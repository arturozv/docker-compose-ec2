'use strict';

const express = require('express');
const redis = require("redis");

const app = express();
const client = redis.createClient(6379, 'redis');

client.set("fiat", JSON.stringify({make:"fiat", model:"500"}));
client.set("ford", JSON.stringify({make:"ford", model:"mustang"}));

app.get('/:make', (req, res) => {
  client.get(req.params.make, function(err, reply) {
    res.json({response: JSON.parse(reply), error: err});
  });
});

app.get('/', (req, res) => {
  res.json({message:"hello there! try getting some redis data from url:/fiat"});
});

app.listen(8090);
console.log("server started!")