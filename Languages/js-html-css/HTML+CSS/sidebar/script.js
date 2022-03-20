const main = document.getElementById("main");
const links = document.getElementsByClassName("link");

for (const link of links) {
  link.addEventListener("click", () => {
    main.textContent = link.textContent;
  });
}