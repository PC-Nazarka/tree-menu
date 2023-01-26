function changeNested(element) {
  parentElem = element.parentElement.querySelector(".nested")
  if (parentElem != null) {
    parentElem.classList.toggle("active")
  }
}

function setActiveItem(queryParam) {
  const menuClass = "menu"
  let url = new URL(location);
  activeMenuItem = url.search.split(`${queryParam}=`)[1]
  element = document.querySelector(`span[data-item-id="${activeMenuItem}"]`)
  changeNested(element)
  tempElement = element
  while (!tempElement.classList.contains(menuClass)) {
    if (tempElement.parentElement.classList.contains("nested")) {
      tempElement.parentElement.classList.toggle("active")
    }
    tempElement = tempElement.parentNode
  }
}

const reg = /\/[\d+]\//
const queryParam = "menuitem"
let url = new URL(location);
if (url.pathname.match(reg)) {
  link = document.getElementById("link")
  text = link.innerText
  link.parentNode.textContent = text
  link.remove()
}
if (url.search.indexOf(queryParam) !== -1) {
  setActiveItem(queryParam)
}

var toggler = document.getElementsByClassName("caret")

for (let i = 0; i < toggler.length; i++) {
  toggler[i].addEventListener("click", function() {
    changeNested(this)
    if (this.dataset.itemId !== undefined) {
      url.searchParams.set(queryParam, this.dataset.itemId)
      location = url.href
    }
  })
}