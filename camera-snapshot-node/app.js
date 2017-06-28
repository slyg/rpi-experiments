const Koa = require('koa')
const route = require('koa-route')
const serve = require('koa-static')
const app = new Koa()

app.use(serve('shots/'))

app.use(route.get('/snap', async function(ctx){
  ctx.body = 'ok'
}));

app.listen(3000)
