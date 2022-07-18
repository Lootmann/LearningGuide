"use strict";

const baseUrl = "http://127.0.0.1:8888";
const log = console.log;

function getUrl(url) {
  return baseUrl + url;
}

function write(content) {
  log(content);
  document.getElementById("display").innerHTML = JSON.stringify(
    content,
    null,
    "  "
  );
}

// ping
function ping() {
  fetch(getUrl(""))
    .then((response) => {
      if (!response.ok) {
        console.error("error response :", response);
      } else {
        return response.json().then((msg) => {
          write(msg);
        });
      }
    })
    .catch((error) => {
      console.error(error);
    });
}

document.getElementById("ping").addEventListener("click", () => {
  ping();
});

// get All Items
function getAllItems() {
  fetch(getUrl("/items"))
    .then((response) => {
      if (!response.ok) {
        console.error("error response :", response);
      } else {
        return response.json().then((items) => {
          write(items);
        });
      }
    })
    .catch((error) => {
      console.error(error);
    });
}

const getAllItemsButton = document.getElementById("get-all-items");
getAllItemsButton.addEventListener("click", () => {
  getAllItems();
});

// get
