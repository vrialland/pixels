window.addEventListener("DOMContentLoaded", () => {
  const { hostname, port } = window.location
  const ws = new WebSocket(`ws://${hostname}:${port}/ws`)
  ws.onopen = () => console.log('Connection ready!')
  ws.onerror = (error) => console.error(error.message)
  ws.onclose = () => console.log('Connection closed!')
  ws.onmessage = (e) => console.log(`Received ${e.data}`);

  const cells = document.querySelectorAll('td')
  for (let cell of cells) {
    cell.addEventListener("click", (ev) => {
      const { row, col } = ev.target.dataset
      const color = document.getElementById("color").value
      const data = {
        action: "set_color",
        color,
        row,
        col
      }
      ws.send(JSON.stringify(data))
      console.log(`Set color to ${color} on ${row},${col}`)
      ev.target.style.backgroundColor = color
    })
    cell.addEventListener("contextmenu", (ev) => {
      const { row, col } = ev.target.dataset
      const data = {
        action: "reset_color",
        row,
        col
      }
      ws.send(JSON.stringify(data))
      console.log(`Reset color on ${row},${col}`)
      ev.target.style.backgroundColor = "black"
      ev.preventDefault()
    })
  }
})
