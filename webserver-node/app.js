const Koa = require('koa')
const app = new Koa()

app.use(async function(ctx) {
  ctx.body = 'Hello World'
})

app.listen(3000)
