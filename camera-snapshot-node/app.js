const Koa = require('koa')
const route = require('koa-route')
const serve = require('koa-static')
const app = new Koa()

const PiCamera = require('pi-camera');
const myCamera = new PiCamera({
  mode: 'photo',
  output: `${ __dirname }/shots/test.jpg`,
  nopreview: true,
});

app.use(serve('shots/'))

app.use(route.get('/snap', async function(ctx){
  try {
    const result = await myCamera.snap()
    ctx.body = {error: undefined, result}
  } catch (error) {
    ctx.body = {error, result: undefined}
  }
}));

app.listen(3000)
