const five = require('johnny-five')
const Raspi = require('raspi-io')
const board = new five.Board({ io: new Raspi() })

const CYCLE_DURATION = 1000
const LOOP_START_DELAY = 100
const END_OF_ALL_DELAY = 5000

const delay = time => new Promise(resolve => setTimeout(resolve, time))

// One cycle for a given relay
const cycle = relay => async function() {
  relay.open()
  await delay(CYCLE_DURATION/2)
  relay.close()
}

const terminate = (loops, relays) => () => {
  loops.forEach(clearInterval)
  relays.close()
}

board.on('ready', function() {

  const relays = new five.Relays(['P1-12', 'P1-16', 'P1-18', 'P1-22'])
  const [ONE, TWO, THREE, FOUR] = relays

  let loops = [] // reference to all loops (intervals)

  relays.forEach(async function(relay, index) {
    // Delayed start of looping cycle
    await delay(index * LOOP_START_DELAY)
    loops[index] = setInterval( cycle(relay), CYCLE_DURATION )
  })

  setTimeout(terminate(loops, relays), END_OF_ALL_DELAY)

  this.repl.inject({ relays, ONE, TWO, THREE, FOUR })

})
