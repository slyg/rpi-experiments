const five = require('johnny-five')
const Raspi = require('raspi-io')
const randomColor = require('randomcolor')
const board = new five.Board({ io: new Raspi({enableSoftPwm: true}) })

const RED   = 'P1-12' // Pin 18
const GREEN = 'P1-16' // Pin 23
const BLUE  = 'P1-18' // Pin 24

board.on('ready', function() {

  const led = new five.Led.RGB([RED, GREEN, BLUE])

  this.loop(500, function() {
    led.color(randomColor())
  })

  this.repl.inject({ led })

})
