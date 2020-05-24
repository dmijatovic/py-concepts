
const app = document.getElementById("api-response")

app.innerHTML=`
  <div>Loading data from Flask API...</div>
`

fetch("api")
  .then(res=>{
    debugger
    console.log(res)
    return res.json()
  })
  .then(data=>{
    debugger 
    app.innerHTML=`<pre>${JSON.stringify(data)}</pre>`
  })
  .catch(e=>{
    debugger
    console.error(e)
    app.innerHTML!=`FAILED! ${JSON.stringify(e)}`
  })