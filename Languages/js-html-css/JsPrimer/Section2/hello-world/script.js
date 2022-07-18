"use strict";

function fetchUserInfo(userId) {
  fetch(`https://api.github.com/users/${encodeURIComponent(userId)}`)
    .then((response) => {
      console.log(response.status);

      // response.ok: Boolean
      if (!response.ok) {
        console.error("error response", response);
      } else {
        return response.json().then((userInfo) => {
          console.log(userInfo);
        });
      }
    })
    .catch((error) => {
      console.error(error);
    });
}
