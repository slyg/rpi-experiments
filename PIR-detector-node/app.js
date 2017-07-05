const five = require('johnny-five')
const Raspi = require('raspi-io')
const board = new five.Board({ io: new Raspi() })

board.on('ready', function() {

  const motion = new five.Motion('P1-7')
  const led = new five.Led('P1-12')
  const FADE_DURATION = 1000

  motion
    .on('calibrated', () => { console.log('Motion sensor ready') })
    .on('motionstart', () => { led.fadeIn(FADE_DURATION) })
    .on('motionend', () => { led.fadeOut(FADE_DURATION) })

  this.repl.inject({ motion, led })

})
