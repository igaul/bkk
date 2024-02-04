const baseUrl = "/wa/song-search";
const spinnerEl = document.getElementById("spinner");
const searchFormEl = document.getElementById("searchform");
const tableBodyEl = document.getElementById("tbresults");
const searchEl = document.getElementById("search");
const searchbyEl = document.getElementById("searchby");
spinnerEl.style.display = "none";
let lastQuery = "";
let lastFilter = "";
let lastResults = undefined;
let currPage = 0;
const pageSize = 25;

function renderResults(data) {
  while (tableBodyEl.firstChild) {
    tableBodyEl.removeChild(tableBodyEl.firstChild);
  }
  data.forEach(function (item) {
    const tr = document.createElement("tr");
    const artist = document.createElement("td");
    artist.innerText = item.artist;
    tr.appendChild(artist);
    const title = document.createElement("td");
    title.innerText = item.title;
    tr.appendChild(title);
    tableBodyEl.appendChild(tr);
  });
}

searchFormEl.addEventListener("submit", function (event) {
  event.preventDefault();
  const query = searchEl.value;
  const filter = searchbyEl.value;
  if (!query) return;
  spinnerEl.style.display = "block";
  const url =
    baseUrl + "?search=" + encodeURIComponent(query) + "&searchby=" + filter;

  lastQuery = query;
  lastFilter = filter;

  fetch(url)
    .then(response => response.json())
    .then(resp => {
      if (!resp || !resp.data) {
        throw new Error("no data");
      }
      lastResults = resp.data;

      // const data = resp.data.slice(currPage * pageSize, (currPage + 1) * pageSize);

      renderResults(resp.data);
      tableBodyEl.parentElement.parentElement.classList.remove("hidden");
    })
    .catch(console.error)
    .finally(() => {
      spinnerEl.style.display = "none";
    });
});
