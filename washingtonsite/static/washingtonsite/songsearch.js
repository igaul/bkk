const baseUrl = "/wa/song-search";
const spinnerEl = document.getElementById("spinner");
spinnerEl.style.display = "none";
const searchFormEl = document.getElementById("searchform");
const tableBodyEl = document.getElementById("tbresults");
let lastQuery = "";
let lastFilter = "";
let lastResults = undefined;
let currPage = 0;
const pageSize = 25;

function mountResults(data) {
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

function search(query, filter) {
  spinnerEl.style.display = "block";
  const url =
    baseUrl +
    "?search=" +
    encodeURIComponent(query) +
    "&searchby=" +
    encodeURIComponent(filter);

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

      mountResults(resp.data);
      tableBodyEl.parentElement.parentElement.classList.remove("hidden");
    })
    .catch(console.error)
    .finally(() => (spinnerEl.style.display = "none"));
}

searchFormEl.addEventListener("submit", function (event) {
  event.preventDefault();
  const searchEl = document.getElementById("search");
  const searchbyEl = document.getElementById("searchby");
  const query = searchEl.value;
  const filter = searchbyEl.value;
  if (query !== "") {
    search(query, filter);
  }
});
