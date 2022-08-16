async function decorate() {
  const serverOrigin = 'https://c521-126-167-41-14.ngrok.io';
  
  const cells = document.getElementsByTagName("p")
  for (var i in cells) {
    let innnerHtml = cells[i].innerHTML
    const innerText = cells[i].innerText

    if (innerText.length < 15) continue

    const params = { sentents: innerText }
    const query = new URLSearchParams(params)
    response = await fetch(`${serverOrigin}/spacy?${query}`, {
      method: "GET",
      mode: "cors",
    })
      .then((response) => {
        return response.json()
      })
      .then((data) => {
        if (!data) return
        for (var c in data) {
          // 述語に色を付ける
          predicates = data[c].predicates
          for (var j in predicates) {
            innnerHtml = innnerHtml.replace(
              predicates[j],
              `<span style=color:red>${predicates[j]}</span>`
            )
            cells[i].innerHTML = innnerHtml
          }

          // 目的語に色を付ける
          objects = data[c].objects
          for (var j in objects) {
            innnerHtml = innnerHtml.replace(
              objects[j],
              `<span style=color:blue>${objects[j]}</span>`
            )
            cells[i].innerHTML = innnerHtml
          }

          // 主語に色を付ける
          subjects = data[c].subjects
          for (var j in subjects) {
            innnerHtml = innnerHtml.replace(
              subjects[j],
              `<span style=color:green>${subjects[j]}</span>`
            )
            cells[i].innerHTML = innnerHtml
          }
        }
      })
  }
}
