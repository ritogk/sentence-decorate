async function test() {
  const cells = document.getElementsByTagName("p")

  for (var i in cells) {
    let innnerHtml = cells[i].innerHTML
    const innerText = cells[i].innerText

    if (innerText.length < 15) continue
    const params = { sentents: innerText }
    const query = new URLSearchParams(params)
    response = await fetch(`https://c521-126-167-41-14.ngrok.io?${query}`, {
      method: "GET",
      mode: "cors",
    })
      .then((response) => {
        return response.json()
      })
      .then((data) => {
        if (!data) return
        for (var c in data) {
          // 述語
          predicates = data[c].predicates
          for (var j in predicates) {
            innnerHtml = innnerHtml.replace(
              predicates[j],
              `<span style=color:red>${predicates[j]}</span>`
            )
            cells[i].innerHTML = innnerHtml
          }

          // 目的語
          objects = data[c].objects
          for (var j in objects) {
            innnerHtml = innnerHtml.replace(
              objects[j],
              `<span style=color:blue>${objects[j]}</span>`
            )
            cells[i].innerHTML = innnerHtml
          }
          console.log(data[c].sentent)
          if (
            data[c].sentent ==
            "高市氏は10日の内閣改造・党役員人事で自民党政調会長を辞し、経済安保担当相に就任"
          ) {
            debugger
          }
          // 主語
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
    console.log(response)
  }
}
