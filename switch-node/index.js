const five = require('johnny-five')
const Raspi = require('raspi-io')
const board = new five.Board({ io: new Raspi({enableSoftPwm: true}) })

const RED = 'P1-12'
const BTN = 'P1-18'

board.on('ready', function() {

  const led = new five.Led(RED)
  const button = new five.Button(BTN)

  button.on('release', function() {
    led[led.isOn ? 'off' : 'on' ]()
  })

  this.repl.inject({ led, button })

})
