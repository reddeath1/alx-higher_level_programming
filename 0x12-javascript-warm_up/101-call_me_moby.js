#!/usr/bin/node
exports.callMeMoby = function (number, func) {
  for (let i = 0; i < number; i++) {
    func();
  }
};
